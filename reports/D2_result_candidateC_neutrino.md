# D-2 executed — Candidate C is squeezed to a DESI-edge neutrino prediction

**Script:** `unified/sims/candidateC_neutrino_inversion.py` · **Figure:**
`unified/figures/candidateC_neutrino_inversion.png` · reproduces from `unified/`.

## What D-2 does that the corpus didn't
`candidateC_yield.py` validates the mechanism (Boltzmann `Y_B/obs = 0.92` at the NH mass floor,
`T_RH = 3.17×10¹²` GeV) but stops at a *comment* — `[EXCLUDED by Σm_ν<0.07-0.12 eV]`. D-2 turns Candidate C
into an actual **`Σm_ν(T_RH)` contour** and confronts the **current DESI posterior**, with three fixes:

1. **Real ΔL=2 washout Boltzmann** for `Y_B(T_RH, m̄²)` instead of the `½Γ/H·Y_eq` weak-washout analytic
   (which overshoots 13–31% in-window). Calibrated: my `Y_B(3.17×10¹², NH-floor) = 7.98×10⁻¹¹` = the shipped
   script's number.
2. **The washout mass is `m̄² = Σmᵢ²` (sum of *squares*), cosmology bounds `Σmᵢ` (sum).** These are different
   observables; D-2 maps between them via the lightest-mass parametrization for NH and IH. This matters: near
   the floor `m̄²` is dominated by the *fixed* atmospheric splitting, so the yield is nearly `Σmᵢ`-independent.
3. **Yield is non-monotonic in `m̄²`** (weak branch `∝m̄²`, strong branch `∝Y_eq(T_d)` falling); the inversion is
   restricted to the physical weak-washout branch.

## Result (canonical couplings `C_W=1/π³, g_χ=1, g*=SM`)

`η_B = 6.10×10⁻¹⁰` fixes the line `η_B ∝ T_RH² · Σmᵢ²`. Intersecting it with the neutrino floors, the
DESI ceiling, and ECCG's res-(iv) reheating window `T_RH∈[3.2, 6.35]×10¹²` GeV (upper edge = `Λ_H`, the D-1
confinement bound) gives a **razor-thin allowed region:**

> **`T_RH ≈ 3.28–3.31×10¹²` GeV, `Σm_ν ≈ 59–64 meV`, NORMAL ORDERING** (width in `T_RH`: factor 1.01).

- The NH mass **floor** (58.6 meV) is matched at `T_RH = 3.31×10¹²`; the **DESI DR2 baseline ceiling**
  (64 meV) is hit at `T_RH = 3.28×10¹²`. The entire viable band is `≤ 6 meV` wide and sits **exactly at the
  current DESI cut.**
- The rest of the res-(iv) window (`T_RH ≳ 3.6×10¹²`) needs `Σmᵢ² <` the NH floor → **impossible for any real
  neutrino spectrum → overproduces `η_B`** (this is the "107% → 850%" the corpus flagged in
  `candidateC_yield.py` §4, now identified as a *neutrino-mass* exclusion, not a mild rider).

## The two sharp falsifiers

1. **Inverted ordering is excluded.** IH floor `Σm_ν = 99 meV` needs `T_RH = 2.4×10¹²` GeV (below the res-(iv)
   window) and lies far above the DESI ceiling. So Candidate C **requires normal ordering** — and DESI DR2 +
   oscillation data already disfavour IH. A confirmed IH kills it.
2. **DESI's aggressive bound is already below the NH floor.** The DESI DR2 + DESY5 combination gives
   `Σm_ν < 46 meV`, *below* the NH oscillation floor of 58.6 meV — the well-known emerging "neutrino mass
   anomaly." If that holds, the Weinberg operator (whose coefficient *is* the neutrino mass) loses its anchor
   and **Candidate C is falsified together with the mass floor itself.**

## Honest caveats (this is a squeeze, not a parameter-free prediction)

- **O(1)-coupling systematic ≈ ×13 in `T_RH`.** The susceptibility `g_χ`, Weinberg normalization `C_W`, and
  `g*` are not pinned. The robustness scan (in-script) shows that across this space **almost every point is
  already in tension**: raising `g_χ` → overproduces `η_B`; lowering `C_W` → needs DESI-excluded heavy
  neutrinos (100–250 meV). Only the *canonical* point threads the res-(iv) window and a DESI-allowed NH mass.
  So the robust statement is **not** "C predicts `Σm_ν = 60 meV"; it is **"C's viable region is squeezed to
  NO + `Σm_ν` at its floor + `T_RH` at the bottom of the res-(iv) window, right where DESI is cutting."**
- **DESI numbers are representative** (baseline 64 meV, aggressive 46 meV, from knowledge to Jan 2026); the
  live value should be refreshed before quoting. The *structure* of the result (floor vs ceiling squeeze) is
  robust to the exact ceiling.
- This tests the **C∥ECCG hybrid** (T_RH tied to the res-(iv) window) — the union's "generic endpoint." **Pure
  Candidate C with free `T_RH`** does not bound `Σm_ν` (it just co-determines the pair on the line); there the
  prediction is only "NO + a point on the `η_B` contour," which becomes sharp only once `T_RH` is fixed by
  ECCG.

## Verdict against the D-2 success criterion
> *"predicts NO + Σm_ν near floor; if excluded, C is dead."* — **Confirmed, and sharper than anticipated:**
Candidate C (hybridized with ECCG) is driven to **normal ordering + `Σm_ν` within a few meV of its floor +
`T_RH ≈ 3.3×10¹²` GeV**, a region DESI is *actively closing*. It is **not yet excluded** (canonical couplings
survive in a razor-thin sliver at the current DESI baseline), but it is **one DESI DR2/DR3 tightening — or an
IH confirmation — from falsification**, by data unrelated to any of the three programs. This makes G-M2 the
union's most imminent make-or-break test alongside the RAR data-collapse (E-1).

## Follow-ups this exposes
- **Fold the actual DESI DR2 likelihood** (not a hard ceiling) and marginalize `g_χ, C_W, g*` with priors →
  a proper `p`-value for Candidate C now.
- **D-1 update (executed):** the reheating constraint is `T_RH < v_S` (≥2.4×10¹³ GeV), **not** `T_RH < Λ_H`
  as tentatively used above — so the correct window upper edge is the portal-thermal `9×10¹²`, wider than the
  `6.35×10¹²` label in the table. This **does not change the result**: D-2 already shows everything above
  `~3.3×10¹²` overproduces `η_B`, so the extra window space is all excluded, and the viable sliver at
  `T_RH ≈ 3.3×10¹²`, `Σm_ν ≈ 59–64 meV`, NO stands. (See `D1_result_preinflation_reheating.md`.)
- The `η_B ∝ T_RH²Σmᵢ²` line is the concrete realization of the corpus's *generalized single-source theorem*
  ("η_B-calculable XOR m_X-sharp"): here η_B is calculable **because** `Σmᵢ²` is measured — at the cost of
  `m_X` being a band. D-2 quantifies exactly how much room that leaves: almost none.
