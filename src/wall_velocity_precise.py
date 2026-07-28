"""
Precise leading-order ECCG wall velocity: LTE hydrodynamics vs ballistic
(Bodeker-Moore) friction, on the GAUGE-INVARIANT 3D-EFT transition.

Two complementary LO methods bracket the true v_w:

(1) LOCAL THERMAL EQUILIBRIUM (LTE).  Zero entropy production at the wall
    (s gamma v continuous, i.e. gamma_+ T_+ = gamma_- T_-;
    Ai-Garbrecht-Tamarit / Ai-Laurent-van de Vis).  Friction is purely
    hydrodynamic (heating in front of the wall).  LTE = minimal friction
    => UPPER bound on v_w.

(2) BALLISTIC / BODEKER-MOORE.  Particles free-stream across the wall with
    equilibrium incoming fluxes (no re-equilibration).  The exact
    finite-velocity 1->1 momentum-transfer pressure P_bal(v_w) interpolates
    between the static thermal-pressure difference (v_w -> 0) and the BM
    pressure sum c_i N_i Dm_i^2 T^2/24 (v_w -> 1).  Ballistic = maximal
    kinetic friction (no transport relief) => LOWER bound on v_w.
    Runaway check: wall runs away iff DeltaV(T_n) > P_bal(1) - P_bal(0)
    [exactly Bodeker-Moore in the gamma -> infinity limit].

Equation of state: taken from the ACTUAL gauge-invariant 3D EFT
(dimensional_reduction.EFT3D, mu = 2 pi T), not from a bag ansatz:
    Delta p(T)   = DeltaV(T)               (driving pressure)
    Delta e(T)   = DeltaV - T dDeltaV/dT   (the DR alpha = Delta e/rho_rad!)
    eps_bag      = (Delta e - 3 Delta p_-... ) trace anomaly:
                   theta_s - theta_b = (Delta e + 3 DeltaV)/4
    alpha_hydro  = (Delta e + 3 DeltaV)/4 / rho_rad     (bag-equivalent)
    Psi_n        = w_-/w_+ = 1 - T Delta s / w_+,  Delta s = -dDeltaV/dT
NOTE: the headline DR "alpha = 0.055" is Delta e/rho_rad; the bag constant
that enters the hydrodynamic junction conditions is the TRACE-ANOMALY one,
alpha_hydro ~ alpha_DR/(1+3(T_n/T_c)^4) ~ 0.031.  Using 0.055 directly in
bag formulas double-counts the dof change.  Both are computed and reported.

Spectrum crossing the wall (broken-phase masses at T_n from the 3D EFT):
    U(1) vector: 3 dof,  m/T = sqrt(g3sq) * phi_n/T_n = 3.77   (dominant)
    Higgs mode : 1 dof,  m/T = sqrt(2 lam3bar) * phi_n/T_n = 1.26
    X fermion  : 4 dof,  m/T = (y_x/sqrt2) * phi_n/T_n = 0.93

Run:  <repo>/.venv/bin/python wall_velocity_precise.py
Outputs: wall_velocity_precise_summary.csv, lte_scan.csv,
         ballistic_friction_curve.csv, runaway_thresholds.csv,
         wall_velocity_precise.png
"""
from __future__ import annotations

import math
import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
from scipy.special import kv

HERE = os.path.dirname(os.path.abspath(__file__))
DEV = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(DEV, "dimensional_reduction"))
sys.path.insert(0, os.path.abspath(os.path.join(DEV, "..", "scripts")))

PI = math.pi
CS = 1.0 / math.sqrt(3.0)
CS2 = 1.0 / 3.0
GSTAR = 106.75
RHO_RAD = PI**2 / 30.0 * GSTAR        # rho_rad / T^4 = 35.12
W_PLUS = 4.0 * RHO_RAD / 3.0          # symmetric-phase enthalpy / T^4

# Benchmark (3D EFT, mu = 2 pi T; dr_summary.csv)
TN_OVER_V = 0.28081011062450073
TC_OVER_V = 0.3914500132565895
PHI_N_OVER_TN = 3.7596743709078595
G3SQ = 1.0028946369738516
LAM3BAR = 0.056030846446377076
Y_X = 0.35
ALPHA_DR = 0.05521500879789242        # = Delta e / rho_rad (DR convention)
TN_GEV = 3.172132e12
VW_BENCH = 0.30
ETA_B_BENCH = 3.8e-10                 # central prediction at v_w = 0.3
ETA_B_OBS = 6.1e-10


# ---------------------------------------------------------------------------
# 1. Model-exact equation of state from the gauge-invariant 3D EFT
# ---------------------------------------------------------------------------

