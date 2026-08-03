from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='new_python_package',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description="A template for Python repositories on GitHub.",
    author="Delica Leboe-McGowan",
    author_email="stormindustries22@outlook.com",
    packages=['new_python_package'],
    install_requires=[

    ],
    long_description=long_description,
    long_description_type='text/markdown'
)
