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

html_theme = 'alabaster'
html_theme_options = {
  'logo': 'FujiNet-Header.png',
  'anchor': '#333',
  'base_bg': '#212121',
  'body_bg': ' #eaeded',
  'base_text': '#ccc',
  'body_text': '#323232',
  #'link': '#448CE4',
  'link': '#2471a3',
  'sidebar_header': '#fdedec',
  'sidebar_hr': '#ff0000',
  'sidebar_text': '#aaaaff',
  'sidebar_link': '#aaa',
  'sidebar_list': '#fff',
  'topic_bg': '#00f',
  'shadow': '#333',
  'code_bg': '#aaa',
  'pre_bg': '#aaa',
}
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