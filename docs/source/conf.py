# Configuration file for the Sphinx documentation builder.
import sphinx_rtd_theme

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

sphinx_tabs_valid_builders = ['linkcheck']
templates_path = ['_templates']


# -- Options for HTML output

html_theme = "sphinx_rtd_theme"
html_context = {
    "sidebar_external_links_caption": "Links",
    "sidebar_external_links": [
        (
            '<i class="fa fa-github fa-fw"></i> GitHub',
            "https://github.com/scilus",
        ),
        (
            '<i class="fa fa-external-link fa-fw"></i> Website',
            "https://scil.usherbrooke.ca/",
        ),
        (
            '<i class="fa fa-envelope fa-fw"></i> Contact',
            "maxime.descoteaux@gmail.com",
        ),
        (
            '<i class="fa fa-database fa-fw"></i> Resources',
            "https://zenodo.org/records/4630660",
        ),
    ],
}



html_logo = "_static/scil_logo.png"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    "rightsidebar": "False",
    "relbarbgcolor": "black"
}
html_static_path = ['_static']
html_css_files = ['custom.css',]
html_sidebars = {
        '**': ['localtoc.html',
               'relations.html',
               'sourcelink.html',
               'searchbox.html',
               # located at _templates/
               'layout.html',
            ]

        }
#original_sidebar : ['localtoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']

#html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }


# -- Options for EPUB output
epub_show_urls = 'footnote'

