import os
import sys

# -- Project Information -------------------------------------------------
project = "DjangAutomate"
copyright = "2025, pr1m8"
author = "pr1m8"
release = "0.1.0"

# -- Path Configuration ---------------------------------------------------
sys.path.insert(0, os.path.abspath('../../'))  # Ensure the module is found

# -- Sphinx Extensions ----------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',      # Auto-generate documentation from docstrings
    'sphinx.ext.napoleon',     # Google-style docstrings support
    'sphinx.ext.viewcode',     # Add links to source code
]

# -- Autodoc Settings -----------------------------------------------------
autodoc_mock_imports = ["sqlalchemy", "django"]
autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "private-members": False,
    "special-members": "__init__",
    "show-inheritance": True,
}

# -- Google-style docstrings ----------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = False

# -- Source File Settings -------------------------------------------------
source_suffix = ['.rst']
master_doc = 'index'  # Ensure index.rst is the main file

# -- HTML Output Settings -------------------------------------------------
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'  # Ensure the theme is loaded correctly
html_static_path = ['_static']

# -- Templates Path -------------------------------------------------------
templates_path = ['_templates']
exclude_patterns = []
