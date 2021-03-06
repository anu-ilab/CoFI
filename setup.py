# pip install -e .

from setuptools import setup

setup(
    name="cofi",
    version="0.1.0",
    packages=["cofi", "cofi.cofi_forward", "cofi.cofi_inverse"],
    description="Common Framework for Inference",
    long_description=open("README.md").read(),
    install_requires=["numpy", "pandas", "scipy", "plotnine", "pyyaml"],
)
