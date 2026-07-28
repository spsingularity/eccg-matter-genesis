# USC pre-registered falsifier matrix — frozen 2026-07-16

**Purpose.** Freeze every falsifiable commitment of the USC program (SEDE dusk + three-horn dawn + KMS-inertia
galactic face + transmutation scale sector) *before* the deciding data arrive (DESI Σm_ν & DR3, LiteBIRD/CMB-S4,
nEDM, cluster SIDM, JWST high-z kinematics). Companion machine-readable freeze:
`PREREGISTRATION_frozen_values.json` (sha256 in §F). Nothing in this document may be edited after freeze;
corrections go in a dated addendum.

**Provenance.** Numbers are the corpus benchmarks as consolidated 2026-07-16 (see
`SESSION_SYNTHESIS_2026-07-16.md`); every value reproduces from a script in `unified/sims/` or
`new-research/st/research/src/`. Grades: [IDENTITY]/[THEOREM]/[DERIVED]/[ESTIMATE]/[CONJECTURE] per corpus
convention.

**Structure.** Each prediction: *statement → current status → deciding data → decision rule → what dies.*
Predictions marked ◆ are realization- or horn-conditional (the rule says which branch dies, not the program).

---

## A. Dusk — dark energy (SEDE / USC injection frame)

**P1. Δ = 1 exactly** (volume-law horizon entropy; discrete — no intermediate value available). [THEOREM-conditional]
Deciding: DESI DR3 + Euclid, forecast σ(Δ) ≈ 0.087.
Rule: |Δ̂ − 1| > 3σ falsifies the volume law; Δ̂ statistically *intermediate* (≠0, ≠1) falsifies the
discreteness (leg-budget) framework itself. Δ̂ = 0 restores the area law and kills SEDE outright.
Dies: the entire dusk sector, hence the union.

**P2. The growth–expansion lock** `1 + w = ⅓[2λε − d ln f_sat/d ln a]`, λ = 1/2 — an exact,
zero-free-function identity (verified to 4 decimals). [IDENTITY]
Deciding: joint w(z) + fσ8(z) (DESI + Euclid + LSST).
Rule: any statistically significant violation falsifies the action (not a fit). Also the discriminant vs
GREA: SEDE's entropy production is structure-timed (D(z)), GREA's is expansion-timed.
Dies: the SK/injection action.

**P3 ◆. The equation of state and the crossing.** CPL (w₀, wₐ) = (−0.984, −0.109); w₀,today = −0.996;
**z_cross = 0.191 in the injection frame** vs **z_cross ≈ 0.016 or none in the conservative FPAB-KGB** —
the crossing is a *realization discriminator*, not a single model prediction. Current GP reconstructions:
z_wt ≈ 0.46 (+0.24/−0.12) — a live ~2.2σ tension, registered as such.
Rule: a measured z_cross ≈ 0.19 selects the injection frame; ≈ 0 or absent selects conservative-KGB;
≈ 0.46 confirmed at >3σ falsifies both USC realizations.
**At-risk register:** SEDE sits 2.7σ/3.6σ/4.2σ/3.0σ from the DR2 CPL centers (Pantheon+/Union3/DESY5/BAO);
**if DR3 confirms the DR2 centers at higher significance, SEDE is falsified alongside ΛCDM** — registered.

**P4 ◆. Growth amplitude.** Legacy smooth pipeline: S8 = σ8 = 0.76; FPAB v0.3 completion: σ8 = 0.811
(the 0.76 is retracted in that track). The full-likelihood campaign (Tier-2) must commit one number
*before* comparison to Euclid/LSST lensing; until then both are registered with their tracks.

