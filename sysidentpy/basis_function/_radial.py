"""Radial Basis Function for NORMAX Models."""

from typing import Optional
import numpy as np

from .basis_function_base import BaseBasisFunction


class Radial(BaseBasisFunction):

    def __init__(
        self,
        center: float = 0.0,    #center point of radial basis function
        width: float = 0.0,     #width of radial basis function
        dimensions: int = 1     #dimensions
        
    ):
        self.center = center
        self.width = width
        self.dimensions = dimensions


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