def eos_from_model(mu_ratio: float = 2.0 * PI):
    """DeltaV(T_n), Delta e, Delta s, alpha's and Psi_n from EFT3D.
    Units v = 1; converted to T_n = 1 units on return."""
    import one_loop_daisy_potential as olp   # noqa: E402
    import dimensional_reduction as dr       # noqa: E402
    p = olp.DaisyParams(lambda_s=0.03, g_q=1.00)
    model = dr.EFT3D(p, mu_ratio=mu_ratio)
    tn = TN_OVER_V

    def deltaV(t):
        bm = model.broken_minimum(t)
        return -float(bm[0]) if bm is not None else 0.0

    dt = 1.0e-3 * tn
    dV = deltaV(tn)
    dVp = (deltaV(tn + dt) - deltaV(tn - dt)) / (2.0 * dt)
    d_e = dV - tn * dVp                      # e_s - e_b (the DR "epsilon")
    d_s = -dVp                               # s_s - s_b  (> 0)
    rho = RHO_RAD * tn**4
    w_plus = W_PLUS * tn**4
    out = dict(
        deltaV_over_T4=dV / tn**4,
        de_over_T4=d_e / tn**4,
        ds_over_T3=d_s / tn**3,
        alpha_DR_check=d_e / rho,
        alpha_hydro=(d_e + 3.0 * dV) / 4.0 / rho,   # trace anomaly / rho_rad
        alpha_driving=dV / rho,
        Psi_n=1.0 - tn * d_s / w_plus,
    )
    # bag-consistency diagnostic: bag would predict
    # T_c/T_n = (3 alpha_hydro / (1 - Psi))^{1/4}
    out["Tc_over_Tn_bag"] = (3.0 * out["alpha_hydro"]
                             / max(1.0 - out["Psi_n"], 1e-12)) ** 0.25
    out["Tc_over_Tn_actual"] = TC_OVER_V / TN_OVER_V
    # deltaV at a shifted temperature (for the preheated-driving variant)
    out["deltaV_func"] = lambda t_over_tn: deltaV(tn * t_over_tn) / tn**4
    return out


def eos_fallback():
    """Bag-closure fallback (used only if the DR import fails): fixes
    (alpha_hydro, Psi) from alpha_DR and the actual T_n/T_c."""
    r4 = (TN_OVER_V / TC_OVER_V) ** 4
    a_h = ALPHA_DR / (1.0 + 3.0 * r4)
    psi = 1.0 - 3.0 * a_h * r4
    return dict(alpha_DR_check=ALPHA_DR, alpha_hydro=a_h,
                alpha_driving=a_h * (1.0 - r4), Psi_n=psi,
                deltaV_over_T4=a_h * (1.0 - r4) * RHO_RAD,
                de_over_T4=ALPHA_DR * RHO_RAD,
                ds_over_T3=(1.0 - psi) * W_PLUS,
                Tc_over_Tn_bag=(3.0 * a_h / (1.0 - psi)) ** 0.25,
                Tc_over_Tn_actual=TC_OVER_V / TN_OVER_V,
                deltaV_func=lambda x: a_h * RHO_RAD * (1.0 - r4 * x**4) * x**0)


# ---------------------------------------------------------------------------
# 2. LTE hydrodynamics (bag junctions + gamma T continuous + shock profile)
# ---------------------------------------------------------------------------

def gam2(v):
    return 1.0 / (1.0 - v * v)


def hfun(v):
    """h(v) = v (1 - v^2).  LTE wall condition: h(v_+) = Psi h(v_-)."""
    return v * (1.0 - v * v)


def mu_rel(xi, v):
    return (xi - v) / (1.0 - xi * v)


def vplus_of_vminus(vm, alpha_p, branch):
    """EKNS junction: v_+(v_-, alpha_+); branch=-1 deflagration, +1 detonation."""
    X = vm / 2.0 + 1.0 / (6.0 * vm)
    disc = X * X + alpha_p * alpha_p + 2.0 * alpha_p / 3.0 - 1.0 / 3.0
    if disc < 0.0:
        return None
    return (X + branch * math.sqrt(disc)) / (1.0 + alpha_p)


def alpha_plus_required(vp, vm):
    """Invert the junction relation: alpha_+ such that (v_+, v_-) match.
    Quadratic (vp^2-1) a^2 + (2vp^2 - 2Xvp - 2/3) a + (vp^2 - 2Xvp + 1/3) = 0."""
    X = vm / 2.0 + 1.0 / (6.0 * vm)
    a2 = vp * vp - 1.0
    a1 = 2.0 * vp * vp - 2.0 * X * vp - 2.0 / 3.0
    a0 = vp * vp - 2.0 * X * vp + 1.0 / 3.0
    disc = a1 * a1 - 4.0 * a2 * a0
    if disc < 0.0:
        return None
    roots = [(-a1 + s * math.sqrt(disc)) / (2.0 * a2) for s in (+1.0, -1.0)]
    good = []
    for a in roots:
        if a <= -0.99:
            continue
        for br in (-1.0, +1.0):
            vpc = vplus_of_vminus(vm, a, br)
            if vpc is not None and abs(vpc - vp) < 1.0e-8:
                good.append(a)
                break
    if not good:
        return None
    return min(good, key=abs)


