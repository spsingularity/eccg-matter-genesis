# External-calculation specifications — the four compute-bound open items (2026-07-17)

These four items cannot be closed at desk scale (they need lattice time or dedicated transport codes).
Closure here = each is converted from "known gap" to a **fully specified, executable project** with
inputs, observables, and decision rules — so any run that happens is decisive rather than exploratory.

---

## S-1. Converged ECCG lattice (first-order transition)

**Current state:** `LATTICE_MC` is a VALIDATED PIPELINE (1.3σ vs one published KKLP point) producing a
PRELIMINARY ECCG number at one volume/one spacing; one input digitized from a figure. The paper-level
claim "first-order confirmed by lattice" overstates this leg.

**Spec:**
- Action/couplings: the ECCG benchmark point (SU(3)_H + Φ_V/Φ_D scalar sector, couplings per
  `GLOBAL_SCAN_REPORT` benchmark).
- Volumes: N_s³×N_t ∈ {12³, 16³, 24³} × {4, 6, 8} — 9 combinations; continuum extrapolation in
  a → 0 at fixed physics via 3 lattice spacings (β-shifted), infinite-volume via the 3 N_s.
- Observables: (i) plaquette/Polyakov susceptibility peak height scaling with V (first-order:
  ∝ V; crossover: saturates); (ii) latent heat Δε/T_c⁴; (iii) surface tension σ/T_c³ via
  histogram-overlap (multicanonical needed near T_c); (iv) T_c/Λ_H.
- Replace the digitized-from-figure input with the run's own measurement.
- **Decision rules:** susceptibility ∝ V at all three spacings → first-order CONFIRMED (the paper's
  claim becomes true); saturation at any spacing → crossover → the ECCG baryogenesis chain loses its
  out-of-equilibrium leg → **falsifies the dawn mechanism as constructed**. Latent heat feeding v_w
  (S-3) and the GW forecast.
- Scale: ~10⁶ core-hours (modest academic allocation); multicanonical reweighting at the 24³×8 point.

## S-2. SQCD confining vacuum beyond one-loop (Λ_H, ⟨Θ⟩, κ₂)

**Current state:** one-loop qualitative at g_H ≈ 1.95 ("lattice/controlled calc needed"); these anchor
the matter sector's absolute scales.

**Spec (two independent routes; either closes it):**
- Route A (controlled analytic): Seiberg-exact results for the closest N_f/N_c cousin with soft SUSY
  breaking treated as perturbation; deliverable: ⟨Θ⟩ and κ₂ with an error band from the
  soft-breaking expansion parameter (m_soft/Λ_H), valid if m_soft/Λ_H ≲ 0.3.
- Route B (lattice): same action as S-1 with the fermionic sector; measure the Θ condensate and the
  two-point κ₂ directly at the S-1 spacings.
- **Decision rule:** if the honest band on ⟨Θ⟩ moves the derived η_B by more than the res-(iv) window
  width, the Candidate-C squeeze (Σm_ν 59–64 meV) shifts accordingly and must be re-quoted — the
  falsifier value is downstream of this input and currently carries its uncertainty silently.

## S-3. Full v_w transport (beyond LO ballistic 0.58)

**Current state:** LO ballistic estimate v_w = 0.58; the paper's η_B uses it as if converged.

**Spec:** standard bubble-wall transport (Boltzmann + wall EOM):
- Inputs from S-1: Δε/T_c⁴, σ/T_c³; friction from the dominant channel (Φ quanta on the wall,
  top-analog Yukawa-weighted).
- Solve the coupled fluid equations (Moore–Prokopec formalism or the modern hydrodynamic variant) for
  deflagration vs detonation branch; deliverable v_w ± band and the wall profile L_w T_c.
- **Decision rules:** v_w ∈ [0.3, 0.7] → η_B prediction stable within a factor ~2 (current claim
  survives); v_w → 1 (runaway) → the sourced asymmetry drops sharply → the "no fine-tuning, 38th
  percentile" claim fails and the m₃/H knob must be re-fit (P2-pattern flag); v_w < 0.1 → diffusion-
  dominated regime, η_B rises, DESI Σm_ν squeeze *tightens*.

## S-4. Mirror-QCD T_c/Λ_MS̄ at N_f = 6 (the μ scale)

**Current state:** perturbation theory brackets Λ_h to a factor ~5 (28–133 MeV, TIER1 #2: near-conformal
loop sensitivity); the physical scale needs the nonperturbative T_c/Λ_MS̄ ratio.

**Spec:** pure lattice question, standard technology: N_f=6 SU(3) with light degenerate quarks,
staggered or Wilson, T_c from the chiral susceptibility peak, Λ_MS̄ via the gradient-flow coupling.
Existing N_f=6-ish studies (near the conformal window) can be reanalyzed first — a literature pass may
close it without new runs.
- **Decision rule:** T_c/Λ_MS̄ pins Λ_h within ~15%; then the transmutation μ is either 28.5 (bare) or
  52 MeV (UZ) — discriminating the two coefficients that the LRD-seeding pincer
  (`GLUEBALL_LRD_seeding_assessment.md`) and the SIDM cluster bound attack from opposite sides. Three
  independent probes would then converge on one number — or fail to, falsifying the transmutation
  identification.

---

**Ledger effect:** the four compute-bound gaps are now *defined projects with decision rules*, each
wired to a named falsifier. Nothing about them is conceptually open; all remaining ignorance is
purchasable with compute.
