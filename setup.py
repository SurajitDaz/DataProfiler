
from setuptools import setup, find_packages

setup(
    name="itmo-profiler",
    version="0.1.0",
    author="ITMO InfoChemistry Center",
    description="Interactive data profiler for Excel using Plotly and PDF export",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas", "numpy", "plotly", "openpyxl", "pdfkit"
    ],
    entry_points={
        "console_scripts": [
            "itmo-profiler=itmo_profiler.core:main"
        ]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
