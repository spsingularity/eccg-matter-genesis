# Audit: assumed vs calculated across the corpus

Extends the discipline of the D-5 FDT check (where "derived from KMS symmetry" turned out to hide an
assumption that fails by 10⁵⁷) to the whole corpus. Each item graded: **[NEW]** a place presented as
derived/known that actually assumes something, caught this session · **[SHARPENED]** a known soft spot made
precise · **[ACKNOWLEDGED]** the corpus already flags it. A balancing list of what *is* genuinely calculated
is at the end, so this reads as an audit, not a hit piece.

---

## I. The meta-pattern: a THERMAL structure is assumed repeatedly, and fails when computed

Three independent places invoke a thermal/KMS/Unruh structure; all three, when calculated, are **not thermal**:

| where | thermal claim | computed reality | ratio |
|---|---|---|---|
| **dusk DE dissipation** | `ζ>0` is the FDT noise at `T_AH` (KMS) | noise is cold/structure-sourced (D-5 FDT) | **10⁵⁷×** too large for thermal |
| **galactic MOND (D-3′)** | inertia = reaction to the Deser–Levin *thermal* tilt | no thermal bath in a galaxy | **10⁻²²** modes (≪1) |
| **dawn baryogenesis** | one KMS structure ties `T_n` and `H_n/2π` | two incommensurate temps → NESS | ratio `10⁻⁷` (corpus's own finding) |

**[NEW] The honest unified statement:** the Ledger Field / clock is a **driven, entropy-producing (NESS)**
system at *every* face — dawn, dusk, and galaxies — **never a KMS-thermal EFT.** The elegant "single dynamical
KMS symmetry" that the corpus (and my R1 derivation) leaned on is an assumption that the numbers reject in all
three sectors. What survives everywhere is the weaker, real structure: **covariant + causal + second-law
(monotone entropy production)**. The mean thermodynamics (`ρ=Ts`, `T_AH=H/2π` from Gibbons–Hawking) survives
as a *background/geometric* fact; the *fluctuation*-KMS does not.

---

## II. Specific "assumed, not calculated" items

**[NEW] `c = 1/2π` is asserted from a KMS-strip analogy that D-5 shows does not apply.** The "unit coupling per
KMS period" derivation assumes the state is KMS (modular strip width `2π`, Tomita–Takesaki). D-5 shows the
state is not KMS at `T_AH`. So `c=1/2π` is an assertion from a broken analogy — and the 16% residual
(`a₀ = 1.16·cH₀/2π`, G-D3) is the independent confirmation that it's a ~16% *match*, not a derivation. The
geometric Gibbons–Hawking `2π` (a background fact) may survive; the fluctuation-KMS reading does not.

**[NEW] The D-3′ KMS-inertia MOND rests on a thermal assumption APDM's own notes already falsified.** APDM's
`reframe_test_results.md` killed the "horizon thermal-bath / FDT route" for `a₀` (`<10⁻¹⁹` bath modes in a
galaxy, can't thermalize in a Hubble time). My D-3′ revived essentially that route (`inertia ∝ excess
Deser–Levin temperature`) without noticing. `d3prime_thermal_consistency.py` confirms `~3×10⁻²²` bath modes.
**So D-3′ survives only if reinterpreted as a *vacuum* (not thermal-equilibrium) effect — which is exactly the
unresolved D-4′ (needs the covariant action).** I over-credited D-3′ as "the surviving mechanism"; it's a
surviving *heuristic* with the same thermal problem as the branch it replaced.

**[SHARPENED] The Avrami/KJMA gate is "derived" only by analogy.** `f_sat = 1−e^{−γD²}` is presented as
derived (Avrami coverage law). But Avrami describes random nucleation + growth with a specific geometry;
applying it to "horizon-entropy activation by structure collapse" *assumes* the activation is such a coverage
process — an analogy, not a computed mapping. Worse, the gate uses `D² = σ8²(a)/σ8²(1)`, which **cancels the
primordial amplitude** — a universe with `10⁻⁵×` the structure has the *same* gate (stress-test M-flag;
Candidate-E `A_s`–`γ` degeneracy). So "structure *amount* activates DE" is false as stated; the gate depends on
the growth *ratio*, and its exponential form is assumed by analogy.

**[SHARPENED] `T_AH = H/2π` drops the Cai–Kim `(1−ε/2)`** (~25% today) — a stability-motivated *choice*, not
the computed apparent-horizon temperature. (Already folded into my R1 derivation's honest scope, but it is an
assumption the SEDE papers present as "the horizon temperature.")

**[SHARPENED] The injection frame is chosen, its physical donor asserted.** The G4 a-leg coupling is *forced*
by SK unitarity (a real argument); but that there *is* an injection `Q = c∇·𝒥` with `𝒥 = s_grav u^μ` (rather
than some other coupling) is a modeling assumption. D-6 derived a constraint (donor internal to the dark
sector), which narrows it — but the injection structure itself is posited.

**[SHARPENED] Mirror unification assumes `α_h(M_Pl) = α_s(M_Pl)`.** The transmutation-μ "no new coupling"
economy rests on *assuming* the hidden confining coupling equals the visible QCD one at the Planck scale —
physically unmotivated (why would a hidden sector share the SM coupling?). Drop it and `μ` is a free scale
again.

**[ACKNOWLEDGED, still assumptions]** `Δ=1` (volume vs area — the one DE postulate); `η_B` magnitude / `m₃/H`
(fit, MaxEP fails); `Ω_DM/Ω_b = 5.36` (adopted); `v_w` (estimated); `γ ≈ 1.5` (halo plausibility, "not
established" per stress test); `μ ≈ 28.5 MeV` (flatness/QCD-coincidence); UZ `ρ∝HΛ³` (contested); glueball
abundance (a `Br` dial, not derived).

---

## III. What IS genuinely calculated (for balance)

These stand up — they are computed, not assumed:

- **The clock identity** `𝒟_E = (3/2)(1−w)` — from `Θ_E` definition + Friedmann. [exact]
- **`γ_slip = 1`** — from `α_M=α_T=0`; confirmed through the Boltzmann code (`φ/ψ = 1.0000`, Stage-2 run).
- **`Δ ≤ 1`** — the leg-budget theorem `C(Ω) ≤ κ|Ω|`. (Only `Δ=1` vs `<1` needs the extra assumptions.)
- **The dawn no-gos** — `R₀ = 0` (the arrow is ℤ₂-even) and the spurion-neutrality theorem. [genuine symmetry
  theorems]
- **The generalized single-source theorem** — `η_B`-calculable XOR `m_X`-sharp. [genuine EFT theorem]
- **`f_B = 28/79`** — the standard SM sphaleron `B−L → B` conversion. [textbook SM]
- **`α_h(M_Pl) = 1/83`** — one-loop RG for confinement at 28.5 MeV. [computed]
- **The finite-k SEDE observables** — `μ_∞ = 1.05`, `P/P_ΛCDM`, `C_ℓ^{φφ,TT}` — through the mochi Boltzmann
  code (Stage-2). [computed, and the reconstruction is deterministic]
- **D-6 (RSD safety), D-7 (`ζ>0` monotonicity), D-1 (reheating), D-2 (neutrino squeeze)** — all computed this
  session.
- **The growth–expansion lock** — an exact identity (honestly labeled as such: a consequence of the ansatz,
  not an independent prediction).

---

## V. Non-thermal assumed-not-calculated items

**[NEW, computed — corrects my own R1] The FPAB coefficients are NOT fully "slaved to the background": the
K/braiding split `b` is a free perturbative parameter.** My R1 response claimed the 16 KGB coefficients are
"outputs, 0 free." Running the mochi engine for `b = 0.20` vs `0.30` (same target background `ρ_X ∝ H f_sat`):

| `b` | `H(z=1)/H₀` (background) | `σ8` (perturb.) | `μ_∞` (perturb.) |
|---|---|---|---|
| 0.20 | 1.7533 | 0.8192 | 1.0507 |
| 0.30 | 1.7527 | 0.8206 | 1.0788 |

The **background is identical** (0.03%, numerical) but the **perturbations differ** (`μ_∞`: 1.05 vs 1.08). So
`b` is genuinely free — the background does not fix it; it is set by the QCD coincidence *or* the FPAB
stability floor, not by data at the background level. **Honest DE input count: `{μ, γ, Δ} + b`** — one more
than my R1 claimed. (`b` is measurable: DR3+Euclid separates `b=0.2` from `b=1` at ~5σ, so it's a genuine
extra prediction, not a hidden fit — but "parameter-free" and "0 free coefficients" are both wrong.)

**[SHARPENED, known via Candidate-E] The gate is `A_s`-independent, so "accumulated structure activates dark
energy" is false as stated.** Under the corpus's today-normalization (`q(1)/q_* = γ` fixed), the gate depends
only on `D²(a) = σ8²(a)/σ8²(1)` — the growth *ratio*, which cancels `A_s`. A universe with 4× the structure
power has the *identical* DE gate. The gate tracks growth *shape*, not structure *amount*; the physical
narrative in the papers ("cumulative structure entropy activates DE") is misleading (the exact `A_s`–`γ`
degeneracy is Candidate-E's own finding, but the prose wasn't corrected).

**[SHARPENED] `γ ≈ 1.5` is fit, not derived from halos.** The fitted value `1.4964` comes from the
gate-normalization/flatness; the "`γ = (p−1)⟨1/α⟩ ≈ 1.5` from `E_bind ∝ M^{5/3}`" is a plausibility number the
stress test itself calls "not established" (the log-slope implies a power law, not the truncated exponential).
The two are not independently checked; `γ` is a fitted shape constant.

**[SHARPENED, matter] `f_B = 28/79` is the *Standard-Model* sphaleron factor, assumed to carry over to ECCG's
extended field content.** 28/79 is the textbook SM `B−L → B` conversion — but ECCG adds chiral content (the
dark sector, condensate portals). Whether the factor is still 28/79 with that content is not recomputed; it is
assumed equal to the SM value.

**[ACKNOWLEDGED, model choices not derivations]** the `ℤ₃₁` discrete-gauge charge assignment (engineered to
forbid `P, P², P³`), the counter-rotating `Q_V = −Q_D` structure (imposed by the `U(1)_𝒬` assignment), and the
`a₀ = c²√Λ/2π` / `Λ⁴ = ρ_DE` "lock" (APDM-admitted dimensional postulates).

## VI. The ECCG microscopic sector — more honest than the rest, but the caveats don't propagate

**[POSITIVE — credit due] The ECCG gap-closure reports are epistemically the *most* honest part of the corpus.**
They carry explicit truth-status tags (`VALIDATED` / `PRELIMINARY` / `DIGITIZED-FROM-PUBLISHED-FIGURE` /
`DERIVED HERE`) and state their standard of closure up front:
> "a matched effective theory can be **closed** without **predicting** physics above its cutoff."
This is exactly the discipline the DE/USC sector lacks. The `FLAVOR_GUT_REPORT` is even labeled "HONEST
NEGATIVE." If the rest of the corpus adopted these tags, most of this audit would be unnecessary.

**[SHARPENED] But "CLOSED / COMPLETE / confirmed" means *a consistent benchmark exists within the EFT +
matching*, not *calculated* — and three load-bearing items are matched/qualitative/preliminary:**

1. **The first-order transition is not actually computed to convergence.** `LATTICE_MC_REPORT`: the code is
   "delivered and staged," `VALIDATED` against *one published* point (KKLP) at 1.3σ — i.e. the **pipeline** is
   validated — but the ECCG-specific result is **`PRELIMINARY`**: "one volume / one spacing / finite stats —
   **not** a converged continuum, infinite-volume number," and "could move by more than the statistical error
   under extrapolation." One input is `DIGITIZED-FROM-A-PUBLISHED-FIGURE` (read off a plot). So the End-to-End
   paper's "first-order confirmed three ways (4D one-loop, 3D DR, lattice MC)" overstates the lattice leg:
   honestly it is "a validated lattice pipeline whose *preliminary* ECCG point is consistent with first-order."
2. **The SQCD confining vacuum is a one-loop *qualitative* estimate.** `MICROSCOPIC_SQCD_THERMAL_REPORT`: "the
   one-loop transmutation formula is **qualitative rather than** [quantitative]," the coupling is "moderately
   strong" (`g_H ≈ 1.95`), and "a lattice or controlled [calculation] is needed." So `Λ_H`, `⟨Θ⟩ = Λ_H`, and
   the vacuum structure that anchors `κ₂` (hence the whole matter sector) are **benchmark-level qualitative
   estimates at strong coupling**, not controlled results.
3. **The four warped-sector "gaps closed"** are closed *as matched-EFT consistency* (the report says so
   explicitly), with the `P²` counterterm made calculable only by *supplying* a boundary UV completion — i.e.
   a modeling choice, not a derivation from the 5D EFT.

**[NEW — the propagation problem] The honest truth-status tags are lost as the claims move up the stack.** At
the report level: "`PRELIMINARY`, could move under extrapolation." At the paper level: "first-order confirmed
by lattice MC." At the USC level: this feeds the over-determination C-conditions as if the dawn benchmark were
solved. **The individual reports are honest; the summaries that cite them are not — the qualifiers evaporate.**
A referee who reads the End-to-End paper's "confirmed" and then the `PRELIMINARY` tag in the underlying report
will distrust the propagation. Fix: carry the truth-status tags up into the paper and the USC conditions (e.g.
"first-order: 4D one-loop + 3D DR robust; lattice preliminary, convergence pending").

## IV. The one-line takeaway

The corpus's **calculated** results are solid (clock identity, no-go theorems, finite-k Boltzmann observables,
the single-source theorem). Its **assumed-but-presented-as-derived** results cluster around one theme: a
**thermal / KMS / Unruh structure** invoked for the DE dissipation, the `c=1/2π` coupling, and the MOND
inertia — which, computed, is **absent by 10⁵⁷ (DE), 10⁻²² (MOND), and 10⁻⁷ (dawn)**. The fix is uniform and
*strengthens* honesty: reframe the whole program as a **driven, causal, second-law (NESS)** system whose *mean*
is horizon-thermal, and stop claiming the *fluctuation*-KMS structure. That subtracts three elegant
"derivations" (KMS-FDT, unit-coupling-per-KMS-period, thermal-inertia MOND) and replaces them with honest
open problems (D-4′ covariant action; the driven-EFT symmetry principle) — the same trade the D-5 FDT check
made, applied corpus-wide.
