# Closing the assumed-vs-calculated gaps — item by item

**What "closing" means here.** These items were *assumed* precisely because most cannot be cheaply
calculated. So closure takes one of three honest forms:
- **[CALCULATED]** — I did the computation; it's now derived.
- **[CORRECTED]** — it cannot be calculated to be what was claimed, so the honest closure is the corrected
  statement (propagated into the corpus). The gap is "closed" by making the claim true.
- **[OPEN]** — genuinely needs a paper-scale calculation, a lattice run, or external data; cannot be closed
  from a desk. I state it honestly and flag it; I do not pretend to close it.

Anyone who claims to have *calculated away* all of these would be committing the exact error this whole audit
is about. The honest result is 1 calculated, several corrected, and a residual that is irreducibly open.

---

## Thermal cluster

**T1. `ζ>0` = fluctuation–dissipation at `T_AH` (KMS).** → **[CORRECTED]** The bath is athermal (noise 10⁵⁷×
the thermal value, `D5_fdt_result.md`). Cannot be made thermal. Closure: `ζ>0` survives as the **second law**
(driven/NESS); the FDT-at-`T_AH` reading is retracted. **Propagated:** correction banners on the manuscript +
5 KMS-action docs + README (commit `e91eaf0`).

**T2. `c = 1/2π` "unit coupling per KMS period."** → **[CORRECTED + partially OPEN]** The *mean* geometric
`2π` (de Sitter Euclidean regularity / Gibbons–Hawking) is a background fact and survives. The *fluctuation*-
KMS reading dies with T1. The **exact O(1)** is not `1/2π` — the observed `a₀ = 1.16·cH₀/2π` shows a 16%
residual, so `c=1/2π` is a **16% match, not exact**. The exact coefficient is the **[OPEN]** D-4′ worldline
calculation. Closure: state "geometric `2π` for the mean (derived); exact O(1) open (D-4′); currently a 16%
match, not a derivation." Propagated via the T1 banners.

**T3. KMS-tilt inertia MOND (D-3′).** → **[CORRECTED]** Relies on a thermal bath a galaxy does not have
(`~3×10⁻²²` modes — APDM's own falsification). Cannot be a thermal-equilibrium effect. Closure: it survives
**only as a vacuum (Unruh-reaction) effect**, whose existence is the **[OPEN]** D-4′ covariant-action question.
Downgrade "the surviving MOND mechanism" → "a surviving vacuum *heuristic*, pending a covariant action."

## Non-thermal cluster

**N1. The K/braiding split `b` is "slaved to the background."** → **[CORRECTED]** Computed: same background,
different perturbations for `b=0.20` vs `0.30` (`μ_∞ = 1.05` vs `1.08`). `b` is a **free perturbative
parameter**. Closure: honest DE count `{μ, γ, Δ} + b` (b measurable at ~5σ by DR3+Euclid, so a prediction,
not a hidden fit). **Propagated:** R1 derivation + ledger corrected (commit `747c66f`).

**N2. "Accumulated structure activates dark energy."** → **[CORRECTED]** The gate is `A_s`-independent (depends
on the growth *ratio* `D²=σ8²(a)/σ8²(1)`, which cancels `A_s`). Closure: the narrative becomes "the gate tracks
the growth *shape*, not the structure *amount*" (Candidate-E's `A_s`–`γ` degeneracy). Correction recorded in
the audit; needs a one-line fix in `SEDE_cosmology.md`'s activation prose.

**N3. `γ ≈ 1.5` "derived from halo binding."** → **[CORRECTED — with a proven negative]** The fitted value
`1.4964` is from the gate/flatness normalization; the halo derivation is not merely absent, it is a **proven
negative** — the SEDE2 track showed *every* halo/merger→gate derivation fails (the inverse-source envelope
obstruction). So `γ` is irreducibly a **prescription/fit**. Closure: state it as such and cite the negative;
promote `γ` to a fitted parameter (`{μ, γ, Δ} + b`, γ fitted) rather than "derived."

**N4. `f_B = 28/79`.** → **[CALCULATED — genuinely closed]** It is the SM sphaleron `B−L→B` factor
(Harvey–Turner: `(8N_g+4N_H)/(22N_g+13N_H) = 28/79`), and it is **valid for ECCG** because the dark sector is
(a) SM-gauge-singlet (no `SU(2)_L` isospin → sphaleron-inert) and (b) chemically decoupled at the EW scale
(`Γ_mix/H = ε²αT/H = 7.5×10⁻⁴ ≪ 1` at 130 GeV, for `ε=4.2×10⁻⁹`). So the visible-baryon factor is the pure SM
value — a calculation whose ECCG validity is now established, not assumed. (Caveat: a strong-portal or
`SU(2)_L`-charged variant would need recomputation; the benchmark is safe.) **This one moves from "assumed" to
"calculated."**

## ECCG microscopic cluster

**E1. First-order transition "confirmed three ways."** → **[CORRECTED; the lattice leg is OPEN]** The 4D
one-loop and 3D-DR legs are robust; the lattice leg is a **validated pipeline** with a **PRELIMINARY** (single-
volume, non-converged) ECCG point + one digitized input. Closure: restate as "4D one-loop + 3D DR robust;
lattice pipeline validated, ECCG point preliminary — continuum/infinite-volume convergence **[OPEN]**, needs a
lattice run." Cannot be desk-closed.

**E2. SQCD confining vacuum / `Λ_H`, `⟨Θ⟩`, `κ₂`.** → **[CORRECTED; OPEN]** One-loop qualitative at strong
coupling (`g_H≈1.95`). Closure: label "benchmark-level qualitative estimate; controlled value **[OPEN]**, needs
lattice." Cannot be desk-closed.

**E3. Propagation problem** (truth-status tags evaporate up the stack). → **[CORRECTED — a documentation fix I
can do]** Carry the `PRELIMINARY`/`QUALITATIVE` tags from the reports up into the End-to-End paper's "confirmed"
and the USC over-determination conditions. This is the one ECCG item fully closable now (by editing the
summaries, pending your go-ahead to touch the manuscripts).

---

## Scoreboard

| kind | count | items |
|---|---|---|
| **[CALCULATED]** — newly derived | 1 | N4 (f_B) |
| **[CORRECTED]** — closed by making the claim true | 6 | T1, T3, N1, N2, N3, E3 |
| **[CORRECTED + OPEN residual]** | 3 | T2 (exact c), E1 (lattice), E2 (SQCD) |
| **[OPEN]** — paper-scale / lattice / data | — | D-4′ (the 4π, feeds T2/T3), D-5 exact coefficient, converged lattice, controlled SQCD |

**Honest bottom line.** The assumed-vs-calculated gaps are now *closed in the only legitimate senses*: one is
genuinely calculated (f_B); six are corrected so the claim matches reality (the thermal→NESS reframe, the
`b`/`γ` parameter honesty, the gate narrative, the ECCG propagation); and three carry an irreducible open
residual (the exact `c` O(1), a converged lattice, the SQCD controlled calculation) that **no one can close
from a desk** — I flag these rather than paper over them. Propagating the six corrections fully into the
primary manuscripts (beyond the banners already added) is the remaining action, pending your go-ahead per
paper. The breadth sweep (3 agents) will add any further instances to this ledger.
