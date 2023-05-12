# stdlib
import typing

# local
from . import HtmlMetaHub

if typing.TYPE_CHECKING:
    from pyramid.config import Configurator  # type: ignore[import]
    from pyramid.request import Request  # type: ignore[import]

# ==============================================================================


def includeme(config: "Configurator"):
    """the pyramid includeme command
    including this will automatically setup the htmlmeta object for every request
    """
    config.add_request_method(
        "htmlmeta_hub.pyramid_helpers.new_HtmlMetaHub", "htmlmeta", reify=True
    )


def new_HtmlMetaHub(request: "Request"):
    """simply creates a new hub"""
    return HtmlMetaHub()