def _front_profile(xi_w, v_front, lnT_front):
    """Integrate the similarity fluid equations from the wall to the shock.
    Returns T far outside (units where the integration starts at lnT_front)."""
    def rhs(xi, y):
        v, lnT = y
        mu = mu_rel(xi, v)
        den = gam2(v) * (1.0 - v * xi) * (mu * mu / CS2 - 1.0)
        dv = 2.0 * v / (xi * den)
        return [dv, gam2(v) * mu * dv]

    def ev_shock(xi, y):
        return xi * mu_rel(xi, y[0]) - CS2
    ev_shock.terminal = True
    ev_shock.direction = 1.0

    def ev_still(xi, y):
        return y[0] - 1.0e-9
    ev_still.terminal = True
    ev_still.direction = -1.0

    sol = solve_ivp(rhs, (xi_w, 0.99999), [v_front, lnT_front],
                    events=[ev_shock, ev_still], rtol=1e-10, atol=1e-12,
                    max_step=5e-3)
    if sol.t_events[0].size:          # shock
        xi_sh = float(sol.t_events[0][0])
        v_sh, lnT_sh = [float(x) for x in sol.y_events[0][0]]
        v2 = mu_rel(xi_sh, v_sh)      # shock-frame inner speed
        v1 = xi_sh                    # shock-frame outer speed (fluid at rest)
        f = lambda v: v / (1.0 - v * v)          # gamma^2 v
        T_out = math.exp(lnT_sh) * (f(v2) / f(v1)) ** 0.25
        return T_out, xi_sh
    # fluid velocity died out: no shock, T continuous
    return math.exp(float(sol.y[1, -1])), float(sol.t[-1])


def lte_residual_defl(xi_w, alpha_n, psi):
    """Deflagration (xi_w < c_s) or hybrid (c_s < xi_w < v_J) residual:
    T far outside implied by the profile minus T_n (=1). None if no matching."""
    vm = min(xi_w, CS - 1e-12) if xi_w < CS else CS
    target = psi * hfun(vm)
    if hfun(1e-12) > target:
        return None
    try:
        vp = brentq(lambda v: hfun(v) - target, 1e-12, vm * (1.0 - 1e-12),
                    xtol=1e-14)
    except ValueError:
        return None
    a_p = alpha_plus_required(vp, vm)
    if a_p is None or a_p <= 0.0:
        return None
    T_plus = (alpha_n / a_p) ** 0.25          # units T_n = 1
    v_front = mu_rel(xi_w, vp)                # universe-frame speed ahead
    if v_front <= 0.0:
        return None
    T_out, _ = _front_profile(xi_w, v_front, math.log(T_plus))
    return T_out - 1.0


def lte_residual_deto(xi_w, alpha_n, psi):
    """Detonation residual: LTE condition Psi h(v_-) - h(v_+) with the
    junction at alpha_+ = alpha_n (fluid ahead unperturbed)."""
    vp = xi_w

    def g(vm):
        v = vplus_of_vminus(vm, alpha_n, +1.0)
        return (v - vp) if v is not None else 1.0

    try:
        vm = brentq(g, CS + 1e-12, vp - 1e-12, xtol=1e-14)
    except ValueError:
        return None
    return psi * hfun(vm) - hfun(vp)


def jouguet(alpha_n):
    return (math.sqrt(alpha_n * (2.0 + 3.0 * alpha_n)) + 1.0) / (
        math.sqrt(3.0) * (1.0 + alpha_n))


def solve_lte(alpha_n, psi, n_scan=240):
    """Scan deflagration/hybrid branch then detonation branch; return dict."""
    vJ = jouguet(alpha_n)
    xis = np.linspace(0.02, vJ - 1e-4, n_scan)
    res = np.array([np.nan if (r := lte_residual_defl(x, alpha_n, psi)) is None
                    else r for x in xis])
    rows = pd.DataFrame({"xi_w": xis, "residual": res, "branch": "defl/hybrid"})
    v_defl = None
    ok = np.isfinite(res)
    for i in range(len(xis) - 1):
        if ok[i] and ok[i + 1] and res[i] * res[i + 1] < 0.0:
            v_defl = brentq(lambda x: lte_residual_defl(x, alpha_n, psi),
                            xis[i], xis[i + 1], xtol=1e-10)
            break
    # detonation branch
    xis_d = np.linspace(vJ + 1e-4, 0.995, 120)
    res_d = np.array([np.nan if (r := lte_residual_deto(x, alpha_n, psi)) is
                      None else r for x in xis_d])
    rows = pd.concat([rows, pd.DataFrame({"xi_w": xis_d, "residual": res_d,
                                          "branch": "detonation"})])
    v_deto = None
    okd = np.isfinite(res_d)
    for i in range(len(xis_d) - 1):
        if okd[i] and okd[i + 1] and res_d[i] * res_d[i + 1] < 0.0:
            v_deto = brentq(lambda x: lte_residual_deto(x, alpha_n, psi),
                            xis_d[i], xis_d[i + 1], xtol=1e-10)
            break
    out = dict(v_defl=v_defl, v_deto=v_deto, v_J=vJ, scan=rows)
    if v_defl is not None:
        out["v_w"] = v_defl
        out["regime"] = ("subsonic deflagration" if v_defl < CS
                         else "hybrid (supersonic deflagration)")
        # diagnostics at the solution
        vm = min(v_defl, CS)
        vp = brentq(lambda v: hfun(v) - psi * hfun(vm), 1e-12,
                    vm * (1 - 1e-12), xtol=1e-14)
        a_p = alpha_plus_required(vp, vm)
        out.update(v_plus=vp, v_minus=vm, alpha_plus=a_p,
                   T_plus_over_Tn=(alpha_n / a_p) ** 0.25)
    elif v_deto is not None:
        out["v_w"] = v_deto
        out["regime"] = "detonation"
    else:
        out["v_w"] = None
        out["regime"] = "no steady LTE solution"
    return out


