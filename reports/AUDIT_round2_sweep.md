# Audit round 2 — breadth sweep (3 agents) + closure verdicts

Three agents swept SEDE-dev, USC docs, and ECCG+APDM for the assumed-as-derived failure mode. They found
~40 further instances. Below: the highest-signal NEW ones, each with a **closure verdict** — `[CALC]` I can
calculate, `[CORRECT]` un-calculable → fix the claim, `[OPEN]` paper-scale/lattice/data. As before, almost
none are calculable: they were assumed *because* they can't be. Closing them = correcting the claims.

## The three meta-patterns (the sweep sharpened these)

**P1 — thermal framing** (round 1): asserted, fails 10⁵⁷/10⁻²²/10⁻⁷. → **[CORRECT]** (NESS reframe, banners done).

**P2 — matched-benchmark / fit dressed as derivation** (pervasive, the dominant pattern):
the whole corpus repeatedly presents "a consistent point exists (with free knobs retuned)" as "derived."

**P3 — convergence by shared normalization** (NEW, the most important round-2 finding): multiple "independent
confirmations" that actually share *one* calibrated forward model or *one* tuned knob, so the joint impression
of convergent derivation exceeds the sum of the parts.

---

## P3 — the new meta-finding (both sectors)

**[CORRECT] ECCG's four "independent" confirmations share one reverse-engineered normalization.** `Δ_CP`,
`m₃/H`, `η₂`, `v_w` are each held fixed in one report while "predicting" via a **common calibrated
`predict_eta_B.py`** that already encodes the `η_B` fit — each report tunes its *own* knob (`η₃=1`, `m₃/H`
solved, bracket=1, `T*` free) to the same `η_B ≈ 6×10⁻¹⁰`. So "four confirmations landing on `η_B`" is partly
one fit viewed four ways. *Fix:* state that the dawn cross-checks share a calibration; they are one
consistency, not four predictions.

**[CORRECT] USC's flagship "zero free functions and zero free couplings" is built on a matched function + a
retracted coupling.** `ζ` is *matched* to SEDE (`ζ_res=0` is a *choice*), and `c=1/2π` is *retracted* at the
top of `covariant_action.md` (D-5 FDT) yet still *banked as a derivation* in `parameter_reduction.md` (R5/R6)
— an internal contradiction. *Fix:* "zero free functions" → "one matched function (ζ=ζ_SEDE) + one residual
set to zero by choice"; drop `c=1/2π` from the derived column.

---

## P2 — matched/fit-as-derived (the biggest bucket), NEW instances

**Dark energy (SEDE):**
- **[CORRECT — the strongest new SEDE item] `Δ=1` "exactly, zero free parameters" is an IR-cutoff choice.** The
  count paper's own §5.2 shows `Δ` is a smooth monotone function of a cutoff `L` that "nothing in SEDE
  determines" (`L=`particle horizon → `Δ=0.855`); `Δ=1` appears only at `L→∞`, justified by silently
  identifying the cosmological spatial slice with the entanglement-network IR cutoff. And §8 admits "`Δ=1`
  remains the empirical bet, **not a theorem of this counting**" — contradicting the abstract's "discharged."
  This confirms `Δ=1` is *the* one DE postulate (already in the ledger), now with the reverse-engineering
  exposed. Reinforces N-node N1 as the single irreducible input.
- **[CORRECT] `z_cross = 0.195` "genuine prediction, not a knob"** — convention-selected: the Cai–Kim
  `(1−ε/2)` alternative "fails" and is discarded, so the surviving GH convention is *chosen* because it gives
  a crossing in the right quadrant (and it sits ~2.2σ from the data-preferred GP value).
- **[CORRECT] `p=5/3` "forced"** — a revision from `p=1` to the data-favored value, then asserted "forced"
  (self-flagged: "happens to be the one favoured in diagnostic fits").
- **[CORRECT — statistical] `Δχ²≈371` "area-law excluded"** is a *profile*, not a posterior — it inflates the
  real marginalized signal (`ΔDIC≈−3`) by ~100×. And `σ(Δ)=0.087`/"11σ" is Fisher-optimistic; the OOS
  `Δχ²=−8.2` is the cherry-picked direction (reverse split favors ΛCDM). *Fix:* quote the marginalized ΔDIC,
  label the profile and Fisher numbers as such.

**Matter (ECCG):**
- **[CORRECT] `Δ_CP=π/2` "calculable via SCPV"** — a symmetric-point value the report admits is *not
  radiatively stable*; the real output is a scan median over an *assumed* coefficient measure (only 22% has
  the needed `λ'>0`). Not a derivation.
- **[CORRECT] "No fine-tuning, `Δ_BG=2`, 38th percentile"** — `m₃/H` is *solved to hit `η_B`*, not sampled, on
  a calibrated forward model; `Δ_BG=2` (product-of-powers) is real, but the "viable-volume percentile" is a
  level-set of the fit, not per-point pipeline physics.
- **[CORRECT] `η₃/η₂=ε` "parameter-free, 13% accurate"** — the 13% *is* the leftover mismatch; it needs an
  assumed bracket ≈1 + an assumed ℤ₂ chain parity. `η₂=9.85` "to machine precision" is a fit (10 O(1) inputs
  for 2 outputs; universality excluded).
