> ⚠️ **CORRECTION (assumed-vs-calculated audit — `ECCG-SEDE/new-research/AUDIT_round2_sweep.md`).** **`v_w=0.58`** is an **LO ballistic** friction
> ansatz (free-streaming 1→1), **not a full Boltzmann transport solve** (flagged Open); the `±0.09` is an
> *assumed* ×0.7–1.5 NLO envelope, not a computed NLO. The exclusion of `v_w=0.3` is robust only within the
> ballistic LO model.

# Precise wall velocity: LTE hydrodynamics + Bodeker-Moore friction balance

**Status:** v_w upgraded from an order-of-magnitude bracket (0.24-0.48) to a
computed leading-order value **v_w = 0.58 +/- 0.09** (near-sonic
deflagration/hybrid). The benchmark input **v_w = 0.30 is EXCLUDED** at LO:
at v = 0.3 the friction balances only ~1/3 of the driving pressure.
**Module:** `wall_velocity_precise.py` (runs under the repo venv). Outputs:
`wall_velocity_precise_summary.csv`, `lte_scan.csv`,
`ballistic_friction_curve.csv`, `runaway_thresholds.csv`,
`wall_velocity_precise.png`. All numbers below are computed by the module on
the gauge-invariant 3D-EFT transition (mu = 2 pi T benchmark).

---

## 1. Equation of state: what "alpha = 0.055" is and is not

The DR report's alpha is the **energy-density** difference,
alpha_DR = Delta e/rho_rad, computed from epsilon = DeltaV - T dDeltaV/dT.
The bag constant that enters the hydrodynamic junction conditions is the
**trace anomaly**, (Delta e - 3 Delta p)/4. Reusing 0.055 directly in bag
formulas double-counts the dof change (factor ~2). From the EFT3D potential
at T_n (model-exact, not a bag ansatz):

    DeltaV(T_n)/T_n^4 = 0.6425          (driving pressure; alpha_driving = 0.0183)
    Delta e/rho_rad   = 0.0552          (reproduces the DR alpha exactly)
    alpha_hydro       = 0.0275          (trace anomaly / rho_rad; the "bag" alpha)
    Psi_n = w_-/w_+   = 0.9723          (Delta N_eff = 2.96 dof)
    bag-consistency:  T_c/T_n(bag) = 1.31 vs actual 1.39  (-5.7%: the true
                      DeltaV(T) is not exactly bag; residual EoS systematic)

Delta N_eff = 2.96 is exactly the massive U(1) vector triplet (3 dof at
m_A/T_n = 3.77, Boltzmann-removed behind the wall) - an independent
consistency check of the spectrum used for the friction.

Spectrum crossing the wall (3D-EFT broken-phase masses at T_n):
A_mu (boson, 3 dof, Dm/T = 3.77), h (boson, 1 dof, 1.26),
X (Dirac fermion, 4 dof, 0.93).

## 2. Bodeker-Moore runaway check at the new alpha

LO (1->1) friction saturates at P_BM = sum c_i N_i Dm_i^2 T^2/24 (c = 1
boson, 1/2 fermion). The exact kinetic runaway criterion, which my ballistic
construction reproduces as its v -> 1 limit, is

    runaway  <=>  DeltaV(T_n)  >  P_BM - Delta p_th ,

(the static thermal-pressure difference Delta p_th must be subtracted: it is
already inside DeltaV). Computed:

    P_BM = 1.910 T^4,  Delta p_th = 0.370 T^4,  max net friction = 1.540 T^4
    driving DeltaV(T_n) = 0.642 T^4   =>  NO RUNAWAY, margin x2.40

Threshold in generic dof gaining Dm = g_q phi_n (`runaway_thresholds.csv`):

