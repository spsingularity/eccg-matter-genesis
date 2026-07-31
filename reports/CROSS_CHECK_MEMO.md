# Cross-check: two independent ECCG codebases

*Provenance: this work is sole-authored. "Track A" and "Track B" below are two independent
codebases the author developed separately — different solvers, different friction treatments,
different normalizations — and then compared without reconciling them first. No other person
contributed. The value of the comparison is that the two implementations were built
independently, not that different people built them.*

An independent comparison. The two tracks **agree on every structural prediction and key
relation**, and **disagree only in the transition/bubble-wall sector** — exactly the part both
independently flag as "benchmark, not precision." One discrepancy (beta/H) is most likely a bug
already found and fixed in Track B.

---

## Strong agreements (mutual validation)

| Quantity | Track A | Track B | |
|---|---|---|---|
| Q_visible = -Q_dark (equal & opposite) | structural | structural | AGREE |
| R_tr = Y_B/Y_X | 0.2636 | 0.2635 (transport) | AGREE |
| m_X | 1.33 GeV | 1.3255 GeV | AGREE |
| **eta_3 = epsilon_H eta_2** | predicted | predicted (Z_2 chain parity) | **AGREE** (independent) |
| T_n | 3.17e12 GeV | 3.17e12 GeV | AGREE |
| phi/T (r_phi) | 3.43 | 3.34-3.76 | AGREE (~10%) |
| CP checks q(0)=0, q(-d)=-q(d) | verified | verified | AGREE |

Two independent codebases converging on the equal-and-opposite charge, R_tr, m_X, and especially
**eta_3 = epsilon eta_2** (which the Track B flavor-model Z_2 parity derives from scratch) is a
genuine validation of the core mechanism.

**Both audits also independently found** that the quoted eta_B was obtained by **rescaling a
hardcoded abundance**, not recomputed from the full source/collision/washout chain. Independent
confirmation of the same shortcut — and of the honest conclusion that eta_B is not yet robustly
predicted.

## Discrepancies (ranked by actionability)

### 1. beta/H: Track A 661 vs Track B ~390 (+/-20%). LIKELY A BUG ALREADY FIXED.
1.69x apart — outside the Track B robustness band [312, 468]. The numerical-robustness study
found the shipped **bounce solver silently returns spurious LARGE actions ~27% of the time**, and
beta/H = d(S3/T)/dlnT is a derivative of the action curve, so a single spurious-high point
inflates it. **661 is consistent with un-cleaned solver output.** Recommendation: apply outlier
rejection + a smooth global fit to the action curve before differentiating (`numerical_robustness/`
has the fix and gives 3.9(4)e2). This is the single most actionable cross-check.

### 2. v_w: Track A 0.174 [0.088, 0.334] vs Track B 0.58 +/- 0.09. GENUINE MODEL DIFFERENCE.
Factor ~3.4. Track A's relaxation-time friction gives a slow wall; Track B's Bodeker-Moore +
hydrodynamics gives a fast one and finds **LTE has NO steady solution** and that at v_w = 0.3
friction balances only **36%** of the driving — so v_w must be *higher*, not lower. Track A's
0.174 is in direct tension with the Track B exclusion of v_w = 0.3. Recommendation: compare the
friction pressure at a common v_w; the relaxation-time approximation tends to overestimate
friction (underestimate v_w).

### 3. eta_B differs by ~2x — but it is DOWNSTREAM of (1) and (2).
eta_B ~ 1/(v_w * beta/H). Track A (v_w=0.17, beta/H=661) vs Track B (0.58, 390) gives Track A's
eta_B ~2.0x Track B's — the slower wall boosts, the higher beta/H cuts, net ~2x. **The eta_B
discrepancy is not independent**: resolving beta/H and v_w resolves it.

### 4. Smaller / likely definitional
- **L_w T: 4.37 vs 8.44** (~2x) — probably a wall-thickness convention (10-90% vs 1/e, or L_w vs
  2L_w). Align definitions.
- **alpha: 0.063 vs 0.055 (Track B DR), 0.0275 (trace-anomaly/hydro)** — ~15%; likely the alpha
  definition (Delta e/rho vs the trace anomaly used in the bag EoS). Align.
- **delta_CP: pi/3 (Track A geometric phase) vs pi/2 (Track B spontaneous CP)** — a real
  *mechanism* difference, not a bug; both tracks flag it as "not yet blind."

### 5. m_X interpretation: 1.33 (f_sph = 0.744 kept) vs the Track B mediator -> 1.78 (f_sph -> 1)
R_tr = 0.2636 = 0.744 x (28/79). The 0.744 is the sphaleron-timing fraction of the 4-body
transfer. The Track B analysis argues a *renormalizable 2-body mediator* completes the transfer
before sphaleron freeze-out (f_sph -> 1), pushing m_X toward 1.78 GeV. Both are conditional on the
(unfinished) mediator dynamics; worth reconciling once the messenger completion is fixed.

## Assessment

- **The robust physics agrees** across two independent implementations (charge structure, R_tr,
  m_X, eta_3 = epsilon eta_2, T_n, the CP checks, the honest meta-status).
- **The disagreements are confined to the transition/wall sector** (beta/H, v_w, L_w, alpha) —
  precisely where both tracks flag "not precision." This is the expected and reassuring pattern:
  the controlled results converge, the least-controlled ones diverge.
- **Highest-value action:** reconcile beta/H — the robustness work strongly suggests 661 includes
  solver-failure artifacts, and the fix is in hand. After that, the friction/v_w normalization is
  the main genuine physics difference, and it (via eta_B ~ 1/(v_w beta/H)) accounts for
  essentially all of the ~2x eta_B difference.
- Both tracks reach the **same honest bottom line**: a compelling common cogenesis mechanism with
  several quantitative relations, but not yet a precision, fully-independent prediction of the
  matter abundance.
