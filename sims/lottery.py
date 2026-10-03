"""Scenario 14: does wanting tilt chance? Lottery draws vs number popularity.

Pre-specified in scenarios/14-lottery-test.md: for each game, the fraction of
main-draw balls <= 31 compared with 31/N (and <= 12 vs 12/N), normal
approximation, then pooled across games weighted by number of balls.
Data: New York State open data (data.ny.gov), files in data/.
"""
import csv
import json
from datetime import datetime
from math import sqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# (file, label, columns holding main numbers, how many main balls, [(start, end, N)])
GAMES = [
    ("ny_d6yy-54nr.csv", "Powerball", ["Winning Numbers"], 5,
     [("2010-01-01", "2015-10-06", 59), ("2015-10-07", "2100-01-01", 69)]),
    ("ny_5xaw-6ayf.csv", "Mega Millions", ["Winning Numbers"], 5,
     [("2002-05-17", "2005-06-21", 52), ("2005-06-22", "2013-10-18", 56),
      ("2013-10-19", "2017-10-27", 75), ("2017-10-28", "2100-01-01", 70)]),
    ("ny_6nbc-h7bj.csv", "NY Lotto", ["Winning Numbers"], 6, [("1900-01-01", "2100-01-01", 59)]),
    ("ny_dg63-4siq.csv", "Take 5", ["Evening Winning Numbers", "Midday Winning Numbers"], 5,
     [("1900-01-01", "2100-01-01", 39)]),
    ("ny_kwxv-fwze.csv", "Cash4Life", ["Winning Numbers"], 5, [("1900-01-01", "2100-01-01", 60)]),
]


def analyse():
    rows = []
    for fname, label, cols, k, periods in GAMES:
        for start, end, N in periods:
            s, e = datetime.fromisoformat(start), datetime.fromisoformat(end)
            balls = []
            draws = 0
            with open(DATA / fname) as f:
                for r in csv.DictReader(f):
                    d = datetime.strptime(r["Draw Date"], "%m/%d/%Y")
                    if not (s <= d <= e):
                        continue
                    for c in cols:
                        nums = [int(x) for x in (r.get(c) or "").split()][:k]
                        if len(nums) == k:
                            balls += nums
                            draws += 1
            if not balls:
                continue
            n = len(balls)
            row = {"game": label, "period": f"{start[:4]}–{'now' if end.startswith('2100') else end[:4]}",
                   "N": N, "draws": draws, "balls": n, "max_seen": max(balls)}
            for cut in (31, 12):
                p0 = cut / N
                obs = sum(b <= cut for b in balls) / n
                se = sqrt(p0 * (1 - p0) / n)
                row[f"le{cut}"] = {"expected": p0, "observed": obs, "excess": obs - p0, "se": se,
                                   "z": (obs - p0) / se}
            rows.append(row)
    return rows


def pooled(rows, cut):
    w = sum(r["balls"] for r in rows)
    excess = sum(r["balls"] * r[f"le{cut}"]["excess"] for r in rows) / w
    se = sqrt(sum((r["balls"] * r[f"le{cut}"]["se"]) ** 2 for r in rows)) / w
    return {"excess": excess, "se": se, "z": excess / se, "balls": w}


if __name__ == "__main__":
    rows = analyse()
    for r in rows:
        a, b = r["le31"], r["le12"]
        flag = "" if r["max_seen"] <= r["N"] else "  !! number above N: wrong period boundaries"
        print(f"{r['game']:14s} {r['period']:10s} N={r['N']:2d} draws={r['draws']:6d} max={r['max_seen']:2d}  "
              f"<=31: {a['observed']:.4f} vs {a['expected']:.4f} (z={a['z']:+.2f})  "
              f"<=12: {b['observed']:.4f} vs {b['expected']:.4f} (z={b['z']:+.2f}){flag}")
    out = {"games": rows, "pooled_le31": pooled(rows, 31), "pooled_le12": pooled(rows, 12)}
    for k in ("pooled_le31", "pooled_le12"):
        p = out[k]
        print(f"{k}: excess {p['excess']:+.5f} ± {p['se']:.5f} (z={p['z']:+.2f}) over {p['balls']} balls; "
              f"95% interval {p['excess']-1.96*p['se']:+.4f} to {p['excess']+1.96*p['se']:+.4f}")
    (ROOT / "sims" / "out" / "lottery.json").write_text(json.dumps(out, indent=1))


# ---- Replication sample (pre-specified in scenarios/14, Part 1b): Texas Lottery ----
# Calendar years in which a game's number range changed are dropped, so that
# period boundaries do not need to be known to the day.
TEXAS = [
    ("tx_lottotexas.csv", "Lotto Texas", 6, [(1992, 1999, 50), (2001, 2002, 54), (2007, 2100, 54)]),
    ("tx_lottotexas.csv", "Lotto Texas (5 of 44 era)", 5, [(2004, 2005, 44)]),
    ("tx_cashfive.csv", "Cash Five", 5, [(1995, 2001, 39), (2003, 2017, 37), (2019, 2100, 35)]),
    ("tx_texastwostep.csv", "Texas Two Step", 4, [(2001, 2100, 35)]),
]


def analyse_texas():
    rows = []
    for fname, label, k, periods in TEXAS:
        for y0, y1, N in periods:
            balls, draws = [], 0
            with open(DATA / fname) as f:
                for r in csv.reader(f):
                    if y0 <= int(r[3]) <= y1:
                        balls += [int(x) for x in r[4:4 + k]]
                        draws += 1
            n = len(balls)
            row = {"game": label, "period": f"{y0}–{'now' if y1 == 2100 else y1}", "N": N,
                   "draws": draws, "balls": n, "max_seen": max(balls)}
            for cut in (31, 12):
                p0 = cut / N
                obs = sum(b <= cut for b in balls) / n
                se = sqrt(p0 * (1 - p0) / n)
                row[f"le{cut}"] = {"expected": p0, "observed": obs, "excess": obs - p0, "se": se,
                                   "z": (obs - p0) / se}
            rows.append(row)
    return rows


if __name__ == "__main__":
    print("\nReplication: Texas")
    tx = analyse_texas()
    for r in tx:
        a, b = r["le31"], r["le12"]
        flag = "" if r["max_seen"] <= r["N"] else "  !! number above N"
        print(f"{r['game']:26s} {r['period']:10s} N={r['N']:2d} draws={r['draws']:6d} max={r['max_seen']:2d}  "
              f"<=31: {a['observed']:.4f} vs {a['expected']:.4f} (z={a['z']:+.2f})  "
              f"<=12: {b['observed']:.4f} vs {b['expected']:.4f} (z={b['z']:+.2f}){flag}")
    out["texas"] = tx
    for name, sample in (("texas", tx), ("combined", rows + tx)):
        for cut in (31, 12):
            p = pooled(sample, cut)
            out[f"{name}_le{cut}"] = p
            print(f"{name} <= {cut}: excess {p['excess']:+.5f} ± {p['se']:.5f} (z={p['z']:+.2f}) over {p['balls']} balls")
    (ROOT / "sims" / "out" / "lottery.json").write_text(json.dumps(out, indent=1))
