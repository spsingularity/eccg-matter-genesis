# ECCG: consolidated minimal theory (post-reduction)

A single coherent statement of the theory after the development pass: the
mechanism, the reduced parameter set, the completion, the predictions, and the
honest status. Every quantitative claim is backed by a runnable module under
`development/` (see the pointers). This is the object a first paper should
present.

---

## 1. Mechanism (one paragraph)

Two complex condensates Phi_V, Phi_D carry opposite charge under an EXACT
generalized symmetry U(1)_Q. Their neutral product P = Phi_V Phi_D feeds a
CP-sensitive two-harmonic phase potential V_psi = -A_2 cos(2psi+delta_2)
- A_3 cos(3psi+delta_3), psi = theta_V + theta_D. A first-order transition in a
hidden confining SUSY sector (order parameter Sigma = the hidden meson/modulus)
turns on the third harmonic across the bubble wall, delivering a CP-odd
counter-rotating impulse that generates EQUAL AND OPPOSITE visible (B-L) and dark
(X) charges (d/dt[a^3(n_V-n_D)] = 0 exactly). Sphalerons convert the visible part
to baryons; the dark part is asymmetric dark matter.

## 2. The reduced parameter set

The cosmology depends on a **9-parameter EFT**
theta_EFT = {T_n, beta/H, alpha, v_w, m3/H, m1/H, f_psi/T_n, f_B, r_X_BL}
[eccg_parameters.py], but these are NOT independent. Tracing them to their roots
(derive_transition_sector.py, derive_m3_from_FN.py, derive_transition_couplings.py,
wall_velocity_estimate.py):

