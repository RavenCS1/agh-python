from setuptools import setup, Extension

functions_module = Extension("functions", sources = ["functions.c"])

vector_module = Extension("vector", sources = ["vector.c"], libraries = ["m"])

setup(name = "my_module", version = "1.0", ext_modules = [functions_module, vector_module])