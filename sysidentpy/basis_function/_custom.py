"""Custom Basis Function for NORMAX Models."""

from typing import Optional
import numpy as np

from .basis_function_base import BaseBasisFunction


class Custom(BaseBasisFunction):

    def __init__(
        self,
        degree: int = 2,
        function: str = "" #define which function i.e sin, cos, log, exp, etc.

    ):
        self.degree = degree
        self.function = function

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
