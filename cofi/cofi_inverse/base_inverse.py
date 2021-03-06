from cofi.cofi_forward.model_params import Model


class BaseInverse:
    """Base class for all inverse solvers in CoFI.

    All inverser solvers must be sub-classes of this class and implements two methods:
    1. __init__
    2. solve()
    """

    def __init__(self):
        pass

    def solve(self) -> Model:
        raise NotImplementedError("inversion 'solve' method not implemented")