| EFT quantity | reduces to |
|---|---|
| T_n | the scale Lambda_H ~ 2 T_n, via hidden transmutation (g_H) |
| beta/H, alpha, v_w, phi_true/T | 2 transition couplings {g_q, lambda_s} (SVD dim = 2) |
| g_q | O(1) composite coupling at Lambda_H (g_H's Landau pole IS Lambda_H) |
| lambda_s | (F_Z/Lambda_H^2)^2 O(1) ~ 0.03: a SUSY-lifted MODULI quartic |
| m3/H | FN coefficient eta_3 = 0.36 (natural O(1)) |
| m2/H | FN coefficient eta_2 = 9.85 |
| m1/H | a BOUND (< 0.3), set by the protection, not a dial |
| f_psi/T_n | O(1) ratio (~3), condensate near the transition scale |
| f_B | derived by the flavour transport (neutrino data + portals) |
| r_X_BL | = 1 (Exact/structural: equal-and-opposite charges) |

**Final irreducible continuous freedom:**

    { g_H(M) -> scale,  F_Z -> SUSY scale,  eta_2, eta_3 (O(1) FN),  Delta_CP }
    = two scales + two O(1) coefficients + one phase,

all up to the known O(1) strong-sector normalizations. Down from 27 microscopic
inputs.

## 3. Viability (go/no-go): PASSED

`global_scan.py`: eta_B is a product of O(1) powers, so the Barbieri-Giudice
tuning is **exactly 2** (no fine-tuned cancellation). The viable region is
**connected** and O(1)-sized (86% of prior volume gives natural m3/H); the
benchmark is a typical interior point. The Critical "highly tuned benchmark" risk
is cleared.

## 4. The completion: 4D S_3, viable

The dangerous first harmonic (Abelian Kahler no-go) is removed by a 4D **S_3**
discrete symmetry with P in the 2-dim irrep [collective_breaking.py]: it forbids
bare P and the cross-Kahler X_2^dag X_3 P (verified by singlet counting) while
allowing P^2, P^3, replacing ~14 warped inputs with ~4. Hardening
[s3_cp_invariant.py, s3_thermal_sequestering.py]:
- **CP survives** the S_3 contraction (d Delta_CP/d arg kappa_2 = +3,
  d/d arg kappa_3 = -2 exactly; no first harmonic generated);
- **4D thermal sequestering is buildable** with a chirality-protected messenger
  at 2e16-4e17 GeV, meeting the condensate-survival requirement.
The warped construction remains as an alternative completion.

## 5. Closed consistency requirements

- **Condensate thermal survival** [thermal_survival.py]: the naive setup fails by
  2.3e8 (portal thermal mass), but the sequestering (warped OR S_3 messenger)
  closes it -- the sequestering sector does triple duty (Kahler + thermal +
  cold-dark), zero new parameters.
- **Domain walls** [domain_wall_history.py]: SAFE, 6.3x margin; A_3 bias collapses
  them before domination; controlled by A_3/A_2.
- **Symmetric dark component** [symmetric_depletion.py]: depleted by a light
  p-wave dark scalar (y_s ~ 0.05-0.08), which auto-evades CMB injection.
- **Wall velocity** [wall_velocity_estimate.py]: subsonic deflagration
  (non-runaway); v_w ~ 0.24-0.48 brackets the input 0.3.
- **beta/H** [beta_over_H_robustness.py]: solver bug fixed (27% spurious actions);
  beta/H = 3.9(4)e2 (~20% syst), replacing the false-precision 347.05.

## 6. Predictions

- **Flagship: m_X ~ 1.78 GeV** asymmetric dark matter, **independent of the
  eta_B fit** (constant across Delta_CP). The full momentum-resolved transport
  [momentum_resolved_transport.py] shows m_X is set by SPHALERON TIMING (not
  washout), m_X = 1.782 f_sph(T_dec); a renormalizable Phi_V->NN->lH mediator
  [renormalizable_mediator.py] drives the decay well above sphaleron freeze-out
  in 89% of its viable window, so **m_X -> 1.78 GeV** generically (the light
  1.33 GeV value is a near-threshold tuning). Same portal fixes m_nu (inverse
  seesaw). Falsifiable by GeV-scale direct detection; the mediator N and the
  dark scalar (m_s >~ 10 MeV) are further targets; self-interaction testable.
- **Internal:** reversing Delta_CP reverses both asymmetries; Delta_CP = 0 kills
  them.
- **Gravitational waves:** high-frequency (~1e7-1e8 Hz), currently unobservable.

## 7. Honest status

- **Established (Exact/structural or Derived):** exact charge conservation; the
  27->9->~5 reduction; BG tuning = 2; connected viable region; m3/H natural;
  transition couplings SQCD-fixed; S_3 selection rules + CP survival; the closed
  consistency requirements; the m_X prediction.
- **Model assumption:** O(1) strong-sector normalizations of (g_q, lambda_s); the
  FN coefficients eta_2, eta_3; f_psi/T_n; the dark-sector constraint estimates.
- **Open precision problems (correctly deferred):** predicting eta_2, eta_3,
  Delta_CP from a hidden-flavour theory; gauge-invariant dimensional reduction of
  the transition; momentum-resolved transport (which fixes r_X_BL -> narrows m_X);
  a full per-point pipeline scan; the nonperturbative (g_q, lambda_s).

## 8. Recommended paper structure

1. **Paper I (minimal EFT):** the mechanism (section 1), the reduced parameter
   set (section 2), the go/no-go (section 3), and the m_X prediction (section 6),
   with the closed consistency requirements (section 5) as support. Position vs
   Affleck-Dine cogenesis (LITERATURE_POSITIONING.md).
2. **Paper II (completion):** the 4D S_3 construction and its hardening
   (section 4), with the warped model as the technical alternative.

## 9. Module / report index

- Parameter reduction & derivation: `parameter_reduction/` (eccg_parameters,
  global_scan, derive_transition_sector, derive_m3_from_FN,
  derive_transition_couplings; 5 reports).
- Completion: `collective_breaking/` (collective_breaking, s3_cp_invariant,
  s3_thermal_sequestering; 2 reports).
- Consistency: `condensate_survival/`, `dark_completion/`, `wall_dynamics/`,
  `numerical_robustness/` (5 reports).
- Prediction: `phenomenology/` (predict_dark_matter; 1 report).
- Cross-cutting: `docs/` (DEVELOPMENT_SUMMARY, CONVENTIONS_AND_CORRECTIONS,
  LITERATURE_POSITIONING, this file).
