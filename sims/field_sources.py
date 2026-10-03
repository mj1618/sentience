"""Scenario 12: if sentience were a field, what would be its source?

A field in physics is sourced by the local density of some quantity, added up
over space. For each candidate quantity we ask: how much of it is in a brain,
and how much in things nobody thinks are sentient? And for a long-range field,
whose contribution dominates at the location of your own head (source / distance)?

All inputs are order-of-magnitude and listed here so they can be attacked.
"""
import json
from pathlib import Path

OUT = Path(__file__).parent / "out"

# name: (mass kg, power dissipated W, electric-field energy stored J,
#        irreversible switching events per s, distance from a head in m)
SYSTEMS = {
    "own brain":            (1.4,    20.0,   0.6,    1e15, 0.05),
    "own liver":            (1.5,    25.0,   0.5,    0.0,  0.4),
    "laptop CPU":           (0.05,   30.0,   1e-3,   1e18, 0.5),
    "phone battery/caps":   (0.05,   2.0,    10.0,   1e16, 0.3),
    "kettle (boiling)":     (1.5,    2000.0, 0.0,    0.0,  2.0),
    "car engine":           (150.0,  5e4,    0.0,    0.0,  10.0),
    "data centre":          (1e6,    3e7,    1e4,    1e23, 1e4),
    "Earth":                (5.97e24, 4.7e13, 0.0,   0.0,  6.4e6),
    "Sun":                  (1.99e30, 3.8e26, 0.0,   0.0,  1.5e11),
}
QUANTITIES = ["mass", "dissipation (W)", "E-field energy (J)", "switching events (/s)"]

# Notes on inputs (all rough):
#  brain E-field energy: membrane area ~2.5e4 m^2 x 1e-2 F/m^2 -> 250 F at 70 mV -> 0.6 J
#  brain switching events: 1e11 neurons x ~1 Hz x 1e4 synapses
#  CPU: 1e10 transistors x 1e9 Hz x 10% activity
#  Earth dissipation: internal heat flow 47 TW; Sun: luminosity


def main():
    rows = []
    brain = SYSTEMS["own brain"]
    for name, vals in SYSTEMS.items():
        *q, r = vals
        row = {"system": name}
        for label, x, b in zip(QUANTITIES, q, brain[:4]):
            row[label + " vs brain"] = x / b if b else None
            # contribution to a long-range field at the head, relative to the brain's own
            row[label + " at head vs brain"] = (x / r) / (b / brain[4]) if b else None
        rows.append(row)
    w = max(len(n) for n in SYSTEMS)
    print("Amount relative to one brain")
    print(f"{'':{w}}  " + "  ".join(f"{q:>22}" for q in QUANTITIES))
    for row in rows:
        print(f"{row['system']:{w}}  " + "  ".join(f"{row[q + ' vs brain']:22.1e}" for q in QUANTITIES))
    print("\nLong-range field strength at your head, relative to your own brain's contribution")
    for row in rows:
        print(f"{row['system']:{w}}  " + "  ".join(f"{row[q + ' at head vs brain']:22.1e}" for q in QUANTITIES))
    (OUT / "field_sources.json").write_text(json.dumps(rows, indent=1))


if __name__ == "__main__":
    main()
