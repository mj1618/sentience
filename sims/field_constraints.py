"""Scenario 2: could sentience be a new field that acts on neurons?

For a new force to matter to a neuron it has to change the energy of some
switch (an ion channel) by an amount comparable to thermal noise, kT.
We compute the coupling that would need and compare with what experiments
already exclude. Bounds are order-of-magnitude; sources in
research/02-physics-constraints.md.
"""
import json
from pathlib import Path

import numpy as np

OUT = Path(__file__).parent / "out"
OUT.mkdir(exist_ok=True)

G = 6.674e-11            # m^3 kg^-1 s^-2
HBARC_EV_M = 1.9733e-7   # eV m
KB = 1.380649e-23
T_BODY = 310.0
KT = KB * T_BODY         # J
KT_EV = KT / 1.602e-19
ALPHA_EM = 1 / 137.036

RHO = 1000.0             # kg/m^3, tissue
M_BRAIN = 1.4            # kg
M_CHANNEL = 250e3 * 1.6605e-27   # 250 kDa ion channel
GATING_MOVE = 1e-9       # m, distance a voltage sensor moves

# Upper limits on Yukawa strength alpha (relative to gravity) at range lam.
# Order-of-magnitude; provenance per row in research/02-physics-constraints.md.
ALPHA_BOUND = {
    1e-9: 1e22,    # neutron-Xe scattering (Kamiya 2015), converted from g^2
    1e-8: 1e20,    # neutron / lateral Casimir, read off review figure
    1e-7: 1e11,    # IUPUI Casimir-less (Chen/Decca 2016), read off figure
    1e-6: 1e7,     # same
    1e-5: 1.4e4,   # Stanford cantilever (Geraci 2008), exact
    1e-4: 1e-1,    # Eot-Wash; unsourced guess (alpha=1 at 38.6 um, Lee 2020, is exact)
    1e-3: 1e-3,    # HUST, via review
    1e-2: 2e-4,    # Irvine (Spero), via review
    1e-1: 1e-3,    # Irvine (Hoskins), via review
    1e0: 5e-4,     # Moody & Paik, via review
}

# Stellar cooling caps any light (m << keV, i.e. range >> 0.2 nm) scalar coupled to
# nucleons at g_N < 1.1e-12, which is alpha ~ 1.7e13 (Hardy & Lasenby 2017).
ALPHA_STELLAR = 1.7e13

SCALES = {1e-9: "protein", 1e-8: "synaptic cleft", 1e-7: "synapse", 1e-6: "dendrite width",
          1e-5: "neuron body", 1e-4: "cortical column", 1e-3: "cortical thickness",
          1e-2: "brain region", 1e-1: "whole brain", 1e0: "beyond the head"}


def mass_coupled():
    rows = []
    for lam, lab in ALPHA_BOUND.items():
        bound = min(lab, ALPHA_STELLAR)
        m_src = min(RHO * 4 / 3 * np.pi * lam ** 3, M_BRAIN)
        # generous: count the entire potential energy as usable
        e_generous = G * m_src * M_CHANNEL / lam
        # realistic: work done by the force over the gating movement
        e_real = e_generous * min(GATING_MOVE / lam, 1.0)
        need_gen = 0.01 * KT / e_generous     # alpha needed for a 1%-of-kT nudge
        need_real = KT / e_real               # alpha needed for a kT nudge
        # most generous imaginable (red-team round 2): every channel event within reach
        # is nudged the helpful way and the brain pools them all, as Scenario 4 grants a
        # chooser. Energy shift dE biases an open/closed event by dE/4kT; pooling N events
        # needs bias 0.24/sqrt(N). A mass-sourced force cannot be patterned like this.
        n_pool = max(1.0, 1e15 * min(1.0, (lam / 0.07) ** 3))
        need_pooled = (0.95 / np.sqrt(n_pool)) * KT / e_generous
        rows.append({
            "range_m": lam, "scale": SCALES[lam],
            "quantum_mass_eV": HBARC_EV_M / lam,
            "thermally_excitable": bool(HBARC_EV_M / lam < KT_EV),
            "alpha_needed_generous": need_gen, "alpha_needed_realistic": need_real,
            "alpha_allowed": bound, "alpha_needed_pooled": need_pooled,
            "shortfall_orders_pooled": float(np.log10(need_pooled / bound)),
            "shortfall_orders_generous": float(np.log10(need_gen / bound)),
            "shortfall_orders_realistic": float(np.log10(need_real / bound)),
        })
    return rows


def electron_coupled(g_e=7e-16, n_coherent=None):
    """Light scalar coupled to electrons with coupling g_e (stellar-cooling limit).
    Returns the largest energy shift on one ion channel if EVERY electron in the
    brain pulled coherently in the same direction (wildly generous)."""
    electrons_per_kg = 0.55 / 1.6605e-27      # ~0.55 electrons per nucleon in tissue
    n_src = M_BRAIN * electrons_per_kg if n_coherent is None else n_coherent
    n_tgt = M_CHANNEL * electrons_per_kg
    R = 0.05
    per_pair_eV = g_e ** 2 / (4 * np.pi) * HBARC_EV_M / R
    total_eV = per_pair_eV * n_src * n_tgt
    return {"g_e": g_e, "ratio_to_coulomb": g_e ** 2 / (4 * np.pi * ALPHA_EM),
            "energy_on_channel_eV": total_eV, "in_kT": total_eV / KT_EV}


if __name__ == "__main__":
    print(f"kT at body temperature = {KT_EV*1e3:.1f} meV; "
          f"thermal range hbar*c/kT = {HBARC_EV_M/KT_EV*1e6:.1f} um\n")
    rows = mass_coupled()
    print(f"{'range':>8} {'scale':<18}{'quantum mass':>13} {'need(gen)':>10} {'need(real)':>11} "
          f"{'allowed':>8} {'short(gen)':>10} {'short(real)':>11}")
    for r in rows:
        print(f"{r['range_m']:8.0e} {r['scale']:<18}{r['quantum_mass_eV']:11.1e}eV "
              f"{r['alpha_needed_generous']:10.1e} {r['alpha_needed_realistic']:11.1e} "
              f"{r['alpha_allowed']:8.0e} {r['shortfall_orders_generous']:10.1f} "
              f"{r['shortfall_orders_realistic']:11.1f}  pooled:{r['shortfall_orders_pooled']:5.1f}")
    ec = electron_coupled()
    print("\nelectron-coupled light scalar at stellar-cooling limit:", ec)
    (OUT / "field_constraints.json").write_text(
        json.dumps({"mass_coupled": rows, "electron_coupled": ec}, indent=1))