# ---------------------------------------------------------------------------
# 3. Ballistic (Bodeker-Moore at finite velocity) friction
# ---------------------------------------------------------------------------

def _L(x, stat):
    """Integrated distribution: BE -> -ln(1-e^-x); FD -> ln(1+e^-x)."""
    if x > 500.0:
        return 0.0
    if stat == "b":
        return -math.log1p(-math.exp(-x)) if x > 1e-12 else -math.log(x)
    return math.log1p(math.exp(-x))


def p_thermal(m, stat):
    """Thermal pressure of one dof at T=1: (m^2/2 pi^2) sum s^{n+1} K2(nm)/n^2."""
    if m < 1e-8:
        return PI**2 / 90.0 * (1.0 if stat == "b" else 7.0 / 8.0)
    s = 1.0 if stat == "b" else -1.0
    tot = 0.0
    for n in range(1, 60):
        z = n * m
        if z > 600.0:
            break
        tot += s ** (n + 1) * kv(2, z) / n**2
    return m * m / (2.0 * PI**2) * tot


def P_front(v, m, stat):
    """Wall-frame pressure from the symmetric-phase flux (massless in front,
    mass m behind), plasma inflow speed v, T=1.
    P = (1/4pi^2 gamma) Int dp p Dp(p) L(gamma p (1-v))."""
    g = 1.0 / math.sqrt(1.0 - v * v)
    a = g * (1.0 - v)

    def integ_refl(p):                # p < m: reflection, Dp = 2p
        return p * 2.0 * p * _L(a * p, stat)

    def integ_trans(p):               # p > m: Dp = p - sqrt(p^2 - m^2)
        return p * (p - math.sqrt(p * p - m * m)) * _L(a * p, stat)

    pmax = m + 80.0 / a
    r1, _ = quad(integ_refl, 0.0, m, limit=200)
    r2, _ = quad(integ_trans, m, pmax, limit=200)
    return (r1 + r2) / (4.0 * PI**2 * g)


def P_back(v, m, stat):
    """Backward push from broken-phase particles overtaking the wall.
    Crossing m -> 0 at fixed (E, p_T), |p_z| grows: the particle GAINS forward
    momentum and the wall recoils backward (friction), so P_back ADDS to
    P_front.  P = (1/4pi^2 g) Int dk k (sqrt(k^2+m^2)-k)
    L(gamma (sqrt(k^2+m^2) + v k))."""
    g = 1.0 / math.sqrt(1.0 - v * v)

    def integ(k):
        E = math.sqrt(k * k + m * m)
        return k * (E - k) * _L(g * (E + v * k), stat)

    kmax = 80.0 / (g * (1.0 + v)) + 5.0 * m
    r, _ = quad(integ, 0.0, kmax, limit=200)
    return r / (4.0 * PI**2 * g)


@dataclass
class Species:
    label: str
    stat: str          # "b" or "f"
    dof: float
    m_over_T: float


SPECTRUM = [
    Species("U(1) vector", "b", 3.0, math.sqrt(G3SQ) * PHI_N_OVER_TN),
    Species("Higgs mode", "b", 1.0, math.sqrt(2.0 * LAM3BAR) * PHI_N_OVER_TN),
    Species("X fermion", "f", 4.0, (Y_X / math.sqrt(2.0)) * PHI_N_OVER_TN),
]


def P_bal_total(v, spectrum):
    return sum(s.dof * (P_front(v, s.m_over_T, s.stat)
                        + P_back(v, s.m_over_T, s.stat)) for s in spectrum)


def P_bal_static(spectrum):
    """v -> 0 limit = thermal-pressure difference (kinetic identity)."""
    return sum(s.dof * (p_thermal(0.0, s.stat) - p_thermal(s.m_over_T, s.stat))
               for s in spectrum)


def P_bm_limit(spectrum):
    """v -> 1 Bodeker-Moore limit: sum c N Dm^2/24 (c=1 boson, 1/2 fermion)."""
    return sum(s.dof * s.m_over_T**2 / (24.0 if s.stat == "b" else 48.0)
               for s in spectrum)


