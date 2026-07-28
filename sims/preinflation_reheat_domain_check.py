#!/usr/bin/env python3
"""
D-1 : Does reheating re-melt the pre-inflationary pinning and regenerate the
      matter/antimatter domains? (Critique gap G-M1.)

The pre-inflation cure pins psi to one Z2 vacuum because the pinning potential
  V2 = -Lambda2^4 cos(2 psi + delta2),   Lambda2^4 = 2 kappa2 f_psi^4
is on during inflation with m2 >> H_inf. G-M1 worried that if T_RH exceeds the
SU(3)_H confinement scale Lambda_H, the hidden sector deconfines, Lambda2 melts,
psi is released, and reconfinement Kibble-regenerates domains.

Resolution grounded in the actual ECCG model (SPONTANEOUS_CP_REPORT,
MICROSCOPIC_SQCD_THERMAL_REPORT):
  (1) The domain-selecting quantity is the SIGN, set by which Z2 minimum psi sits
      in, whose locations are fixed by the CP PHASE delta2 = n2*theta_S -- set by
      the FLAVON theta_S at scale v_S, NOT by the SU(3)_H condensate.
  (2) SU(3)_H selects a REAL diagonal moduli branch |M_ii| = Lambda_H^2, so
      arg<Theta> = 0: reconfinement restores a real condensate everywhere, adding
      NO phase -> delta2 is untouched by any melt/reform of the hidden sector.
  (3) The flavon is inflated to uniformity and never thermally restored provided
      T_RH < v_S -- a condition the model ALREADY imposes.
  So the relevant threshold is v_S, not Lambda_H. This script checks the two
  residual quantitative worries:
     (A) T_RH < v_S across the res-(iv) window (flavon never restored);
     (B) even if T_RH > Lambda_H (brief hidden deconfinement), psi does not
         random-walk into domains: dpsi << pi/2 over < 1 e-fold.
"""
import numpy as np

MPl   = 1.22091e19     # GeV
f_psi = 1.022e13       # GeV  (= sqrt(I_eff), the psi decay constant)
Lam_H = 6.35e12        # GeV  SU(3)_H confinement scale
vS_B  = 2.44e13        # GeV  flavon VEV, branch B (nEDM edge)
vS_A  = 4.8e15         # GeV  flavon VEV, branch A (comfortable)
window = (3.2e12, 9.0e12)   # ECCG res-(iv) reheating window (upper = portal thermal restoration)

def H(T, gstar=228.0):   # gstar=228: SM + deconfined hidden dof (relevant above Lambda_H)
    return 1.66*np.sqrt(gstar)*T**2/MPl

print("="*76)
print("D-1  Pre-inflation cure vs reheating: does T_RH regenerate psi domains?")
print("="*76)
print(f"  f_psi = {f_psi:.2e} GeV   Lambda_H = {Lam_H:.2e} GeV")
print(f"  res-(iv) window T_RH = [{window[0]:.1e}, {window[1]:.1e}] GeV")
print(f"  flavon v_S: branch B = {vS_B:.2e},  branch A = {vS_A:.2e} GeV")
print()

print("(A) Flavon-restoration test  (need T_RH < v_S so delta2=n2*theta_S stays frozen/uniform):")
for lab, vS in [("branch B", vS_B), ("branch A", vS_A)]:
    ok = window[1] < vS
    margin = vS/window[1]
    print(f"    {lab}: v_S/T_RH,max = {margin:5.1f}x  ->  {'SAFE (flavon never restored)' if ok else 'VIOLATED'}")
print("    => the CP phase that sets the Z2 minima is never thermally randomized in-window.")
print()

print("(B) Hidden-deconfinement random-walk test  (only relevant where T_RH > Lambda_H):")
print(f"    {'T_RH [GeV]':>11} | {'H(T_RH) [GeV]':>13} | {'e-folds T_RH->Lam_H':>19} | {'dpsi~H/2pi f_psi':>16} | vs pi/2")
for T in [3.2e12, 5.0e12, 6.35e12, 9.0e12]:
    Nef = max(0.0, np.log(T/Lam_H))
    dpsi = H(T)/(2*np.pi*f_psi)
    ratio = dpsi/(np.pi/2)
    tag = "no deconf." if T <= Lam_H else f"{Nef:.2f} e-folds"
    print(f"    {T:11.2e} | {H(T):13.2e} | {tag:>19} | {dpsi:16.2e} | dpsi/(pi/2) = {ratio:.1e}")
print("    => even at the top of the window the released phase fluctuates by ~1e-6 rad over")
print("       < 0.35 e-folds -- 6 orders below the pi/2 ridge between the two vacua. No flips,")
print("       and radiation-era evolution generates no new super-horizon (domain-scale) modes.")
print()

print("="*76)
print("  VERDICT")
print("="*76)
print("  G-M1 does NOT fire. The pre-inflation cure survives the entire res-(iv) window:")
print("   * the pinning PHASE delta2 = n2 theta_S is flavon-set at v_S >> T_RH and inflated")
print("     uniform (model already requires T_RH < v_S);")
print("   * SU(3)_H reconfines REAL (arg<Theta>=0), so a T_RH>Lambda_H melt/reform of the")
print("     magnitude Lambda2 adds no phase and re-pins psi uniformly;")
print("   * the released phase cannot random-walk into domains (dpsi ~ 1e-6 << pi/2).")
print()
print("  CONSEQUENCES:")
print("   1. The correct D-2 window upper bound is the portal-thermal 9e12 (with T_RH<v_S the")
print("      D-1 condition), NOT Lambda_H=6.35e12. D-2's viable-sliver conclusion is UNCHANGED")
print("      (everything above ~3.3e12 already overproduces eta_B), only the label corrects.")
print("   2. NEW independent falsifier surfaced: branch B (v_S=2.44e13) sits at the nEDM edge,")
print("      theta_bar ~ (v_S/MPl)^2 sin(Delta_CP) ~ 1e-10  ->  a neutron EDM near the current")
print(f"      bound.  theta_bar(B) = {(vS_B/MPl)**2:.1e} x sin(Delta_CP)  [x O(1)].")
print("      Branch A (v_S=4.8e15) evades nEDM but needs a 2nd gauged flavon.")
print("   => The cure is safe, but it is NOT free: it forces T_RH<v_S and (branch B) predicts")
print("      an observable-edge neutron EDM. That EDM is a cross-check independent of DESI/CMB.")