- **[OPEN] `v_w=0.58`** — an LO *ballistic* friction ansatz, not a Boltzmann transport solve; the `±0.09` is an
  *assumed* ×0.7–1.5 NLO envelope. "Full transport" overstates; needs a WallGo-style solve.
- **[CORRECT, propagates] S₃ "gaugeable" and the 14→4 parameter reduction** — anomaly part derived, but the
  non-Abelian dynamics (partner-condensate alignment) and a global `Pin⁺` anomaly are undischarged, and "S₃
  cannot stand alone," which *undercuts the 14→4 count* that GLOBAL_SCAN leans on. Also a shipped ℤ₃₁ claim
  (`ΣQq²=4≠0`) that fails to reproduce.

**USC bridges:**
- **[CORRECT] Dark-sector "0.0% match"** is circular (`η_X` is a fixed input fed back to itself; §5: "not
  rederived"). The `520 MeV` vector and `m_X` closures are benchmark-existence with free-coupling retunes
  (`g_A: 0.040→0.046`).
- **[CORRECT] Candidate C "`η_B` derived"** — `T_RH` is *fit to `η_B`* then declared natural by window-overlap.
- **[CORRECT] `m_X=1.78` "genuine prediction"** = (observed `Ω_DM/Ω_b`) × `m_p` × (`f_B`), i.e. largely a
  repackaging of the observed abundance × the (now-closed) SM factor; only `f_B` is computed.
- **[CORRECT] APDM `𝒟_E+(3/2)(1+w)=3` "[IDENTITY]"** is a definitional tautology (holds for any `w`);
  "verified, sum=3.000" verifies algebra. The `a₀=cH₀/2π` "[SCALE/IDENTITY]" re-asserts the retracted GH-2π.
- **[CORRECT] `ρ=Ts` "on-shell as attractor"** reinserts the volume-law postulate as the `+3Hs` source term —
  "derived on-shell" is "postulate as source."

**Galactic (APDM):**
- **[CORRECT] Phonon `c_s=150 km/s ≈ v_c`** — the *scaling* `c_s=ρ/2Λm³` is derived, but the *value* is
  matched (`Λ` tuned so `c_s=v_c`; "consistency, not prediction" is the honest caveat). "Near-tricritical
  structure derived" is analogy (BEG/He³–He⁴) + an assumed biquadratic coupling.

---

## Closure scoreboard (rounds 1 + 2 combined)

| verdict | count | meaning |
|---|---|---|
| **[CALC] genuinely closed by calculation** | 1 | `f_B=28/79` (SM factor, ECCG-valid) |
| **[CORRECT] closed by fixing the claim** | ~25 | thermal→NESS; the P2 matched/fit items; the P3 shared-normalization disclosures; the statistical profile/Fisher/OOS labels |
| **[OPEN] needs paper-scale calc / lattice / data** | ~6 | exact `c` O(1) (D-4′); D-5 exact coefficient; converged lattice; controlled SQCD; full `v_w` transport; the S₃ dynamics + global anomaly |

**The honest verdict.** "Close all assumed-vs-calculated gaps" resolves to: **one is genuinely calculated
(`f_B`); the large majority are un-calculable overclaims whose only honest closure is correcting the claim to
match reality (which I have done in these audit docs and, for the thermal cluster, propagated into the corpus
via banners); and a small residual is irreducibly open (paper-scale calculations, a lattice run, external
data).** No one can *calculate away* the P2/P3 items — they are matched benchmarks and definitional identities,
not un-computed integrals. The value delivered is the complete, honest re-labeling + the single new
calculation + the exposure of the P3 shared-normalization illusion (the sharpest structural finding: several
"independent confirmations" are one fit viewed many ways).

**Remaining action (your call):** propagate the ~25 [CORRECT] relabelings from these audit docs into the
primary manuscripts (banners are fastest and match the corpus convention; full body rewrites are larger). I
have done the thermal cluster; the P2/P3 items are documented but not yet propagated.


---

## PROPAGATION STATUS (updated)

The [CORRECT] relabelings are now propagated into the source manuscripts as correction banners:
- **USC corpus (`unified/docs/`):** parameter_reduction, dark_sector_completion, shared_mechanisms,
  open_derivations, c1c4_test, APDM_relation (+ the 6 thermal-cluster docs from round 1). ✅ committed.
- **SEDE-dev (`../SEDE-dev/paper/`):** SEDE_count (Δ=1/L→∞), SEDE_cosmology (z_cross, p=5/3, A_s, Δχ²=371),
  SEDE_foundations (ρ=Ts, Landau, NESS). ✅ committed in the SEDE-dev repo.
- **ECCG (`../ECCG/.../eccg_gap_closure/`):** SPONTANEOUS_CP (Δ_CP=π/2), GLOBAL_SCAN (38th-pct fit), 
  WALL_VELOCITY_PRECISE (v_w ballistic), FLAVOR_MODEL (η₂ fit). ✅ files corrected in place (ECCG is not a git
  repo, so no commit there — the banners are in the files).

**Not propagated (deliberately):** full body rewrites of abstracts/prose (the banners flag every overclaim at
its source; rewriting the surrounding derivations is the larger editorial pass, left for the author). The
[OPEN] items are flagged, not fixed (they need paper-scale calc / lattice / data).
