# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SCIL longitudinal MRI database'
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
    'sphinx_tabs.tabs',
]

exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
sphinx_tabs_valid_builders = ['linkcheck']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    "rightsidebar": "False",
    "relbarbgcolor": "black"
}
html_context = {
    "sidebar_external_links_caption": "Links",
    "sidebar_external_links": [
        (
            '<i class="fa fa-github fa-fw"></i> GitHub',
            "https://github.com/scilus",
        )
    ],
}

html_static_path = ['_static']
html_css_files = [
    'custom.css',  # overrides for width size
]
# -- Options for EPUB output
epub_show_urls = 'footnote'

