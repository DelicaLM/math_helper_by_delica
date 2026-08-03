from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='math_helper_by_delica',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description="A Python package with a variety of mathematical functions.",
    author="Delica Leboe-McGowan",
    author_email="stormindustries22@outlook.com",
    packages=['math_helper_by_delica'],
    install_requires=[

    ],
    long_description=long_description,
    long_description_type='text/markdown'
)
