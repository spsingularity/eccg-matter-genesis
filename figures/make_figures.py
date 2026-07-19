#!/usr/bin/env python3
"""Figures for Paper VII (ECCG matter genesis). Numbers are the committed results:
f_B=28/79 (SM sphaleron), m_X~1.78 GeV, Candidate C -> NO + Sigma m_nu 59-64 meV,
T_RH~3.3e12 GeV, eta_B=6.1e-10 (from D2_result_candidateC_neutrino.md)."""
import numpy as np, os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = os.path.join(os.path.dirname(__file__), "..", "paper", "figures")
os.makedirs(OUT, exist_ok=True)

# ---- Fig 1: co-genesis mechanism schematic ----
def fig_mechanism():
    fig, ax = plt.subplots(figsize=(8.6, 4.4)); ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
    def box(x, y, w, h, t, c, fc, fs=9):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04,rounding_size=0.10",
                     lw=1.7, edgecolor=c, facecolor=fc)); ax.text(x+w/2, y+h/2, t, ha="center", va="center", fontsize=fs)
    def arr(x1, y1, x2, y2, c="0.4"):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=14, lw=1.4, color=c))
    box(3.4, 5.0, 3.2, 0.8, "SU(3)$_H$ counter-rotating\ncondensates ($Q_V=-Q_D$)", "#2c3e50", "#ecf0f1")
    box(0.3, 3.0, 3.0, 1.0, "visible sector:\n$B{-}L$ asymmetry\n$\\to$ baryons", "#c0392b", "#fdedec", 8.5)
    box(6.7, 3.0, 3.0, 1.0, "dark sector:\nasymmetric DM\n$m_X\\approx1.78$ GeV", "#8e44ad", "#f5eef8", 8.5)
    arr(4.4, 5.0, 2.0, 4.0, "#c0392b"); arr(5.6, 5.0, 8.0, 4.0, "#8e44ad")
    box(0.3, 1.4, 3.0, 0.85, "SM sphaleron\n$f_B=28/79$  [CALCULATED]", "#27ae60", "#eafaf1", 8.5)
    arr(1.8, 3.0, 1.8, 2.25, "#27ae60")
    box(6.7, 1.4, 3.0, 0.85, "shared asymmetry fixes\n$\\Omega_{\\rm DM}/\\Omega_b$  [MATCHED]", "#7f8c8d", "#f4f6f6", 8.5)
    arr(8.2, 3.0, 8.2, 2.25, "#7f8c8d")
    box(2.5, 0.15, 5.0, 0.75, "clock is a Sakharov diagnostic here — it does NOT source matter ($R_0=0$)",
        "#e67e22", "#fef5e7", 8.2)
    ax.set_title("Counter-rotating co-genesis: one asymmetry, two sectors", fontsize=11)
    fig.tight_layout(); p = f"{OUT}/fig1_mechanism.png"; fig.savefig(p, dpi=170); plt.close(fig); print("wrote", p)

# ---- Fig 2: the Candidate-C neutrino squeeze ----
def fig_candidateC():
    # eta_B propto T_RH^2 (Sum m_nu)^2 ; fixed eta_B=6.1e-10 -> T_RH propto 1/Sum m_nu.
    smnu = np.linspace(40, 90, 300)                  # meV
    # normalise so the curve passes (Sum=61.5 meV, T_RH=3.3e12 GeV)
    TRH = 3.3e12 * (61.5/smnu)
    fig, ax = plt.subplots(figsize=(6.8, 4.4))
    ax.plot(smnu, TRH, color="#2c3e50", lw=2.2, label=r"$\eta_B=6.1\times10^{-10}$ (Candidate C)")
    # NH floor and DESI ceiling
    ax.axvspan(40, 58, color="#c0392b", alpha=0.10); ax.text(48, 5.2e12, "IO / below NH floor\n(excluded)", color="#c0392b", fontsize=8, ha="center")
    ax.axvspan(64, 90, color="#7f8c8d", alpha=0.10); ax.text(77, 5.2e12, "above DESI\nceiling", color="#555", fontsize=8, ha="center")
    ax.axvspan(58, 64, color="#27ae60", alpha=0.12)
    ax.axvline(58, color="#c0392b", lw=1.0, ls="--"); ax.axvline(64, color="#7f8c8d", lw=1.0, ls="--")
    ax.scatter([61.5], [3.3e12], s=90, color="#27ae60", zorder=6)
    ax.annotate("surviving sliver:\nNO, $\\Sigma m_\\nu\\approx59$–$64$ meV,\n$T_{\\rm RH}\\approx3.3\\times10^{12}$ GeV",
                (61.5, 3.3e12), (66, 2.4e12), fontsize=8.3, color="#27ae60")
    ax.set(xlabel=r"$\Sigma m_\nu$  [meV]", ylabel=r"$T_{\rm RH}$  [GeV]",
           title="Candidate C ties baryogenesis to the neutrino masses",
           xlim=(40, 90), ylim=(1.5e12, 6e12))
    ax.legend(fontsize=8.5, loc="lower left")
    fig.tight_layout(); p = f"{OUT}/fig2_candidateC.png"; fig.savefig(p, dpi=170); plt.close(fig); print("wrote", p)

if __name__ == "__main__":
    fig_mechanism(); fig_candidateC()
