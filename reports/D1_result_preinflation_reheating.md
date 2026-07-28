# D-1 executed — the pre-inflation cure survives reheating (G-M1 does not fire)

**Script:** `unified/sims/preinflation_reheat_domain_check.py` (reproduces from `unified/`).
**Grounded in:** ECCG `SPONTANEOUS_CP_REPORT.md`, `MICROSCOPIC_SQCD_THERMAL_REPORT.md`,
`PREINFLATION_REPORT.md`.

## The worry (Critique gap G-M1, CRITICAL)
The domain cure pins ψ to one ℤ₂ vacuum via `V₂ = −Λ₂⁴cos(2ψ+δ₂)`, active during inflation with `m₂≫H_inf`.
I raised: if `T_RH > Λ_H = 6.35×10¹²` GeV, the hidden `SU(3)_H` deconfines, `Λ₂⁴ ∝ κ₂ ∝ ⟨Θ⟩` melts, ψ is
released, and reconfinement **Kibble-regenerates the matter/antimatter domains** → `η ≈ 0` again. Since the
res-(iv) window `T_RH∈[3.2, 9]×10¹²` GeV has its upper half above `Λ_H`, this looked like it could collapse
the entire ECCG-res-(iv) dawn.

## The resolution — it does not fire, for three model-grounded reasons

1. **The sign lives in the PHASE, and the phase is flavon-set, not hidden-sector-set.** The domain-selecting
   quantity is which ℤ₂ minimum ψ occupies, fixed by the CP phase `δ₂ = n₂θ_S` — set by the **flavon** `θ_S` at
   scale `v_S`, *not* by `SU(3)_H` (SPONTANEOUS_CP §1: "`δ₂ = n₂θ_S, δ₃ = n₃θ_S`"). The model already inflates
   the flavon to uniformity and requires **`T_RH < v_S`** (SPONTANEOUS_CP §4a: "inflation is the only
   resolution… `T_RH < T_S ~ v_S`… an inflated flavon phase is uniform").
2. **`SU(3)_H` reconfines REAL, adding no phase.** The quantum-modified moduli constraint with positive soft
   masses selects the diagonal branch `|M_ii| = Λ_H²`, so `arg⟨Θ⟩ = 0` (MICROSCOPIC_SQCD). Any `T_RH > Λ_H`
   melt/reform of the *magnitude* `Λ₂` therefore re-pins ψ with the **same uniform phase structure** — magnitude
   domains in `⟨Θ⟩` don't flip the sign.
3. **The released phase can't random-walk into domains.** Even at the window top `T_RH = 9×10¹²`, the hidden
   sector is deconfined for only **0.35 e-folds**, and the released ψ fluctuates by
   `δψ ~ H/(2πf_ψ) = 2.6×10⁻⁶` rad — **6 orders below the `π/2` ridge** between the vacua. Radiation-era
   evolution generates no new super-horizon (domain-scale) modes. No flips.

Numerically (`preinflation_reheat_domain_check.py`):

| test | result |
|---|---|
| `T_RH < v_S` (flavon never restored) | branch B: `v_S/T_RH,max = 2.7×` ✓; branch A: `533×` ✓ |
| hidden deconfinement duration (top of window) | **0.35 e-folds** |
| released-phase excursion vs the vacuum ridge | `δψ/(π/2) = 1.6×10⁻⁶` ✓ (no flips) |

## Verdict
**G-M1 is resolved — downgraded from CRITICAL to a satisfied consistency condition.** The relevant reheating
threshold is **`v_S`, not `Λ_H`**; the res-(iv) window sits safely below `v_S` for both flavon branches.

## Two consequences

1. **D-2's window label is corrected (conclusion unchanged).** D-2 used `[3.2, 6.35]×10¹²` with the upper edge
   = `Λ_H` as a supposed D-1 bound. The correct upper edge is the **portal-thermal-restoration `9×10¹²`**, with
   `T_RH < v_S` the (comfortably satisfied) D-1 condition. Since D-2 already found that everything above
   `~3.3×10¹²` overproduces `η_B`, widening the window to `9×10¹²` adds only more overproducing space — **the
   razor-thin viable sliver at `T_RH ≈ 3.3×10¹²`, `Σm_ν ≈ 59–64 meV`, NO is unchanged.**

2. **A NEW independent falsifier surfaced.** The cure is safe but *not free* — it forces `T_RH < v_S`, and
   **branch B** (`v_S = 2.44×10¹³`, the economical single-flavon option) sits at the **neutron-EDM edge**:
   `θ̄ ~ (v_S/M_Pl)² sin Δ_CP ~ 4×10⁻¹² × O(1)` — a neutron EDM near the current experimental bound. Branch A
   (`v_S = 4.8×10¹⁵`) evades nEDM but needs a second gauged flavon. So the ECCG-res-(iv) dawn carries an
   **nEDM prediction independent of DESI/CMB** — a third leg (with E-2/neutrinos and E-5/tensors) of the dawn's
   over-determination.

## Net effect on the two-horn theorem
The dawn's two horns stand: **ECCG-res-(iv)** (m_X=1.78 sharp, `r≤2×10⁻¹¹`) is internally consistent through
reheating (D-1 ✓), and its independent handles are now **(i)** `r≈0` (tensors), **(ii)** a branch-B neutron EDM
at `~10⁻²⁷` e·cm scale, and — via the *other* horn — **Candidate C's** DESI-edge neutrino prediction (D-2).
The union did not lose a horn; it gained a cross-check.