**P5. Growth + ISW signature** (CORRECTED, Tier-1 #1; ISW briefly retracted then reinstated in Tier-2 `TIER2_referee_grade_result.md`). [DERIVED, mochi-computed]
> ✅ **Tier-2 status:** BOTH channels stand. (1) **+2–3% scale-independent `fσ8` enhancement through the RSD range** (from `μ_∞=1.05`; `+2.6%` P(k), `+1.3%` σ8) — from the sane sub-horizon P(k). (2) **−7.6% low-ℓ ISW**, `C_ℓ^TT(ℓ=2)=0.9236` — reproducible with `z_gr_smg ≤ 5` (the corpus's `z_gr_smg=99` is a pathological regime that fakes a giant ISW via a spurious `k≈0.02` scalar oscillation; the mid-Tier-2 retraction of the ISW was that artifact, now corrected). Only the *DE clustering* `δ_DE/δ_m` is horizon-confined (~7×10⁻⁵). **Rule:** a `fσ8` NOT enhanced by ~+2–3% at DESI DR3+Euclid falsifies the μ(k) modification; the sign (enhancement) is opposite to what eases S8. Original text:
Sourced-fluid (injection) and statistical-reservoir realizations *both* confine the gate–matter response to
k ~ aH: δ_DE/δ_m ≈ 6 at k ≈ aH, ≤ 7×10⁻³ at k = 0.01 h/Mpc, ≤ 7×10⁻⁵ at k = 0.1 h/Mpc.
Deciding: ISW × LSS cross-correlations; RSD/full-shape.
Rule: **any detected gate–matter correlation at k ≳ 0.01 h/Mpc kills both realizations.** An ISW-scale
anomaly with no RSD counterpart is the positive signature.

**P6. The braiding fraction b becomes measurable.** μ_∞(0) = 1.051 (b = 0.20) / 1.052 (b_QCD = 0.2062) /
1.323 (b = 1); stability floor b ≥ 0.164. Current μ₀ = 0.04 ± 0.22 allows all; forecast σ(μ₀) ≈ 0.05
(DR3 + Euclid) separates the endpoints at ~5σ.
Rule (three-way origin test): measured b ≈ 0.206 → visible-QCD amplitude hypothesis; any other value →
transmutation origin (or neither). Whatever b is measured, the 2PI reservoir must supply exactly
(1−b)·ρ_X f′/(9H) of the dissipation — else the conservative and dissipative realizations are inequivalent
and P3/P5 discriminate them.

**P7. Early-universe cleanliness (C2).** No early dark energy (Ω_DE(z=1100) ≈ 10⁻¹⁰), BBN speed-up = 1.0,
ΔY_p = 0; dark-completion ΔN_eff ≈ 0.018. Registered: SEDE predicts **zero cosmic birefringence** —
the ACT DR6 hint (0.215° ± 0.074°, 2.9σ) is a live threat if it consolidates.

## B. Dawn — three horns (matter genesis + dark matter)

The dawn is a **three-horn structure**; the horns are mutually exclusive and the matrix below separates them.
All horns share: no LISA/PTA-band first-order-transition background from baryogenesis (**P12**), and the ~700 Hz
wall signature is retired.

| | **horn (i)** ECCG-res-(iv) | **horn (ii)** C² seesaw | **horn (iii)** C + glueball |
|---|---|---|---|
| η_B | fit (m₃/H = 1.58) | **derived** (∝ T_RH²Σm_ν²) | **derived** (same channel) |
| DM | ADM **m_X = 1.78 GeV** (1.63–1.78) | band 0.18–840 GeV | **glueball m_G = 6Λ_h = 180–630 MeV** |
| Ω_DM/Ω_b | **explained** (co-genesis) | partial | unexplained (Br ≈ (0.4–3)×10⁻¹⁰ dial) |
| tensors | **r ≤ 2×10⁻¹¹** | allowed | allowed |
| nEDM | branch-B at current bound | — | — |
| Σm_ν | free | **NO, 59–64 meV** | **NO, 59–64 meV** |
| SIDM | velocity-dependent (φ, 0.86 MeV) | model-dep. | **velocity-independent, σ/m = 0.47/0.09/0.01 cm²/g at Λ_h = 30/52/105 MeV** |
| direct detection | invisible (σ_SI ~ 2×10⁻⁴⁸, below ν-fog) | model-dep. | invisible (no portal) |

**P8. Primordial tensors.** Rule: **any B-mode detection (any r) kills horn (i)** (the pre-inflationary
condensate) and selects horns (ii)/(iii). Conversely r ≈ 0 forever is consistent with all three (weak).

**P9. Neutron EDM.** Horn (i) branch B (v_S = 2.44×10¹³): θ̄ ≈ 4×10⁻¹² × sin Δ_CP × O(1) — d_n within
roughly an order of the current bound. Rule: a null at 10× tighter kills branch B (forces the two-flavon
branch A); a detection near the bound is positive evidence for horn (i).

**P10. Neutrino masses (the nearest verdict).** Horns (ii)/(iii): **normal ordering AND Σm_ν = 59–64 meV
AND T_RH ≈ 3.3×10¹² GeV** (prior-volume survival already only 0.31–1.27%).
Rule: inverted ordering confirmed, or a robust cosmological ceiling **Σm_ν < 59 meV**, kills the
clock-baryogenesis horns (ii) and (iii) — leaving only horn (i). Σm_ν ≈ 0.6 eV (strong washout) is already
excluded by η_B overproduction.

**P11. Dark-matter character.** Horn (i): a ≈1.78 GeV *mass* target, DD-invisible (a claimed DD detection
at other masses above the fog is evidence against). Horn (iii): velocity-*independent* SIDM at
σ/m = 0.01–0.5 cm²/g. Rule: a cluster-scale exclusion of σ/m > 0.1 pushes Λ_h ≳ 50 MeV — **selecting the
UZ-corrected coefficient (52 MeV) over the bare one (28.5 MeV)**: halo astrophysics measures χ_top/m_G. In
the mixed corner (ξ ∈ [0.0006, 0.0025]) a measured m_X in the *low* band 1.63–1.70 GeV is the glueball-
subcomponent hint.

**P13. Isocurvature.** Horn (i): correlated baryon–DM isocurvature sitting *just below* the Planck CDI bound
(it is what sets H_inf < 1.16×10⁹); only a wrong correlation structure falsifies.

## C. Galaxies — the KMS-inertia MOND face

**P14. a₀(z) rises like H(z)** (rate branch). Frozen templates over z = 0.33 → 1.44:
rate 1.89 ± 0.03 · flat 1.00 · activated 0.49 · density 0.89–0.91. MUSE currently gives 2.16 ± 0.06 —
density excluded +16.7σ, rate favoured (+4.4σ shallow, B(z)-absorbable) — **conditional on the MUSE pipeline**
(raw catalogue is radius-degenerate, corr(rmax, z) = 0.87; registered).
Deciding: **E-1″ protocol** — independent high-z RAR with per-galaxy baryonic decompositions, matched
M*/morphology bins, matched radius sampling in R_eff units, σ(a₀-ratio) ≤ 0.15, decision rule frozen in
`CLOSEOUT_remaining_items.md` §7.
Rule: collapse under a₀ ∝ H confirms the rate branch (→ cascades: horn-(i)-compatible DM + r ≈ 0 if horn (i);
see P8/P10 joint reading). No collapse under any one-parameter A(z) → a₀ is not cosmological → the galactic
face fails.

**P15. Gate independence** [new, coefficient-independent]. a₀ carries **no f_sat factor**:
a₀(3)/a₀(0) ≈ 4.5 even though Ω_DE(z=3) ≈ 3% — **MOND persists and strengthens at high z where dark energy
is off.** Rule: weakened/absent deep-MOND phenomenology in z ≳ 2–3 rotators (JWST) falsifies the KMS-inertia
realization; it is also maximally separated there from any a₀ ∝ ρ_DE^n model.

**P16. The interpolation function, zero shape freedom:** g_obs = √(g_bar² + a₀g_bar). Sits within 0.057 dex
of the empirical ν-function, with a specific signed pattern (−0.05 dex at g_bar ≈ 0.4a₀).
Rule: SPARC-quality stacking that resolves shapes at <0.05 dex either detects the predicted pattern or kills
this specific inertia law (without killing the rate branch as such).

**P17. Modified-inertia discriminators:** exact algebraic RAR on circular orbits (no curl corrections — AQUAL
has them); a non-AQUAL external-field effect. Registered qualitatively; quantitative EFE prediction owed with
the covariant embedding.

**P18. The a₀ normalization:** a₀(0) = cH₀/2π × O(1), O(1) ∈ [0.88, 1.16] pending the 4π worldline
derivation (`D4prime_worldline_formulation.md`). If the derivation yields A = cH/4π exactly, the O(1)
becomes a prediction at the ~10% level and this entry tightens.

## D. Scale sector (transmutation, conditional on horn (iii) or the μ-origin claim)

**P19. Invisibility clause:** the viable hidden sector has ΔN_eff ≈ 0 (glueballs matter-like before BBN).
Rule: a future ΔN_eff detection at 0.1–0.4 is **not** support for this sector (and would demand another
origin); the sector's only kinetic window is P11's SIDM.

**P20. The lattice discharge test:** pure-glue SU(3) vacuum energy carries a finite-volume term
ρ_vac(L) − ρ_vac(∞) ∝ χ_top/(m_G·L). Rule: a lattice determination consistent with zero at the relevant
precision kills the UZ mechanism, hence the transmutation route to μ (and its N1 identification); a detection
fixes the μ-coefficient and (via B.2) the a₀ chain.

## E. Joint / cross-scale readings (the union's signature moves)

- **The master cascade:** rising a₀ (P14) + r ≈ 0 (P8) + nEDM at bound (P9) + m_X = 1.78 (P11) = horn (i)
  fully confirmed. Rising a₀ + any r detection + Σm_ν at floor (P10) + SIDM at 0.1–0.5 (P11) = horn (iii).
  These are *different universes*; the matrix cannot be satisfied à la carte.
- **The sum rule:** 𝒟_E^SEDE + 𝒟_E^APDM = 3 exactly (no dark–visible coupling); a measured deviation is a
  direct detection of dark-sector energy exchange and falsifies the D-6 internal-donor structure.
- **Double-kill clauses:** Σm_ν < 59 meV kills horns (ii)+(iii) the same week; DR3-confirms-DR2 kills the
  dusk and with it all faces; RSD-scale gate correlation (P5) kills both dusk realizations at once.

## F. Freeze mechanics

Machine-readable values: `PREREGISTRATION_frozen_values.json` — the JSON is the canonical numeric record,
this document the canonical rules.

> **sha256(PREREGISTRATION_frozen_values.json) =**
> `a0ee6c9b080999ddc09ec77d3a83ab7be5f8a77ffca742638c43a60ed0b70595`

Recommended: commit both files, tag the commit `prereg-2026-07-16`, and (optionally) deposit the pair with a
timestamping service (OSF/Zenodo). Addenda append; nothing edits.
