# Can stationary entropy production derive m₃/H? — a decisive negative result

The highest-value calculation for turning USC's over-determination (C4) from a *consistency* into a
*prediction* was P4: derive ECCG's one fitted CP number m₃/H (hence η_B) from a stationarity principle at
the impulse. **Result: it fails, unambiguously.** The impulse efficiency is monotonic through the
benchmark and peaks ~4×10⁴ away; maximum-entropy-production would predict m₃/H ∼ 10⁴–10⁵ and a
catastrophically overproduced η_B. m₃/H = 1.84 is fixed by η_B-matching in the perturbative tail, not by
any extremum. This closes the direction honestly and confirms the parameter ledger's standing statement
("deriving m₃/H — no channel").

---

## 1. The hypothesis (P4)

The wall imparts a CP-odd impulse to the relative phase ψ, storing the charge n_Q ∝ ψ̇ that becomes η_B.
The reduced wall equation is
$$
\psi'' + \gamma_w g_3(\tau)\psi' + 2r_2^2 g_2\sin(2\psi) + 3r_3^2 g_3(\tau)\sin(3\psi+\delta_3)=0,
\qquad r_i=\frac{m_i}{\omega_w}.
$$
P4's claim: the efficiency n_Q(m₃) has an extremum — vanishing for m₃ ≪ ω_w (wall too fast, no torque)
and for m₃ ≫ ω_w (adiabatic, the phase tracks the moving minimum and returns) — and stationarity there
would pin m₃/H, making η_B a prediction.

## 2. The calculation

Integrating the wall equation (γ_w = 0.5, r₂ = m₂/ω_w = 3.0 from m₂/H = 2.3×10⁴, δ₃ = 1.3), the impulse
as a function of r₃ = m₃/ω_w:

| r₃ = m₃/ω_w | m₃/H | impulse \|ψ̇\|_max |
|---|---|---|
| 10⁻³ | 7.6 | 7.9×10⁻⁶ |
| 0.1 | 761 | 7.9×10⁻⁴ |
| 0.6 | 4566 | 2.7×10⁻² |
| 1.0 | 7610 | 6.4×10⁻² |
| 2.5 | 19025 | 1.9×10⁻¹ |
| 6.0 | 45660 | 2.5×10⁻¹ |
| 10.0 | 76100 | 2.6×10⁻¹ |

The impulse rises as n_Q ∝ r₃² through the entire perturbative regime (the ratio n_Q/r₃² ≈ 2.9×10⁻⁴ is
constant), and **saturates only at r₃ ∼ 6–10 (m₃/H ∼ 5×10⁴–10⁵)** — it does *not* peak near the
benchmark.

## 3. The verdict

- **The benchmark** is r₃ = 2.4×10⁻⁴ (m₃/H = 1.84 with ω_w/H = 7.6×10³) — deep in the monotonic n_Q ∝ r₃²
  tail. **There is no extremum there.** A stationarity principle has nothing to pin.
- **MaxEP would select** the efficiency maximum, r₃ ∼ O(few)–10, i.e. **m₃/H ∼ 10⁴–10⁵** — a factor
  ∼4×10⁴ above the benchmark. Since η_B ∝ n_Q ∝ r₃², MaxEP would overproduce the asymmetry by
  ∼(10⁵/1.84)² ∼ 10⁹. Catastrophic.
- **So MaxEP / stationary entropy production does NOT derive m₃/H.** The efficiency is monotonic at the
  benchmark; the value 1.84 is fixed by matching the *observed, small* η_B, which *requires* the weak
  (perturbative) third harmonic, not the maximal one.

## 4. What it does explain (the consolation)

The negative result is not empty. It shows *why η_B is small* even though it cannot fix the exact value:
- η_B ∝ r₃² ∝ (m₃/ω_w)² is small because the **third harmonic is weak** — c₃ ∼ ε^{n₃} = ε⁴ from the
  Froggatt–Nielsen hierarchy (ε = Λ_H/M = 0.032). Small c₃ is **'t Hooft-natural** (it restores a
  continuous shift symmetry). So the smallness of η_B is a *natural* consequence of the FN structure,
  and m₃/H ∼ O(1) (the harmonic mass ∼ the transition/Hubble scale) is the natural magnitude.
- What is *not* derived is the precise value 1.84 — it is data-selected, the point on the monotonic
  efficiency curve that reproduces η_B^obs. There is no dawn stationarity, and no dusk channel (the
  scales are causally disconnected), that fixes it.

## 5. Consequences for the union

- **η_B remains a fit, not a prediction.** ECCG stays a matched existence proof for the asymmetry's
  *value*; the union does not upgrade this.
- **C4 remains a consistency, not a prediction** (`USC_c1c4_test.md`): ECCG's η_B → ω_b = 0.02226 agrees
  with the CMB at 0.7σ, but because η_B is fitted this is a passed *cross-check* (the arithmetic is
  mutually consistent; a real parameter is removed at Δχ² ≈ 0.5), not a passed prediction. The hoped-for
  promotion via P4 does not happen.
- **The union's genuine hard predictions are unchanged and stand on their own:** Δ = 1 (σ ≈ 0.09,
  DESI DR3 + Euclid) and **m_X = 1.30 GeV** (direct detection — genuine, since Y_B/Y_X = f_B is computed,
  not fitted). The Δ–η_B lock is a *correlation/consistency* (both at their USC values in one fit), not a
  derived value of η_B.
- **The parameter ledger's floor is confirmed exactly:** four cosmological numbers + one postulate
  (Δ = 1) + **one abundance-selected CP number (m₃/H)** + two prescriptions. The CP number does not come
  down; the MaxEP candidate channel is now explicitly closed.

## 6. Honest bottom line

P4 was the one plausible route to make η_B a prediction, and it fails by ∼4×10⁴: the impulse efficiency
is monotonic through the benchmark and maximal ∼10⁵× higher, so no stationarity pins m₃/H — the observed
small η_B forces the weak-third-harmonic (perturbative) regime, whose value is data-selected and whose
smallness is FN-natural. The result is worth reporting precisely: it confirms η_B stays a fit, keeps C4 a
consistency (not a prediction), and leaves Δ = 1 and **m_X ≈ 1.78 GeV** (updated from 1.30; f_B = 28/79) as
the union's hard predictions. **Correction (`USC_CORRECTION_signselection.md` §§9–10): the *sign* is NOT
derived** — the entropy arrow is ℤ₂-even and selects no vacuum; the matter sign is an environmental initial
condition, as ECCG always held. So both sign and magnitude are inputs, not outputs (magnitude a fit, sign a
bit). The refuted "USC-II mechanism paper" is replaced by the Phase-2 domain-problem + no-go-theorems paper.
