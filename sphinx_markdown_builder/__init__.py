"""
docutils XML to markdown sphinx extension.
"""
from sphinx_markdown_builder.builder import MarkdownBuilder

__version__ = "0.5.5"
__docformat__ = "reStructuredText"


def setup(app):
    app.add_builder(MarkdownBuilder)
    app.add_config_value("markdown_http_base", "", False)
    app.add_config_value("markdown_uri_doc_suffix", ".md", False)
    app.add_config_value("markdown_anchor_sections", False, False)
    app.add_config_value("markdown_anchor_signatures", False, False)
