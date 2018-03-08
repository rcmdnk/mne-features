# Function to mock numba and let the code work on any system

from warnings import warn

try:
    import numba as nb
except ImportError:
    warn('numba not found. Your code will be slow')

    class Bunch(dict):
        """Dictionnary-like object thatexposes its keys as attributes."""

        def __init__(self, **kwargs):  # noqa: D102
            dict.__init__(self, kwargs)
            self.__dict__ = self


    class MockType(object):
        def __getitem__(self, slice):
            return

        def __call__(self, *args, **kwargs):
            return

    nb = Bunch()
    nb.int32 = MockType()
    nb.int64 = MockType()
    nb.float32 = MockType()
    nb.float64 = MockType()

    def jit(*args, **kwargs):
        def identity(ob):
            return ob
        return identity

    nb.jit = jit
