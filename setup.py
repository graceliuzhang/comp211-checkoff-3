from setuptools import setup, Extension

module = Extension(
    "mymodule",
    sources=["mymodule.c"]
)

setup(
    name="mymodule",
    version="1.0",
    ext_modules=[module]
)
