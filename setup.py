from setuptools import setup, find_packages
from Cython.Build import cythonize

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="workninja",
    version="0.0.1",
    author="fullzer4",
    author_email="gabrielpelizzaro@gmail.com",
    description="Fast & Clever Work Manager Framework for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fullzer4/WorkNinja",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    ext_modules=cythonize("src/work_ninja.pyx"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)