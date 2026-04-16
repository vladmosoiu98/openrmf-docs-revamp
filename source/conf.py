# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'OpenRMF OSS'
copyright = '2020-2026, Cingulara / Tutela'
author = 'OpenRMF Community'
release = '1.9'
version = '1.9'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
]

templates_path = ['_templates']
exclude_patterns = []

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'logo_only': False,
    # 'display_version': True,  # Deprecated in sphinx-rtd-theme 3.0+
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

html_context = {
    'display_github': True,
    'github_user': 'Cingulara',
    'github_repo': 'openrmf-docs',
    'github_version': 'master',
    'conf_py_path': '/source/',
}

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {}
latex_documents = [
    (master_doc, 'OpenRMFOSS.tex', 'OpenRMF OSS Documentation',
     'OpenRMF Community', 'manual'),
]

# -- Extension configuration -------------------------------------------------

todo_include_todos = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
