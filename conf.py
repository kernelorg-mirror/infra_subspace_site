import alabaster
#import sphinx_rtd_theme

project = 'subspace.kernel.org'
copyright = '2021-2023, Kernel.org'
author = 'kernel.org'
#html_theme = 'sphinx_rtd_theme'
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme = 'alabaster'
html_theme_path = [alabaster.get_path()]
html_theme_options = {
        'page_width': '70em',
        'show_powered_by': False,
}
master_doc = 'index'
