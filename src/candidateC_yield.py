#!/usr/bin/env python3
"""
Candidate C — spontaneous (quintessential) baryogenesis on a genuine non-compact
B-L current, driven by the Ledger Field's clock rate theta_dot_r = H*D_E, with the
dusk-fixed invariant mu = c*theta_dot = H/(2 pi)  (c*D_E = 1/2pi, USC_crossscale.md).

Mechanism (Cohen-Kaplan / De Simone-Kobayashi):
  L  ⊃  c ∂_mu θ · J^mu_{B-L}   →  chemical potential  mu(T) = c θ̇ = H(T)/2π
  B-L violation: Weinberg operator (LL)(HH), coefficient fixed by observed m_nu
     Γ_W(T) = C_W * T^3 * mbar^2 / v^4 ,  mbar^2 = Σ m_i^2
  Equilibrium bias:  Y_eq = (15 g_chi /(4 π^2 g_*)) * (mu/T)   [g_chi = susceptibility dof]
  Two branches:
    STRONG washout (T_RH > T_d where Γ_W = H):  Y_{B-L} = Y_eq(T_d)  (freeze-OUT)
    WEAK  washout (T_RH < T_d):                Y_{B-L} ≈ 1/2 (Γ_W/H) Y_eq |_{T_RH}  (freeze-IN, UV-dominated)
  Sphalerons: Y_B = (28/79) Y_{B-L}
"""
import numpy as np

# ---------- constants ----------
MPl   = 1.22091e19          # GeV
v     = 174.0               # GeV (Higgs vev / sqrt2 convention for Weinberg op)
eta_B = 6.10e-10
YB_obs = eta_B/7.04         # n_B/s
f_sph = 28.0/79.0
YBL_needed = YB_obs/f_sph

# neutrino mass scale (oscillation floor, normal hierarchy):
dm2_atm, dm2_sol = 2.50e-3, 7.4e-5      # eV^2
mbar2_NH  = dm2_atm + dm2_sol            # Σ m_i^2, m_lightest -> 0  [eV^2]
mbar2_IH  = 2*dm2_atm + dm2_sol
GeV = 1e-9  # eV -> GeV
def mbar2_GeV(mbar2_eV2): return mbar2_eV2*GeV**2

def H(T, gstar): return 1.66*np.sqrt(gstar)*T**2/MPl
def mu_of_T(T, gstar): return H(T, gstar)/(2*np.pi)          # the dusk-fixed tilt = T_AH
def Gamma_W(T, mbar2, C_W): return C_W*T**3*mbar2_GeV(mbar2)/v**4
def Yeq(T, gstar, g_chi): return (15.0*g_chi/(4*np.pi**2*gstar))*mu_of_T(T,gstar)/T

def T_dec(mbar2, C_W, gstar):
    """Γ_W = H  →  decoupling temp of ΔL=2 washout."""
    return 1.66*np.sqrt(gstar)*v**4/(C_W*mbar2_GeV(mbar2)*MPl)

def Y_BL_strong(mbar2, C_W, gstar, g_chi):
    Td = T_dec(mbar2, C_W, gstar)
    return Yeq(Td, gstar, g_chi), Td

def Y_BL_weak(TRH, mbar2, C_W, gstar, g_chi):
    """freeze-in, integrand ∝ T^2 → 1/2 (Γ/H) Y_eq at T_RH; mild washout e^{-Γ/H/1}≈ ignore (O(20%))."""
    return 0.5*(Gamma_W(TRH,mbar2,C_W)/H(TRH,gstar))*Yeq(TRH,gstar,g_chi)

# ---------- central conventions ----------
C_W0, gstar0, g_chi0 = 1/np.pi**3, 106.75, 1.0

print("="*78)
print("0. Sanity anchors")
print(f"   Y_B needed = {YB_obs:.3e}   Y_(B-L) needed = {YBL_needed:.3e}")
Tn = 3.17e12
print(f"   H(T_n=3.17e12) = {H(Tn,gstar0):.3e} GeV  (ECCG: 1.48e7)   mu = {mu_of_T(Tn,gstar0):.3e} (crossscale: 2.36e6)")
print(f"   mu/T at T_n = {mu_of_T(Tn,gstar0)/Tn:.2e}  (corpus: 7.4e-7)")
print(f"   Gamma_W/H at T=2.5e9 (ECCG f_B washout epoch) = {Gamma_W(2.5e9,mbar2_NH,C_W0)/H(2.5e9,gstar0):.1e}  (ECCG integrates ΔL=2 washout to 4e-5 -> consistent)")

print("="*78)
print("1. STRONG-washout branch (T_RH above ΔL=2 equilibration): freeze-out at T_d")
for mbar2,lab in [(mbar2_NH,'NH floor'),(mbar2_IH,'IH floor'),(4.8e-3,'Σm=0.12eV degen')]:
    Y,Td = Y_BL_strong(mbar2, C_W0, gstar0, g_chi0)
    print(f"   {lab:16s} mbar2={mbar2:.2e} eV^2  T_d={Td:.2e} GeV  Y_BL={Y:.2e}  overproduce x{Y/YBL_needed:.0f}")