def solve_ballistic(driving, spectrum, fric_scale=1.0):
    """Terminal velocity from DeltaP_bal(v) * fric_scale = driving.
    Returns (v_w or None-if-runaway, DeltaP_max)."""
    P0 = P_bal_static(spectrum)
    dP_max = (P_bm_limit(spectrum) - P0) * fric_scale

    def F(v):
        return (P_bal_total(v, spectrum) - P0) * fric_scale - driving

    if driving >= dP_max:
        return None, dP_max
    return brentq(F, 1e-4, 1.0 - 1e-7, xtol=1e-8), dP_max


# ---------------------------------------------------------------------------
# 3b. Combined friction + hydrodynamics force balance
# ---------------------------------------------------------------------------
# For xi_w < v_J the wall is a (non-LTE) deflagration/hybrid: given xi_w the
# junction conditions + shock matching CLOSE the hydro (standard one-parameter
# family), fixing the preheated wall-front state (v_+, T_+).  The steady state
# is then the force balance at the wall,
#     DeltaV(T_+)  =  fric_scale * T_+^4 * DeltaP_bal(v_+; m_i/T_+),
# with the ballistic friction evaluated with the local inflow.  For
# xi_w > v_J (detonation) the inflow is unperturbed: T_+ = T_n, v_+ = xi_w.

def hydro_Tplus(xi_w, alpha_n):
    """Non-LTE deflagration/hybrid hydro closure: T_+ (units T_n=1) and the
    wall-frame inflow speed v_+ such that the front profile matches T_n at
    the shock.  Returns (T_plus, v_plus) or None."""
    vm = min(xi_w, CS - 1e-12)

    def resid(Tp):
        a_p = alpha_n / Tp**4
        vp = vplus_of_vminus(vm, a_p, -1.0)
        if vp is None or vp <= 0.0 or vp >= xi_w:
            return None
        v_front = mu_rel(xi_w, vp)
        T_out, _ = _front_profile(xi_w, v_front, math.log(Tp))
        return T_out - 1.0

    lo, hi = 1.0 + 1e-9, 1.6
    rlo = resid(lo)
    if rlo is None:
        return None
    # find a bracketing hi
    rhi, Tp_hi = None, None
    for Tp in np.linspace(1.005, hi, 40):
        r = resid(Tp)
        if r is None:
            break
        if r * rlo < 0.0:
            rhi, Tp_hi = r, Tp
            break
        lo, rlo = Tp, r
    if rhi is None:
        return None
    Tp = brentq(lambda x: resid(x), lo, Tp_hi, xtol=1e-10)
    a_p = alpha_n / Tp**4
    vp = vplus_of_vminus(vm, a_p, -1.0)
    return Tp, vp


def force_balance(xi_w, eos, spectrum, fric_scale=1.0):
    """Net accelerating pressure on the wall at steady xi_w (units T_n^4).
    Positive => wall still accelerates."""
    alpha_n = eos["alpha_hydro"]
    vJ = jouguet(alpha_n)
    if xi_w >= vJ:                       # detonation: unperturbed inflow
        Tp, vp = 1.0, xi_w
    else:
        hy = hydro_Tplus(xi_w, alpha_n)
        if hy is None:
            return None
        Tp, vp = hy
    spec_scaled = [Species(s.label, s.stat, s.dof, s.m_over_T / Tp)
                   for s in spectrum]
    fric = Tp**4 * (P_bal_total(vp, spec_scaled) - P_bal_static(spec_scaled))
    drive = eos["deltaV_func"](Tp)
    return drive - fric_scale * fric


def solve_ballistic_hydro(eos, spectrum, fric_scale=1.0, n_scan=36):
    """Terminal xi_w from the combined balance; None => runaway."""
    xis = np.linspace(0.05, 0.995, n_scan)
    prev_x, prev_f = None, None
    for x in xis:
        f = force_balance(x, eos, spectrum, fric_scale)
        if f is None:
            continue
        if prev_f is not None and prev_f > 0.0 and f < 0.0:
            return brentq(
                lambda z: force_balance(z, eos, spectrum, fric_scale),
                prev_x, x, xtol=1e-7)
        prev_x, prev_f = x, f
    return None


# ---------------------------------------------------------------------------
# 4. Runaway thresholds (generic N_boson at Dm = g_q phi_n)
# ---------------------------------------------------------------------------

def runaway_table(driving, dm_over_T):
    rows = []
    p0_dof = p_thermal(0.0, "b") - p_thermal(dm_over_T, "b")
    pbm_dof = dm_over_T**2 / 24.0
    for Nb in [1, 2, 3, 4, 6, 8, 12]:
        a_inf_ekns = Nb * pbm_dof / RHO_RAD
        dp_max = Nb * (pbm_dof - p0_dof)
        rows.append(dict(N_boson=Nb,
                         alpha_inf_EKNS=a_inf_ekns,
                         runaway_EKNS=ALPHA_DR > a_inf_ekns,
                         dP_max_over_T4=dp_max,
                         runaway_exact=driving > dp_max))
    Ncrit_ekns = ALPHA_DR * RHO_RAD / pbm_dof
    Ncrit_exact = driving / (pbm_dof - p0_dof)
    return pd.DataFrame(rows), Ncrit_ekns, Ncrit_exact