| convention | N_crit (dof at Dm=3.77T) | note |
|---|---:|---|
| EKNS alpha-language (alpha_DR = 0.0552 vs alpha_inf = N x 0.0168) | 3.28 | was 2.1 at alpha = 0.036: alpha's +55% did move the naive threshold up |
| exact kinetic (DeltaV vs P_BM - Dp_th) | 1.29 | the honest criterion |

The vector triplet alone (3 dof) clears the exact threshold; the EKNS-language
threshold of 3.28 is an artifact of using the Delta-e alpha with the
un-subtracted P_BM. **Verdict: non-runaway, robustly** - the margin is x2.4
with the actual spectrum, and even a x0.7 friction (NLO down-fluctuation)
leaves x1.7.

## 3. Method 2: LTE hydrodynamics - and why it has NO steady solution

Bag junctions + entropy conservation across the wall (gamma_+ T_+ =
gamma_- T_-; Ai-Garbrecht-Tamarit / Ai-Laurent-van de Vis) give the wall
condition h(v_+) = Psi h(v_-), h(v) = v(1-v^2), closed by the full
deflagration shock profile (similarity ODE + shock matching, solved
numerically; `lte_scan.csv`). Result for (alpha_n = 0.0275, Psi = 0.9723):

- **Deflagrations/hybrids:** the wall condition linearizes to
  alpha_+ = (1-Psi)/3, i.e. it demands preheating to
  T_+/T_n = (3 alpha_n/(1-Psi))^{1/4} = 1.31 ~ T_c/T_n. Shock preheating is
  only O(alpha). The obstruction parameter 3 alpha_n/(1-Psi) = **2.98 > 1**:
  the residual is +0.15..+0.39 at every xi_w - **no solution**.
- **Detonations:** entropy production sigma > 0 for every xi_w > v_J = 0.696
  (LTE residual +0.001..+0.020) - detonations *require* dissipation.

**Conclusion (structural):** the dof jump (Psi -> 1) is too small for this
alpha; hydrodynamic obstruction cannot stop the wall. A friction-free wall
accelerates without bound; the terminal velocity is set entirely by the
kinetic friction. LTE's surviving role is to fix the front hydro state
(T_+, v_+) used in Method 1.

## 4. Method 1: ballistic (BM) friction + hydrodynamic force balance

Exact finite-velocity 1->1 momentum transfer with boosted equilibrium fluxes
(1D-reduced integrals):

    P_front = (1/4pi^2 gamma) Int dp p Dp(p) L(gamma p(1-v)),
       Dp = 2p (p<Dm, reflection),  p - sqrt(p^2-Dm^2) (transmission)
    P_back  = (1/4pi^2 gamma) Int dk k (sqrt(k^2+Dm^2)-k) L(gamma(E+vk))
       (back-crossers LOSE mass, gain |p_z|, and also brake the wall)
    L_BE = -ln(1-e^-x),  L_FD = ln(1+e^-x)

Validation (computed): v->0 limit 0.3704 vs Delta p_th = 0.3703; v->1 limit
1.9115 vs P_BM = 1.9102. The wall is thin against the mean free path
(L_wall ~ few/T << l_mfp ~ 10-100/T), so free-streaming across the wall is
the correct LO kinetic treatment, not merely a bound.

Steady state: for xi_w < v_J the (non-LTE) deflagration hydro is closed by
junctions + shock matching, fixing the preheated inflow (T_+, v_+); balance

    DeltaV(T_+)  =  T_+^4 DeltaP_bal(v_+; m_i/T_+) .

The balance curve F(xi_w) is smooth and monotonically decreasing (stable
root); F < 0 on the whole detonation branch (no detonation solution):

    bare ballistic (T_n inflow)            v_w = 0.617
    hydro-consistent balance               v_w = 0.577   <- central
      (at the solution: T_+/T_n = 1.096, v_+ = 0.454)
    friction x1.5 / x0.7 (LO->NLO proxy)   v_w = 0.473 / 0.644
    minimal spectrum (vector only)         v_w = 0.588

