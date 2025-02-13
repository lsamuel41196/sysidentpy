"""Custom Basis Function for NORMAX Models."""

from typing import Optional
import numpy as np

from .basis_function_base import BaseBasisFunction


class Custom(BaseBasisFunction):

    def __init__(
        self,
        bf_name: str = "custom_bf",
        degree: int = 2,

    ):
        self.degree = degree
        self.bf_name = bf_name

    def fit(
        self,
        data: np.ndarray,
        max_lag: int = 1,
        ylag: int = 1,
        xlag: int = 1,
        model_type: str = "NARMAX",
        predefined_regressors: Optional[np.ndarray] = None,
    ):   
        
        pass

    def transform(
        self,
        data: np.ndarray,
        max_lag: int = 1,
        ylag: int = 1,
        xlag: int = 1,
        model_type: str = "NARMAX",
        predefined_regressors: Optional[np.ndarray] = None,
    ):
        pass
