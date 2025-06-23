from setuptools import setup

setup(
    name="IUM",
    version="0.1",
    install_requires=[
        "pandas",
        "matplotlib",
        "numpy",
        "scipy",
        "geopandas",
        "seaborn",
        "plotly",
    ],
    extras_require={
        "notebook": [
            "notebook",
            "ipykernel",
            "jupyterlab",
        ]
    }
)