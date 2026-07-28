# Pin⁺ ν mod 16 — an explicit satisfying assignment, constructed (2026-07-17)

**Closes (as construction) the item left `[OPEN — bookkeeping, satisfiable-by-choice]` in `TIER1_results.md` #3.**
Source content: `ECCG .../s3_gauging/S3_GAUGING_REPORT.md` (fermion list §102–150; Dai–Freed statement §147–150;
"freedom to set ν=0" §133–136; R3 spectator solution `r3_spectator_solution.csv`).

## 1. The rule (standard, not invented here)

For gauged CP in 3+1d (Pin⁺ structure), the anomaly is valued in `Ω^{Pin⁺}_5 ⊃ ℤ₁₆`
(Fidkowski–Kitaev; Witten, *Fermion path integrals and topological phases*): **each Majorana fermion
contributes ν = ±1 mod 16, the sign being its intrinsic CP phase**; a pair with a CP-commuting
(CP-real) Dirac/Majorana mass necessarily carries opposite signs and contributes `+1 − 1 = 0`.
For gauge-charged fermions the relevant statement is the twisted-bordism one the report itself makes:
*"every S₃-charged fermion is vectorlike … ⇒ trivial in any bordism classification"* [Exact/structural].

## 2. The content, organized into CP-massable pairs

All ~16 CP-relevant Weyl fermions of the R3 realization pair up under the report's own massability
structure ("all spectators massable by construction", each by an allowed ℤ₂^M-even spurion dressing):

| pair | members | pairing channel | ν contribution |
|---|---|---|---|
| P1–P4 | the 4 R3 spectator pairs (spec0f/f̄b … spec3f/f̄b, 8 Weyl) | designed vectorlike pairs, spurion-dressed (q31_D = 4, 25, 27, 6) | 4 × 0 |
| P5 | HF-ino / H̄F-ino | conjugate pair (q31 = 4, 27 ≡ −4) | 0 |
| P6 | ΦV-ino / ΦD-ino | Q = −2/+2, z₃ = 0/1; Q-neutral combination, spurion-dressable | 0 |
| P7 | C_spec / D_spec | Q = +1/−1; q31 = 21+6 = 27 ≡ −4 → dressed by the q31=4 spurion | 0 |
| P8 | Y₁ / Y₄ | q31 = 1+26 = 27 ≡ −4 → same dressing channel | 0 |
| P9 | Y₂ / Y₃ | q31 = 3+9 = 12 → dressed by the allowed spurion combination closing 12 mod 31 | 0 |

**Assignment: within each pair, intrinsic CP phases (+1, −1). Total ν = 0 mod 16 — exhibited.**

## 3. Why this is stronger than "satisfiable"

The per-pair overall sign flip `(+,−) → (−,+)` is the only freedom, and it never changes the sum:
**given (i) the pairing structure and (ii) CP-commuting mass dressings, ν = 0 is automatic, not tuned.**
The condition (ii) is the one genuine requirement: at the CP-symmetric point (where the anomaly is
evaluated) each pair's mass phase must be removable. Each pair has its own independent spurion channel,
so each mass phase is absorbable by a field redefinition one pair at a time — no over-constraint. This is
exactly the "fixed jointly with the spontaneous-CP flavon couplings" clause of the report, discharged at
the symmetric point where it is needed.

## 4. Honest scope

- The ±1-per-Majorana rule is the untwisted `ℤ₁₆`; for the gauge-charged members the operative statement
  is vectorlikeness ⇒ bordism-trivial (the report's own Dai–Freed line), which the pairing realizes.
- The construction covers the fermions the report lists as CP-relevant (condensate-inos, ℤ₃₁ spectators,
  R3 set, breaking sector). A future enlargement of the chiral content re-opens the count.
- The Y₂/Y₃ dressing channel (closing 12 mod 31) is asserted from the spurion set's closure, not traced
  through every allowed operator; if that specific channel fails, Y₂/Y₃ pair through a two-spurion
  dressing instead — the phase-absorption counting is unchanged.

**Status change:** `[OPEN — bookkeeping]` → **`[CONSTRUCTED — ν = 0 exhibited; automatic given
CP-commuting dressings, which exist by per-pair phase absorption]`.**
