import datetime
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join('..', 'src')))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
]

try:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
except ImportError:
    html_theme = 'default'

# Getting recommendation to use locale
gettext_uuid = True
gettext_compact = False

