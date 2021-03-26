from . import HtmlMetaHub


def includeme(config):
    """the pyramid includeme command
    including this will automatically setup the htmlmeta object for every request
    """
    config.add_request_method(
        "htmlmeta_hub.pyramid_helpers.new_HtmlMetaHub", "htmlmeta", reify=True
    )


def new_HtmlMetaHub(request):
    """simply creates a new hub"""
    return HtmlMetaHub()
