# 文件头部 ************************************************************************************
import sphinx_rtd_theme


#默认配置 **************************************************************************************
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '笔记'
copyright = '2023, dongzl'
author = 'dongzl'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = ['recommonmark','sphinx_markdown_tables']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_rtd_theme
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# 配置：********************************************************************************************
# -- Options for LOGO output -------------------------------------------------
# -- 在html_logo中设置图片文件路径 -------------------------------------------
html_logo = './demo/image/logo.jpg'
# 不显示源码
html_show_sourcelink = False
# 修改默认样式
#def setup(app):
#    app.add_stylesheet("my_theme.css")
html_sidebars = { '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html']}