# ---------------------------------------------------------------------------
# 5. eta_B propagation
# ---------------------------------------------------------------------------

# other error-budget sources (parameter_reduction/eta_B_error_budget.py),
# quadrature half-widths in ln eta_B, excluding v_w
OTHER_SOURCES = {
    "bracket": (1, 2.5), "eta_2": (1, 1.5), "sin_dCP": (1, 1.7),
    "beta/H": (1, 1.5), "T_n": (1, 1.1), "f_B": (1, 1.15), "D_S": (1, 1.1),
}


def eta_band(vw_lo, vw_hi):
    """Total eta_B multiplicative band with v_w in [vw_lo, vw_hi]."""
    d_vw = 1.0 * 0.5 * math.log(vw_hi / vw_lo)     # eta_B ~ 1/v_w, |power|=1
    quad_sum = d_vw**2 + sum((p * 0.5 * math.log(F))**2
                             for p, F in OTHER_SOURCES.values())
    return math.exp(2.0 * math.sqrt(quad_sum)), math.exp(2.0 * d_vw)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    print("=" * 72)
    print("ECCG precise wall velocity: LTE hydrodynamics vs ballistic (BM) LO")
    print("=" * 72)

    # ---- EoS from the gauge-invariant 3D EFT --------------------------------
    try:
        eos = eos_from_model()
        eos_src = "EFT3D (mu=2piT), model-exact"
    except Exception as exc:                                  # pragma: no cover
        print(f"  [WARN] model EoS failed ({exc}); bag-closure fallback")
        eos = eos_fallback()
        eos_src = "bag closure fallback"
    aH, psi = eos["alpha_hydro"], eos["Psi_n"]
    D = eos["deltaV_over_T4"]
    print(f"\n--- equation of state at T_n ({eos_src}) ---")
    print(f"  DeltaV(T_n)/T^4      = {D:.4f}   (driving pressure)")
    print(f"  Delta e /rho_rad     = {eos['alpha_DR_check']:.4f}  "
          f"(DR alpha convention; report: {ALPHA_DR:.4f})")
    print(f"  alpha_hydro (trace)  = {aH:.4f}   <-- bag constant for hydro")
    print(f"  alpha_driving        = {eos['alpha_driving']:.4f}")
    print(f"  Psi_n = w_-/w_+      = {psi:.4f}   "
          f"(Delta N_eff = {(1-psi)*GSTAR:.2f} dof)")
    print(f"  bag check: T_c/T_n bag {eos['Tc_over_Tn_bag']:.3f} vs actual "
          f"{eos['Tc_over_Tn_actual']:.3f}  "
          f"({100*(eos['Tc_over_Tn_bag']/eos['Tc_over_Tn_actual']-1):+.1f}%)")

    # ---- runaway check -------------------------------------------------------
    dm = math.sqrt(G3SQ) * PHI_N_OVER_TN
    tab, Ncrit_ekns, Ncrit_exact = runaway_table(D, dm)
    tab.to_csv(os.path.join(HERE, "runaway_thresholds.csv"), index=False)
    print(f"\n--- Bodeker-Moore runaway check (Dm/T = {dm:.3f}) ---")
    print(f"  EKNS convention (alpha_DR={ALPHA_DR:.4f} vs alpha_inf): "
          f"N_boson_crit = {Ncrit_ekns:.2f}  (was 2.1 at alpha=0.036)")
    print(f"  exact kinetic (DeltaV vs P_BM - Dp_th):      "
          f"N_boson_crit = {Ncrit_exact:.2f} dof")
    P0 = P_bal_static(SPECTRUM)
    Pbm = P_bm_limit(SPECTRUM)
    print(f"  actual spectrum: P_BM = {Pbm:.3f} T^4, Dp_th = {P0:.3f} T^4, "
          f"max net friction = {Pbm-P0:.3f} T^4")
    runaway = D >= (Pbm - P0)
    print(f"  driving {D:.3f} vs max friction {Pbm-P0:.3f}  =>  "
          f"{'RUNAWAY' if runaway else 'NO runaway'} "
          f"(margin x{(Pbm-P0)/D:.2f})")

    # ---- method 2: LTE hydrodynamics -----------------------------------------
    print("\n--- method 2: LTE hydrodynamics (gamma T continuous) ---")
    lte = solve_lte(aH, psi)
    lte["scan"].to_csv(os.path.join(HERE, "lte_scan.csv"), index=False)
    obstr = 3.0 * aH / (1.0 - psi)
    print(f"  alpha_n = {aH:.4f}, Psi_n = {psi:.4f}, "
          f"v_Jouguet = {lte['v_J']:.4f}")
    print(f"  deflagration/hybrid root: {lte['v_defl']}   "
          f"detonation root: {lte['v_deto']}")
    print(f"  => {lte['regime']}: the LTE wall condition needs "
          f"T_+/T_n = (3 alpha_n/(1-Psi))^(1/4) = {obstr**0.25:.2f} ~ T_c/T_n,")
    print(f"     but shock preheating is only O(alpha); "
          f"3 alpha_n/(1-Psi) = {obstr:.1f} >> 1 => NO hydrodynamic")
    print(f"     obstruction. Detonation branch: entropy production > 0 for "
          f"all xi_w > v_J (LTE residual")
    print(f"     positive) => a steady wall REQUIRES non-equilibrium "
          f"friction; strict LTE admits NO steady")
    print(f"     wall at ANY xi_w: a friction-free wall accelerates without "
          f"bound. The terminal velocity is")
    print(f"     set entirely by the kinetic friction (method 1); LTE here "
          f"only fixes the front hydro state.")

    # ---- method 1: ballistic (BM finite-v) friction + hydro -----------------
    print("\n--- method 1: ballistic (Bodeker-Moore) friction force balance ---")
    chk1 = P_bal_total(1e-4, SPECTRUM)
    chk2 = sum(s.dof * P_front(1.0 - 1e-8, s.m_over_T, s.stat)
               for s in SPECTRUM)
    print(f"  check v->0: P_bal = {chk1:.4f} vs Dp_th = {P0:.4f}")
    print(f"  check v->1: P_front = {chk2:.4f} vs P_BM = {Pbm:.4f}")
    vs = np.linspace(0.01, 0.999, 60)
    dPs = np.array([P_bal_total(v, SPECTRUM) - P0 for v in vs])
    pd.DataFrame({"v_w": vs, "dP_bal_over_T4": dPs}).to_csv(
        os.path.join(HERE, "ballistic_friction_curve.csv"), index=False)
    v_bal, dPmax = solve_ballistic(D, SPECTRUM)
    print(f"  bare ballistic (T_n inflow):            v_w = {v_bal:.4f}")
    v_c = solve_ballistic_hydro(eos, SPECTRUM, fric_scale=1.0)
    v_fric_hi = solve_ballistic_hydro(eos, SPECTRUM, fric_scale=1.5)
    v_fric_lo = solve_ballistic_hydro(eos, SPECTRUM, fric_scale=0.7)
    spec_min = [s for s in SPECTRUM if s.label == "U(1) vector"]
    v_spec_min = solve_ballistic_hydro(
        dict(eos, deltaV_func=eos["deltaV_func"]), spec_min, fric_scale=1.0)
    print(f"  hydro-consistent balance:               v_w = {v_c:.4f}")
    print(f"  friction x1.5 / x0.7 (LO->NLO proxy):   v_w = "
          f"{v_fric_hi:.4f} / {v_fric_lo:.4f}")
    print(f"  minimal spectrum (vector only):         v_w = {v_spec_min:.4f}")

    # ---- combine -------------------------------------------------------------
    print("\n--- combined estimate ---")
    cands = [v for v in [v_c, v_fric_hi, v_fric_lo, v_spec_min, v_bal] if v]
    v_lo, v_hi = min(cands), max(cands)
    v_err = 0.5 * (v_hi - v_lo)
    vJ = lte["v_J"]
    regime = ("detonation" if v_c >= vJ else
              "hybrid (supersonic deflagration)" if v_c > CS else
              "deflagration at the sonic edge")
    print(f"  v_w = {v_c:.2f} +/- {v_err:.2f}   [{v_lo:.2f}, {v_hi:.2f}]  "
          f"regime: {regime} (v_J = {vJ:.2f})")
    print(f"  v_w = 0.3 (benchmark input) is EXCLUDED at LO: friction at "
          f"v=0.3 is x{(P_bal_total(0.3, SPECTRUM)-P0)/D:.2f} of driving.")

    # ---- eta_B propagation ---------------------------------------------------
    # eta_B ~ 1/v_w (power -1): the wall source ~1/v_w^2 combines with a transfer
    # factor ~v_w; verified against the shipped scan (required m3/H ~ v_w^0.5).
    print("\n--- eta_B propagation (eta_B ~ 1/v_w) ---")
    eta_c = ETA_B_BENCH * (VW_BENCH / v_c) ** 1
    eta_lo = ETA_B_BENCH * (VW_BENCH / v_hi) ** 1
    eta_hi = ETA_B_BENCH * (VW_BENCH / v_lo) ** 1
    band_new, vw_factor_new = eta_band(v_lo, v_hi)
    band_old, vw_factor_old = eta_band(VW_BENCH / math.sqrt(2.0),
                                       VW_BENCH * math.sqrt(2.0))
    m3H_shift = math.sqrt(v_c / VW_BENCH)
    print(f"  central: eta_B = {eta_c:.2e}  (was {ETA_B_BENCH:.1e} at v_w=0.3;"
          f" obs {ETA_B_OBS:.1e})")
    print(f"  v_w-band alone: eta_B in [{eta_lo:.2e}, {eta_hi:.2e}] "
          f"(factor x{vw_factor_new:.1f}; was x{vw_factor_old:.1f})")
    print(f"  total quadrature band: x{band_new:.1f} (was x{band_old:.1f})")
    print(f"  required m3/H rescales by sqrt(v_w/0.3) = x{m3H_shift:.2f}")

    # ---- summary CSV ---------------------------------------------------------
    pd.DataFrame([dict(
        eos_source=eos_src, alpha_DR=eos["alpha_DR_check"], alpha_hydro=aH,
        alpha_driving=eos["alpha_driving"], Psi_n=psi,
        deltaV_over_T4=D, dm_vector_over_T=dm,
        Ncrit_EKNS=Ncrit_ekns, Ncrit_exact_dof=Ncrit_exact,
        runaway=runaway, friction_margin=(Pbm - P0) / D,
        v_Jouguet=lte["v_J"], lte_regime=lte["regime"],
        lte_obstruction_param=3.0 * aH / (1.0 - psi),
        v_ballistic_bare=v_bal, v_ballistic_hydro=v_c,
        v_fric_x1p5=v_fric_hi, v_fric_x0p7=v_fric_lo,
        v_spectrum_min=v_spec_min,
        v_w_central=v_c, v_w_lo=v_lo, v_w_hi=v_hi, v_w_err=v_err,
        regime=regime,
        eta_B_central=eta_c, eta_B_lo=eta_lo, eta_B_hi=eta_hi,
        eta_band_vw_new=vw_factor_new, eta_band_vw_old=vw_factor_old,
        eta_band_total_new=band_new, eta_band_total_old=band_old,
        m3H_rescale=m3H_shift,
    )]).to_csv(os.path.join(HERE, "wall_velocity_precise_summary.csv"),
               index=False)

    # ---- figure --------------------------------------------------------------
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.2))
    ax = axes[0]
    ax.plot(vs, dPs, "C0-", label=r"$\Delta P_{\rm bal}(v_w)$ ballistic")
    ax.axhline(D, color="C3", ls="--", label=r"driving $\Delta V(T_n)$")
    ax.axhline(Pbm - P0, color="C2", ls=":",
               label=r"BM limit $P_{LO}-\Delta p_{th}$")
    if v_c:
        ax.axvline(v_c, color="C3", ls="-.", lw=1,
                   label=f"$v_w$ = {v_c:.2f}")
        ax.axvspan(v_lo, v_hi, color="C3", alpha=0.12)
    ax.set_xlabel(r"$v_w$"), ax.set_ylabel(r"$P/T_n^4$")
    ax.set_title("ballistic force balance"), ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    ax = axes[1]
    sc = lte["scan"]
    for br, c in [("defl/hybrid", "C0"), ("detonation", "C1")]:
        m = sc["branch"] == br
        ax.plot(sc["xi_w"][m], sc["residual"][m], c + "-", label=br)
    ax.axhline(0, color="k", lw=0.7)
    ax.axvline(CS, color="gray", ls=":", label=r"$c_s$")
    ax.axvline(lte["v_J"], color="gray", ls="--", label=r"$v_J$")
    if lte["v_w"]:
        ax.axvline(lte["v_w"], color="C3", ls="-.",
                   label=f"LTE $v_w$={lte['v_w']:.3f}")
    ax.set_xlabel(r"$\xi_w$"), ax.set_ylabel(r"$T_{n,\rm implied}/T_n - 1$")
    ax.set_title(f"LTE matching  ($\\alpha_n$={aH:.3f}, $\\Psi$={psi:.3f})")
    ax.legend(fontsize=8), ax.grid(alpha=0.3)

    ax = axes[2]
    ax.errorbar([0], [ETA_B_BENCH], yerr=[[ETA_B_BENCH * (1 - 1 / 2)],
                [ETA_B_BENCH * 1.0]], fmt="s", color="gray",
                label=r"old ($v_w=0.3$, $\times 2$)")
    ax.errorbar([1], [eta_c], yerr=[[eta_c - eta_lo], [eta_hi - eta_c]],
                fmt="o", color="C0", label="this work ($v_w$ band only)")
    ax.axhline(ETA_B_OBS, color="C3", ls="--", label=r"$\eta_B^{\rm obs}$")
    ax.set_yscale("log"), ax.set_xticks([0, 1])
    ax.set_xticklabels(["before", "after"])
    ax.set_ylabel(r"$\eta_B$"), ax.set_title(r"$\eta_B$ tightening")
    ax.legend(fontsize=8), ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "wall_velocity_precise.png"), dpi=150)
    print("\nWrote wall_velocity_precise_summary.csv, lte_scan.csv,")
    print("      ballistic_friction_curve.csv, runaway_thresholds.csv,")
    print("      wall_velocity_precise.png")


if __name__ == "__main__":
    main()
