# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os

version_num = ""

curr_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(os.path.dirname(curr_directory))
init_directory = os.path.join(project_directory, "new_python_package/")
init_path = os.path.join(init_directory, "__init__.py")

try:
    with open(init_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith("__version__"):
                line_no_whitespace = line.strip().replace(" ","")
                if line_no_whitespace.startswith("__version__="):
                    line_no_prefix = line_no_whitespace.replace("__version__=","")
                    line_no_quotes = line_no_prefix.replace("\"","")
                    if line_no_quotes != "" and line_no_quotes != "unknown":
                        if not line_no_quotes.startswith("version("):
                            version_num = line_no_quotes
except FileNotFoundError:
    version_num = ""

project = 'new-python-package'
copyright = '2026, Delica Leboe-McGowan'
author = 'Delica Leboe-McGowan'
release = version_num

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
#

extensions = ['autodoc2',
    'myst_parser',
    'sphinx.ext.napoleon',  # For Google and NumPy style docstrings
    'sphinx.ext.githubpages',]

autodoc2_docstring_parser_regexes = [
    (r".*", "rst"),
]

autodoc_type_aliases = {

}
primary_domain = 'py'

master_doc = "index"

suppress_warnings = ["ref.*"]

napoleon_google_docstring = False
napoleon_numpy_docstring = True

autodoc2_packages = [
    "../../new_python_package/new_python_funcs.py",
"../../tests/test_new_python_funcs.py"
]
#templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_theme_options = {
    "sidebarwidth": "350",
}
# html_theme_options = {
#     'sidebarwidth': '350px',
# }

#html_static_path = ['_static']
# html_sidebars = {
#     '**': [
#         'globaltoc.html',
#     ]
# }

