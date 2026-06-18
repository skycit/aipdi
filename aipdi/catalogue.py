"""Loader for the named-entity catalogue and the indicative-band rule.

The catalogue (data/catalogue.csv) lists all 398 entities used in the paper,
each coded by segment, vertical and role, disclosed model posture, and source.
`indicative_band` reproduces the deterministic segment x posture rule used for
the "Indic. AIPDI" column of Table V. It is a coarse locator on the 0-100
scale, NOT a firm-level measurement (Sections IV-C, VIII); for an actual score,
collect the indicator evidence and call `aipdi.scoring.aipdi`.
"""

from __future__ import annotations

import csv
import os
from typing import Dict, List

__all__ = ["DATA_DIR", "load_catalogue", "indicative_band", "BAND_MAP"]

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")

# Segment x posture -> indicative AIPDI band (mirrors aipdiBand in the paper).
BAND_MAP: Dict[str, Dict[str, int]] = {
    "Provider":       {"O": 10, "M": 20, "S": 30},
    "Infrastructure": {"M": 35, "O": 28, "S": 60},
    "AI-native":      {"S": 90, "M": 55, "O": 45},
    "Incumbent":      {"S": 42, "M": 30, "O": 26},
}


def indicative_band(segment: str, posture: str, default: int = 50) -> int:
    """Deterministic indicative AIPDI from segment and posture (S/M/O).

    A trailing dagger on the posture (segment-typical coding) is ignored.
    """
    posture = posture.replace("\u2020", "").strip()
    return BAND_MAP.get(segment, {}).get(posture, default)


def load_catalogue(path: str | None = None) -> List[Dict[str, str]]:
    """Load data/catalogue.csv as a list of dict rows, adding `indic_aipdi`."""
    path = path or os.path.join(DATA_DIR, "catalogue.csv")
    rows: List[Dict[str, str]] = []
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            r["indic_aipdi"] = indicative_band(r["segment"], r["posture"])
            rows.append(r)
    return rows
