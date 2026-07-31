# Conventions and corrections (single source of truth)

Consolidates the convention fixes and numerical corrections found during the
development pass. Non-destructive: the checksummed registry and reports are left
intact; this file records what should be adopted going forward.

---

## 1. Charge convention (RESOLVE the contradiction)

Two documents disagree on the U(1)_Q charges of the condensates:

- `docs/02_THEORY_OVERVIEW.md`:  q(Phi_V) = +1, q(Phi_D) = -1.
- `UV_PORTAL_AND_ABUNDANCE_REPORT.md`:  q(Phi_V) = -2, q(Phi_D) = +2.

These differ by both a sign and a normalisation. P = Phi_V Phi_D is neutral
either way, but the physical sign of the baryon asymmetry and the dark charge
ratio r_X_BL depend on the choice, so a single convention is mandatory.

**ADOPT (matches the portal report, which fixes the transfer operators):**

    q(Phi_V) = -2,   q(Phi_D) = +2,   q(L) = -1,   q(H) = 0,   q(X) = +1.

Then the portals L_V = (c_V/Lambda_V^2) Phi_V^dag (LH)^2 and
L_D = (y_X/2) Phi_D^dag XX are both exactly neutral, and P = Phi_V Phi_D has
q = 0. The overview's +1/-1 is the *abstract* U(1)_G normalisation of the
first-principles derivation; when combining with the transfer sector, rescale to
the -2/+2 physical assignment. State this once, in the master equations.

## 2. Notation unification

- **Third-harmonic coefficient:** the overview writes J_CP = Im(kappa_2^3 c_3^*2)
  while the first-principles doc writes Im(kappa_2^3 kappa_3^*2). `c_3` and
  `kappa_3` are the SAME coupling at different dressing stages
  (c_3 = kappa_3/M^2 in the registry). Use **kappa_3** for the dimensionless
  harmonic coupling and **c_3 = kappa_3/M^2** for the dimensionful one; write the
  CP invariant as J_CP = Im(kappa_2^3 kappa_3^*2).
- **Dark mass:** the executive summary quotes m_X ~ 1.3 GeV; the portal report
  computes 1.78 GeV. The difference is the flavored charge ratio r_X_BL:
  m_X = (Omega_X/Omega_b) m_p (28/79)/r_X_BL, giving 1.78 GeV at r_X_BL = 1 and
  ~1.3 GeV with the flavored correction. Always quote m_X **with** the r_X_BL
  used.
- **Planck mass:** as the master-equations doc already warns, older scripts mix
  M_Pl (1.221e19) and the reduced M_Pl (2.435e18). The reduced value is used in
  the Friedmann law here; check each script.

## 3. beta/H correction (supersedes the registry value)

The registry lists `beta_over_H = 347.047799` (6 significant figures). The
robustness study (`numerical_robustness/`) shows this is **false precision**: the
bounce solver returns spurious actions ~27% of the time and the shipped n=11
pointwise PCHIP derivative is unstable (values 224/347/360/818 depending on grid
and scipy version). After outlier rejection and a smooth fit:

    beta/H = 3.9(4) x 10^2   (central ~374-414, ~20% numerical systematic).

**ADOPT:** quote beta/H = 3.9(8) x 10^2 (numerical band only; the one-loop
gauge-fixed theory systematic is larger and separate). Propagate this band to
percolation, the delta_Tn/Tn bound, and the GW frequency. No structural
conclusion changes (still strongly first-order, beta/H >> 1).

## 4. Recommended registry edits (for the next version)

| parameter | old | new |
|---|---|---|
| beta_over_H | 347.047799 | 3.9(8)e2 (with band) |
| m_X_asymmetric | 1.3 (unqualified) | 1.3 (r_X_BL flavored) / 1.78 (r_X_BL=1) |
| (charge convention) | inconsistent | q(Phi_V,Phi_D) = (-2,+2) everywhere |

These are documentation/precision fixes; none changes the mechanism or the
existence of the benchmark.
