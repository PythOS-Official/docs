import os
import sys
sys.path.insert(0, os.path.abspath(".."))  # if project's code is one level up

project = "PythOS"
author = "PythOS Team"
release = ""

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_logo = "_static/logo.png"  # optional: your logo
html_static_path = ["_static"]

# To support Markdown files
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
