"""aipdi -- a reference implementation of the AI-Provider Dependency Index.

Companion code for "AI-Dependent or AI-Enabled? A Reliability-Oriented Index
for Measuring Downstream Reliance on Foundation-Model Providers."

Public API
----------
Scoring (Section III-F equations):
    normalize, technical_subindex, commercial_subindex, aipdi,
    aipdi_geometric, survivability, single_supplier_share, hhi,
    availability_series, availability_parallel, unavailability_parallel,
    expected_loss
Weighting (Section IV-C):
    DEFAULT_WEIGHTS, TECHNICAL_INDICATORS, COMMERCIAL_INDICATORS,
    equal_weights, entropy_weights, ahp_weights, consistency_ratio,
    budget_allocation
Sensitivity (Section IV-C):
    dirichlet_uncertainty, oat_elasticity, sobol_sensitivity
Catalogue:
    load_catalogue, indicative_band
"""

from .scoring import (
    normalize, technical_subindex, commercial_subindex, aipdi,
    aipdi_geometric, survivability, single_supplier_share, hhi,
    availability_series, availability_parallel, unavailability_parallel,
    expected_loss,
)
from .weighting import (
    DEFAULT_WEIGHTS, TECHNICAL_INDICATORS, COMMERCIAL_INDICATORS,
    equal_weights, entropy_weights, ahp_weights, consistency_ratio,
    budget_allocation, validate_weights,
)
from .sensitivity import dirichlet_uncertainty, oat_elasticity, sobol_sensitivity
from .catalogue import load_catalogue, indicative_band, BAND_MAP

__version__ = "0.1.0"

__all__ = [
    "normalize", "technical_subindex", "commercial_subindex", "aipdi",
    "aipdi_geometric", "survivability", "single_supplier_share", "hhi",
    "availability_series", "availability_parallel", "unavailability_parallel",
    "expected_loss",
    "DEFAULT_WEIGHTS", "TECHNICAL_INDICATORS", "COMMERCIAL_INDICATORS",
    "equal_weights", "entropy_weights", "ahp_weights", "consistency_ratio",
    "budget_allocation", "validate_weights",
    "dirichlet_uncertainty", "oat_elasticity", "sobol_sensitivity",
    "load_catalogue", "indicative_band", "BAND_MAP",
    "__version__",
]