# required T_d to match:
# Y_eq(T) = A*T with A = (15 g_chi/(4 pi^2 g*)) * 1.66 sqrt(g*)/(2 pi MPl)
A = (15*g_chi0/(4*np.pi**2*gstar0))*1.66*np.sqrt(gstar0)/(2*np.pi*MPl)
Td_req = YBL_needed/A
mbar2_req = 1.66*np.sqrt(gstar0)*v**4/(C_W0*Td_req*MPl)/GeV**2
print(f"   -> required T_d = {Td_req:.2e} GeV  -> required mbar2 = {mbar2_req:.2e} eV^2 "
      f"(= Σm_ν ~ {3*np.sqrt(mbar2_req/3):.2f} eV degenerate)  [EXCLUDED by Σm_ν<0.07-0.12 eV]")

print("="*78)
print("2. WEAK-washout branch (T_RH < T_d): freeze-in, Y ∝ T_RH^2 · mbar^2")
Td_NH = T_dec(mbar2_NH, C_W0, gstar0)
print(f"   T_d(NH floor) = {Td_NH:.2e} GeV  -> weak branch iff T_RH < this")
for TRH in [1e12, 2e12, Tn, 5e12, 9e12, 1.5e13]:
    Y = Y_BL_weak(TRH, mbar2_NH, C_W0, gstar0, g_chi0)
    print(f"   T_RH={TRH:.2e}  Gam/H={Gamma_W(TRH,mbar2_NH,C_W0)/H(TRH,gstar0):.3f}  "
          f"Y_BL={Y:.2e}  Y_B={f_sph*Y:.2e}  ratio_to_obs={f_sph*Y/YB_obs:.2f}")
# invert for T_RH:
TRH_req = np.sqrt(YBL_needed/Y_BL_weak(1.0, mbar2_NH, C_W0, gstar0, g_chi0))
print(f"   -> REQUIRED T_RH (NH floor, central conventions) = {TRH_req:.3e} GeV")
print(f"      vs ECCG/res-(iv) window (3.2e12, 9.0e12);  ECCG T_n = 3.17e12")

print("="*78)
print("3. Systematics scan on required T_RH  (Y ∝ C_W g_chi g*^{-3/2} T_RH^2 mbar^2)")
rows=[]
for C_W,cl in [(0.01,'C_W=0.01'),(1/np.pi**3,'C_W=1/pi^3'),(0.05,'C_W=0.05')]:
    for g_chi,gl in [(1,'g_chi=1'),(6,'g_chi=6'),(15,'g_chi=15')]:
        for gs,sl in [(106.75,'g*=SM'),(228,'g*=SM+hidden')]:
            T = np.sqrt(YBL_needed/Y_BL_weak(1.0, mbar2_NH, C_W, gs, g_chi))
            rows.append((T,cl,gl,sl))
rows.sort()
for T,cl,gl,sl in rows:
    inwin = "  <-- inside res-(iv) window" if 3.2e12<=T<=9.0e12 else ""
    print(f"   T_RH_req = {T:.2e}  ({cl:11s} {gl:9s} {sl:14s}){inwin}")
print(f"   range: {rows[0][0]:.1e} – {rows[-1][0]:.1e} GeV  (factor {rows[-1][0]/rows[0][0]:.0f} total, i.e. x{np.sqrt(rows[-1][0]/rows[0][0]):.1f} per sqrt)")

print("="*78)
print("4. Hybrid double-counting check: clock channel INSIDE ECCG's own res-(iv) window")
for TRH in [3.2e12, 9.0e12]:
    Y = f_sph*Y_BL_weak(TRH, mbar2_NH, C_W0, gstar0, g_chi0)
    print(f"   T_RH={TRH:.1e}: clock-channel Y_B = {Y:.2e} = {Y/YB_obs*100:.0f}% of observed  (corpus claims '≲2% rider')")

print("="*78)
print("5. Normalization ambiguity (erratum-2 NESS): if the dawn clock were the PLASMA")
print("   modular flow (mu = T/2pi) instead of the entropy clock (mu = H/2pi):")
Y_plasma = (15/(4*np.pi**2*gstar0))*(1/(2*np.pi))   # T-independent equilibrium value
print(f"   Y_eq = {Y_plasma:.2e}  -> overproduces by x{f_sph*Y_plasma/YB_obs:.1e}  (EXCLUDED -> C selects the entropy-clock normalization)")

print("="*78)
print("6. Comparison line: condensate-current version (born pinned, §9/§10): Y ≲ 1e-11 (undershoot x60);")
print("   genuine B-L current at T_RH=T_n: Y_B = %.2e (central) — the pinning penalty is gone."%(f_sph*Y_BL_weak(Tn,mbar2_NH,C_W0,gstar0,g_chi0)))
