from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([
        "solver/fast_neighbors.pyx",
        "solver/c_heuristics.pyx"
    ], language_level=3),
    zip_safe=False,
)