At v = 0.3 the friction+heating balances only 36% of the driving
(F(0.3) = +0.41 T^4); stalling there would need the LO friction to be wrong
by ~x2.7. **v_w = 0.3 does not survive.**

## 5. Combined result

    v_w = 0.58 +/- 0.09      (range 0.47 - 0.64)
    regime: deflagration/hybrid at the sonic edge (v_w ~ c_s; v_J = 0.696)

The error is dominated by the LO->NLO friction normalization (x0.7-1.5
envelope covering 1->2 transition radiation at gamma ~ 1.2, symmetric-phase
thermal masses, and the back-side flux model), with the spectrum variation
(+/-0.01) and the EoS/bag-mapping residual (-5.7% bag check, ~+/-0.02 on
v_w) subdominant. The two methods "agree" in the strong sense available:
LTE proves no hydrodynamic stalling below c_s and no entropy-consistent
detonation, and the friction balance lands in the only window left open,
just below the Jouguet velocity. The previous LTE-style guess
c_s sqrt(alpha/alpha_inf) = 0.24-0.48 overlaps this band only at its top
edge; its central value 0.3 is excluded.

## 6. eta_B propagation (eta_B ~ 1/v_w^2)

At the benchmark (FITTED) m3/H = 1.843:

    eta_B central:  3.8e-10  ->  1.03e-10   (x (0.3/0.577)^2 = x0.27)
    v_w-band alone: [0.83, 1.53] x 1e-10    (factor x1.9; was x4.0)
    total quadrature band:  x3.9            (was x6.3, the "~x7 residual")

Since m3/H is the fitted parameter (required m3/H ~ sqrt(v_w) at fixed
eta_B, verified in `global_scan.py`), the physical statement is: holding
eta_B at the observed 6.1e-10 **raises the required m3/H by x1.39**
(1.843 -> 2.56); the *prediction band*, which is the deliverable, shrinks
because the dominant 1/v_w^2 lever collapses from a factor-4 to a factor-1.9
contribution. The residual band is now dominated by the flavor bracket
(x2.5) and sin(Delta_CP) (x1.7), as anticipated by the error budget - v_w
is no longer the #1 lever.

## 7. Truth-status summary

- **Exact/structural:** the kinetic runaway criterion DeltaV(T_n) vs
  P_BM - Dp_th and its verdict (non-runaway, margin x2.4); the v->0/v->1
  limits of the ballistic pressure (validated to 0.03%/0.07%); NO steady
  LTE wall for (alpha_hydro, Psi) = (0.0275, 0.9723) - obstruction parameter
  3 alpha/(1-Psi) = 2.98 > 1; entropy production > 0 on the whole detonation
  branch; the alpha_DR (Delta e) vs alpha_hydro (trace anomaly) distinction.
- **Derived (benchmark numbers):** alpha_hydro = 0.0275, Psi_n = 0.9723,
  DeltaV(T_n)/T_n^4 = 0.642 from the EFT3D potential; v_J = 0.696;
  v_w = 0.577 central; N_crit = 1.29 dof (exact) / 3.28 (EKNS convention);
  Delta N_eff = 2.96 dof = the vector triplet (spectrum consistency).
- **Model assumption:** boosted-equilibrium incoming fluxes and
  equilibrium back-side flux in the ballistic integrals; bag-form similarity
  profile for the front hydro (bag check off by 5.7%); the wall spectrum
  (A, h, X with 3D-EFT masses); g* = 106.75.
- **Open precision problems:** (i) NLO friction - 1->2 transition
  radiation/LPM at gamma ~ 1.2 (bracketed here by x0.7-1.5, the dominant
  error); (ii) symmetric-phase thermal masses in Dm^2 (few-% level);
  (iii) a Boltzmann/WallGo-style transport solve to replace the ballistic
  wall-frame fluxes; (iv) non-bag EoS in the fluid profile (5.7% bag
  residual); (v) the LTE entropy-condition analysis at two-loop EoS accuracy.
