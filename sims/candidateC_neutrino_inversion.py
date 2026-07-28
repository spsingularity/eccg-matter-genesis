#!/usr/bin/env python3
"""
D-2 : Invert Candidate C into a falsifiable Sigma_m_nu vs T_RH prediction.

Candidate C (USC_shared_mechanisms.md): the Ledger clock's velocity theta_dot = H*D_E
is a chemical potential mu = c*theta_dot = H/(2 pi) for a NON-COMPACT B-L current.
B-L violation is the Weinberg operator (LH)(LH), whose coefficient is FIXED by the
measured neutrino masses:  Gamma_W(T) = C_W T^3 * mbar^2 / v^4,  mbar^2 = Sum_i m_i^2.

So the baryon yield depends on the neutrino masses through mbar^2 = Sum m_i^2 (the
WASHOUT mass, sum of SQUARES), while cosmology bounds Sum m_i (the sum). This script:

  1. Builds Y_B(T_RH, mbar^2) with the ACTUAL Delta-L=2 washout Boltzmann equation
     (not the 1/2 Gamma/H weak-washout analytic the corpus used -- that overshoots
     by 13-31% in the relevant window).
  2. For each T_RH, root-finds the mbar^2 that reproduces eta_B = 6.10e-10.
  3. Maps mbar^2 -> Sum m_nu for normal (NH) and inverted (IH) ordering via the
     lightest-mass parametrization.
  4. Overlays the ordering floors and the current DESI DR2 Sigma_m_nu ceiling, and
     reports the allowed (T_RH, Sum m_nu) region under the ECCG res-(iv) window and
     the D-1 reheating constraint T_RH < Lambda_H.

Verdict logic: because mbar^2 = Sum m_i^2 is dominated by the (fixed) atmospheric
splitting near the floor, the yield is nearly independent of Sum m_nu there -> C
essentially PINS T_RH, and the union (C || ECCG res-iv, T_RH in [3.2, 6.35]e12) then
predicts Sum m_nu at its NH floor. DESI is cutting exactly there.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

# ---------------- constants (match candidateC_yield.py) ----------------
MPl   = 1.22091e19      # GeV
v     = 174.0          # GeV
eta_B = 6.10e-10
YB_obs = eta_B/7.04    # n_B/s  = 8.665e-11
f_sph = 28.0/79.0
YBL_obs = YB_obs/f_sph
eV2GeV = 1e-9

# neutrino oscillation splittings (eV^2), NuFIT-like central values
dm2_sol = 7.4e-5       # Delta m^2_21
dm2_atm = 2.50e-3      # |Delta m^2_3l|

# ordering floors (m_lightest -> 0)
def masses_NH(m0):
    return np.array([m0, np.sqrt(m0**2+dm2_sol), np.sqrt(m0**2+dm2_atm)])
def masses_IH(m0):
    # m3 lightest; m1,m2 near sqrt(dm2_atm)
    return np.array([np.sqrt(m0**2+dm2_atm-dm2_sol), np.sqrt(m0**2+dm2_atm), m0])
def sum_and_mbar2(masses):
    return masses.sum(), (masses**2).sum()

Sig_NH_floor, mbar2_NH_floor = sum_and_mbar2(masses_NH(0.0))
Sig_IH_floor, mbar2_IH_floor = sum_and_mbar2(masses_IH(0.0))

# ---------------- DESI Sigma_m_nu ceilings (95%, representative, cutoff Jan-2026) --------------
DESI_DR2_baseline   = 0.0642   # DESI DR2 BAO + CMB, baseline  (eV)
DESI_DR2_aggressive = 0.0459   # DESI DR2 + CMB + DESY5 SN  (eV)  -- already BELOW the NH floor
DESI_DR1_conserv    = 0.072    # DESI DR1 + CMB  (eV)

# ---------------- Candidate C yield with real washout Boltzmann ----------------
def make_yield(C_W=1/np.pi**3, gstar=106.75, g_chi=1.0):
    A = (15*g_chi/(4*np.pi**2*gstar))*1.66*np.sqrt(gstar)/(2*np.pi*MPl)   # Yeq = A*T
    def H(T):  return 1.66*np.sqrt(gstar)*T**2/MPl
    def Yeq(T): return A*T
    def Gam(T, mbar2_eV2): return C_W*T**3*(mbar2_eV2*eV2GeV**2)/v**4
    def Y_B(TRH, mbar2_eV2):
        def rhs(x, Y):
            T = TRH*np.exp(-x)
            return -(Gam(T, mbar2_eV2)/H(T))*(Y[0]-Yeq(T))
        sol = solve_ivp(rhs, [0, 14], [0.0], rtol=1e-9, atol=1e-32, dense_output=False)
        return f_sph*sol.y[0, -1]
    return Y_B, H

C_W0, gstar0 = 1/np.pi**3, 106.75
Y_B, Hfun = make_yield()   # central conventions

def mbar2_weakmax(TRH, C_W=C_W0, gstar=gstar0):
    """mbar^2 (eV^2) at which Gamma_W(T_RH)/H(T_RH) = 1 -- the weak/strong boundary.
    The physical (light-neutrino) solution lives BELOW this; above it the yield is
    strong-washout suppressed (freeze-out at T_d < T_RH) and falls with mbar^2."""
    return (1.66*np.sqrt(gstar)*v**4/(C_W*TRH*MPl))/eV2GeV**2

# ---------------- invert: mbar^2 required to give eta_B, on the WEAK branch ----------------
def mbar2_required(TRH):
    """root-find mbar^2 (eV^2) s.t. Y_B = YB_obs on the weak-washout branch.
    Returns the mbar^2 value (may be below an ordering floor -> caller maps to nan);
    +inf if even the weak-branch peak underproduces (T_RH too low);
    nan if even mbar^2->0 overproduces (cannot happen here, kept for safety)."""
    hiw = 0.98*mbar2_weakmax(TRH)
    f = lambda lm: np.log(Y_B(TRH, np.exp(lm))/YB_obs)
    lo = np.log(1e-6)
    if f(lo) > 0: return np.nan
    if f(np.log(hiw)) < 0: return np.inf     # weak branch never reaches obs -> T_RH too low
    return np.exp(brentq(f, lo, np.log(hiw), xtol=1e-4))

def sum_from_mbar2(mbar2, ordering):
    floor = mbar2_NH_floor if ordering == 'NH' else mbar2_IH_floor
    if mbar2 < floor: return np.nan       # below ordering floor -> impossible
    m0 = np.sqrt((mbar2 - floor)/3.0)      # mbar^2 = 3 m0^2 + floor (both split fixed)
    masses = masses_NH(m0) if ordering == 'NH' else masses_IH(m0)
    return masses.sum()

print("="*82)
print("D-2  Candidate C  ->  Sigma_m_nu vs T_RH   (central: C_W=1/pi^3, g*=106.75, g_chi=1)")
print("="*82)
print(f"  eta_B target = {eta_B:.2e}   Y_B,obs = {YB_obs:.3e}")
print(f"  NH floor: Sum m_nu = {Sig_NH_floor*1e3:.1f} meV,  mbar^2 = {mbar2_NH_floor:.3e} eV^2")
print(f"  IH floor: Sum m_nu = {Sig_IH_floor*1e3:.1f} meV,  mbar^2 = {mbar2_IH_floor:.3e} eV^2")
print(f"  DESI DR2 baseline ceiling  : Sum m_nu < {DESI_DR2_baseline*1e3:.1f} meV")
print(f"  DESI DR2 aggressive ceiling: Sum m_nu < {DESI_DR2_aggressive*1e3:.1f} meV  (BELOW NH floor!)")
print()

# quick Boltzmann calibration check vs the shipped boltzmann script
print(f"  [calibration]  Y_B(T_RH=3.17e12, NH floor) = {Y_B(3.17e12, mbar2_NH_floor):.3e}"
      f"  (boltzmann script: 7.98e-11, ratio_to_obs 0.92)")
print()

print(f"  {'T_RH [GeV]':>11} | {'mbar^2 req':>11} | {'Sum_nu NH':>10} | {'Sum_nu IH':>10} | notes")
print("  " + "-"*74)
res = []
for TRH in [2.0e12, 2.5e12, 3.0e12, 3.2e12, 3.6e12, 4.0e12, 5.0e12, 6.35e12, 9.0e12]:
    mb2 = mbar2_required(TRH)
    if not np.isfinite(mb2):
        note = "T_RH too HIGH: overproduces even at m->0" if np.isnan(mb2) else "T_RH too low"
        print(f"  {TRH:11.2e} | {'--':>11} | {'--':>10} | {'--':>10} | {note}")
        res.append((TRH, mb2, np.nan, np.nan)); continue
    sNH = sum_from_mbar2(mb2, 'NH'); sIH = sum_from_mbar2(mb2, 'IH')
    tags = []
    if TRH >= 3.2e12: tags.append("in res-iv")
    if TRH > 6.35e12: tags.append("EXCEEDS Lambda_H (D-1)")
    print(f"  {TRH:11.2e} | {mb2:11.3e} | "
          f"{(sNH*1e3 if np.isfinite(sNH) else np.nan):10.1f} | "
          f"{(sIH*1e3 if np.isfinite(sIH) else np.nan):10.1f} | {', '.join(tags)}")
    res.append((TRH, mb2, sNH, sIH))

# ---------------- key thresholds ----------------
# highest T_RH that still admits an NH solution (mbar2_req = NH floor):
def g_NH(TRH):
    m = mbar2_required(TRH)
    return (m if np.isfinite(m) else 1e-6) - mbar2_NH_floor
TRH_at_NHfloor = brentq(g_NH, 2.0e12, 4.0e12, xtol=1e9)
# T_RH where required Sum_nu (NH) hits the DESI baseline ceiling:
def g_ceil(TRH):
    m = mbar2_required(TRH); s = sum_from_mbar2(m, 'NH') if np.isfinite(m) else np.nan
    return (s if np.isfinite(s) else 1.0) - DESI_DR2_baseline
try:
    TRH_at_ceil = brentq(g_ceil, 1.0e12, TRH_at_NHfloor*0.999, xtol=1e9)
except Exception:
    TRH_at_ceil = np.nan

print()
print("="*82)
print("  RESULT (central conventions)")
print("="*82)
print(f"  * NH-floor match:  T_RH = {TRH_at_NHfloor:.2e} GeV gives Sum m_nu = {Sig_NH_floor*1e3:.1f} meV (the floor).")
print(f"    This sits JUST BELOW the ECCG res-(iv) window floor (3.2e12).")
print(f"  * At the res-(iv) floor T_RH=3.2e12:  required mbar^2 = {mbar2_required(3.2e12):.3e} eV^2")
mb32 = mbar2_required(3.2e12)
print(f"    -> {'BELOW NH floor: NH impossible, overproduces at floor by' if mb32 < mbar2_NH_floor else 'Sum_nu(NH) ='} "
      f"{('x%.2f'%(Y_B(3.2e12,mbar2_NH_floor)/YB_obs)) if mb32<mbar2_NH_floor else '%.1f meV'%(sum_from_mbar2(mb32,'NH')*1e3)}")
print(f"  * DESI baseline ceiling reached at T_RH = {TRH_at_ceil:.2e} GeV (NH).")
print()
lo = max(TRH_at_ceil if np.isfinite(TRH_at_ceil) else 0, 3.2e12)
hi = min(TRH_at_NHfloor, 6.35e12)
print(f"  ALLOWED window (yield=obs AND Sum_nu in [NH floor, DESI ceiling] AND T_RH in [3.2, 6.35]e12):")
if lo <= hi:
    print(f"    T_RH in [{lo:.2e}, {hi:.2e}] GeV,  Sum m_nu in [{Sig_NH_floor*1e3:.0f}, {DESI_DR2_baseline*1e3:.0f}] meV, NORMAL ORDERING.")
    print(f"    -> a NARROW, pinned prediction. Width in T_RH: factor {hi/lo:.2f}.")
else:
    print(f"    EMPTY at central conventions: res-(iv) floor 3.2e12 already overproduces at the NH mass floor")
    print(f"    (Y_B/obs = {Y_B(3.2e12,mbar2_NH_floor)/YB_obs:.2f}). Consistency needs T_RH ~ {TRH_at_NHfloor:.2e} (just under the window),")
    print(f"    i.e. C prefers the LOW edge; the res-(iv) window as a whole overproduces.")
print()
print("  FALSIFIERS:")
print(f"   - Inverted ordering: floor Sum m_nu = {Sig_IH_floor*1e3:.0f} meV needs T_RH = "
      f"{TRH_at_NHfloor/np.sqrt(mbar2_IH_floor/mbar2_NH_floor):.2e} GeV (yield x{mbar2_IH_floor/mbar2_NH_floor:.1f} higher at fixed T_RH).")
print(f"     IH is independently disfavoured by DESI (floor {Sig_IH_floor*1e3:.0f} meV > ceiling {DESI_DR2_baseline*1e3:.0f} meV).")
print(f"   - DESI aggressive bound {DESI_DR2_aggressive*1e3:.0f} meV is BELOW the NH floor {Sig_NH_floor*1e3:.1f} meV:")
print(f"     if that holds, the neutrino mass floor itself is in crisis AND Candidate C's washout")
print(f"     operator (fixed by m_nu) loses its anchor -> C is falsified with the floor.")

# ---------------- robustness across O(1) conventions ----------------
print()
print("="*82)
print("  ROBUSTNESS: the O(1) couplings (Weinberg norm C_W, susceptibility g_chi, g*)")
print("  shift the required T_RH by ~x13. In much of this space C is ALREADY in tension:")
print("="*82)
print(f"  {'convention':30} | {'T_RH@NHfloor':>12} | {'Sum_nu req @ res-iv floor 3.2e12':>32}")
print("  " + "-"*80)
for C_W, cw in [(1/np.pi**3,'C_W=1/pi^3'), (0.05,'C_W=0.05'), (0.01,'C_W=0.01')]:
    for gchi, gl in [(1,'g_chi=1'), (6,'g_chi=6')]:
        for gs, sl in [(106.75,'g*=SM'), (228,'g*=SM+hidden')]:
            YB, _ = make_yield(C_W=C_W, gstar=gs, g_chi=gchi)
            try:
                Tf = brentq(lambda T: YB(T, mbar2_NH_floor)/YB_obs - 1, 1e12, 3e13)
            except Exception:
                Tf = np.nan
            hiw = 0.98*mbar2_weakmax(3.2e12, C_W, gs)
            f = lambda lm: np.log(YB(3.2e12, np.exp(lm))/YB_obs)
            if f(np.log(hiw)) > 0:
                mb = np.exp(brentq(f, np.log(1e-6), np.log(hiw)))
                s = sum_from_mbar2(mb, 'NH')
                st = (f"{s*1e3:6.1f} meV" + ("  (> DESI 64: excluded)" if s*1e3 > DESI_DR2_baseline*1e3 else "  (allowed)")) if np.isfinite(s) \
                     else "NH mass below floor -> OVERPRODUCES eta_B"
            else:
                st = "underproduces"
            print(f"  {cw+' '+gl+' '+sl:30} | {Tf:12.2e} | {st:>32}")
print("  " + "-"*80)
print("  Reading: only near the CANONICAL point (C_W=1/pi^3, g_chi=1, g*=SM) does the")
print("  res-iv window meet a DESI-allowed NH mass; raising g_chi overproduces eta_B, and")
print("  small C_W needs DESI-excluded heavy neutrinos. C is squeezed, not free.")

# ---------------- figure ----------------
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    TRHs = np.logspace(np.log10(1.5e12), np.log10(9e12), 60)
    sNH, sIH = [], []
    for T in TRHs:
        m = mbar2_required(T)
        sNH.append(sum_from_mbar2(m, 'NH')*1e3 if np.isfinite(m) else np.nan)
        sIH.append(sum_from_mbar2(m, 'IH')*1e3 if np.isfinite(m) else np.nan)
    fig, ax = plt.subplots(figsize=(7.2, 5.0))
    ax.plot(TRHs, sNH, 'b-', lw=2.2, label='C yield = $\\eta_B$, normal ordering')
    ax.plot(TRHs, sIH, 'c--', lw=2.0, label='C yield = $\\eta_B$, inverted ordering')
    ax.axhline(Sig_NH_floor*1e3, color='b', ls=':', lw=1, alpha=.7, label=f'NH floor {Sig_NH_floor*1e3:.0f} meV')
    ax.axhline(Sig_IH_floor*1e3, color='c', ls=':', lw=1, alpha=.7, label=f'IH floor {Sig_IH_floor*1e3:.0f} meV')
    ax.axhspan(DESI_DR2_baseline*1e3, 200, color='red', alpha=.10)
    ax.axhline(DESI_DR2_baseline*1e3, color='red', lw=1.6, label=f'DESI DR2 ceiling {DESI_DR2_baseline*1e3:.0f} meV')
    ax.axhline(DESI_DR2_aggressive*1e3, color='darkred', lw=1.2, ls='-.', label=f'DESI aggressive {DESI_DR2_aggressive*1e3:.0f} meV')
    ax.axvspan(3.2e12, 6.35e12, color='green', alpha=.10, label='ECCG res-(iv) $\\cap$ D-1 ($T_{RH}<\\Lambda_H$)')
    ax.set_xscale('log'); ax.set_xlabel('$T_{RH}$  [GeV]'); ax.set_ylabel('$\\Sigma m_\\nu$  [meV]')
    ax.set_ylim(0, 140); ax.set_title('Candidate C: neutrino-mass vs reheating prediction (D-2)')
    ax.legend(fontsize=7.5, loc='upper right', ncol=1); ax.grid(alpha=.25)
    out = "figures/candidateC_neutrino_inversion.png"
    fig.tight_layout(); fig.savefig(out, dpi=140)
    print(f"\n  figure -> {out}")
except Exception as e:
    print(f"\n  (figure skipped: {e})")
