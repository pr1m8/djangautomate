# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Djangautomate'
copyright = '2025, pr1m8'
author = 'pr1m8'
release = '0.1.0'
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))  # Adjust for the correct path

#sys.path.insert(0, os.path.abspath('../../djangautomate'))  # Adjust for the correct path
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
import os
import sys

sys.path.insert(0, os.path.abspath('../../'))  # Ensure the module can be found

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'autoapi.extension',  # Enables automatic API documentation
]

# Specify where AutoAPI should look for the module
autoapi_dirs = ['../../djangautomate']  # Adjust if needed

# Use Google-style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = False

source_suffix = ['.rst']  # Keep only reStructuredText



html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


templates_path = ['_templates']
exclude_patterns = []

language = 'y'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_static_path = ['_static']
