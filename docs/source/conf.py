# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Myelo-Inferno MRI database'
copyright = '2023, SCIL'
author = 'Edde'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'


html_theme_options = {
    "rightsidebar": "False",
    "relbarbgcolor": "black"
}

html_static_path = ['_static']
html_css_files = [
    'my_style.css',  # overrides for width size
]
# -- Options for EPUB output
epub_show_urls = 'footnote'

