"""Конфигурация Sphinx для проекта ApiProject."""

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "ApiProject"
author = "ApiProject maintainers"
release = "1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = ["_build"]
language = "ru"

napoleon_google_docstring = True
napoleon_numpy_docstring = False

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

html_theme = "alabaster"
html_static_path = ["_static"]

