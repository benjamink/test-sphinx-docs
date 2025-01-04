# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FujiNet'
copyright = '2025, FujiNet Team'
author = 'FujiNet Team'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_pdj_theme'
html_theme_options = {
  'logo': 'FujiNet-Header.png',
  'base_bg': '#212121',
  'base_text': '#ffffff',
  'body_text': '#666666',
}
#  'bgcolor': '#302B35',
#  'textcolor': '#ffffff', 
#  'linkcolor': '#115178',
#  'headbgcolor': '#212121',
#  'headtextcolor': '#ffffff',
#  'sidebarbgcolor': '#212121',
#  'sidebartextcolor': '#ffffff',
#  'sidebartextcolor': '#666666',
#  'footerbgcolor': '#212121',
#  'footertextcolor': '#999999',
#}
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'about.html',
        'searchfield.html',
        'navigation.html',
        'relations.html',
        'donate.html',
    ]
}