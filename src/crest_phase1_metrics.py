"""
CREST Phase 1 metrics utilities.

This module contains lightweight helper functions for reproducing
Phase 1 benchmark tables and figures from derived CSV assets.

It is not yet the full raw SPARC refit pipeline.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def rmse(y_true, y_pred) -> float:
    """Return root mean squared error."""
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


def gain_percent(baseline_rmse: float, model_rmse: float) -> float:
    """
    Return percent gain relative to baseline RMSE.

    Positive means the model improved over the baseline.
    Negative means the model performed worse than the baseline.
    """
    baseline_rmse = float(baseline_rmse)
    model_rmse = float(model_rmse)
    return 100.0 * (baseline_rmse - model_rmse) / baseline_rmse


def load_phase1_rmse_table(path: str) -> pd.DataFrame:
    """Load the Phase 1 RMSE comparison table."""
    return pd.read_csv(path)


def load_halo_reference_table(path: str) -> pd.DataFrame:
    """Load the Phase 1 tuned-halo reference table."""
    return pd.read_csv(path)


def load_overlap_cases(path: str) -> pd.DataFrame:
    """Load the Phase 1 map/cube overlap galaxy list."""
    return pd.read_csv(path)


def crest_backbone_acceleration(g_bar, a0: float = 7.781e-11):
    """
    Fixed CREST backbone acceleration branch.

    g_pred = g_bar + sqrt(a0 * g_bar)

    Parameters
    ----------
    g_bar:
        Baryonic acceleration array.
    a0:
        CREST backbone acceleration scale in SI units.

    Returns
    -------
    numpy.ndarray
        Predicted acceleration.
    """
    g_bar = np.asarray(g_bar, dtype=float)
    return g_bar + np.sqrt(a0 * g_bar)


def mond_simple_acceleration(g_bar, a0: float):
    """
    Simple MOND-style one-parameter acceleration branch.

    g_mond = 0.5 * g_bar * (1 + sqrt(1 + 4*a0/g_bar))
    """
    g_bar = np.asarray(g_bar, dtype=float)
    return 0.5 * g_bar * (1.0 + np.sqrt(1.0 + (4.0 * a0 / g_bar)))


def rar_acceleration(g_bar, a0: float):
    """
    RAR-form one-parameter branch.

    g_rar = g_bar / (1 - exp(-sqrt(g_bar/a0)))
    """
    g_bar = np.asarray(g_bar, dtype=float)
    return g_bar / (1.0 - np.exp(-np.sqrt(g_bar / a0)))
