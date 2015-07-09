from . import HtmlMetaHub
from pyramid.threadlocal import get_current_request


def includeme(config):
    """the pyramid includeme command
    including this will automatically setup the htmlmeta object for every request
    """
    config.add_request_method(
        'htmlmeta_hub.pyramid_helpers.new_HtmlMetaHub',
        'htmlmeta',
        reify=True,
    )


def new_HtmlMetaHub(request):
    """simply creates a new hub"""
    return HtmlMetaHub()


# ==============================================================================
#   WARNING
#
#   Everything below is pretty much deprecated.  use the includeme instead and request methods
#
# ==============================================================================


def htmlmeta_setup(request=None, **kwargs):
    """Attaches a HtmlMetaHub to a request as 'request._htmlmeta'


        DONT DO THIS ANYMORE.  USE THE object directly via add_request_method



        You'd probably have something like this in your base controller:

        from htmlmeta_hub.pyramid_helpers import *
        class Handler(object):
            def __init__(self,request):
                self.request = request
                h.htmlmeta_init(self.request, title='MySite', keywords='abc', description='awesome website')

        All the commands in the module accept an optional 'request' kwarg, but you should really pass it in.

        If no 'request' is submitted, it will call pyramid.threadlocal.get_current_request()

        The helpers should allow you to easily and cleanly manage metadata within views/handlers and templates.
    """
    request = request or get_current_request()
    request._htmlmeta = HtmlMetaHub(**kwargs)
    return request._htmlmeta


def htmlmeta_set_http_equiv(k, v, request=None):
    """proxies HtmlMetaHub.set_http_equiv through request._htmlmeta"""
    request = request or get_current_request()
    request._htmlmeta.set_http_equiv(k, v)


def htmlmeta_set_link(k, v, request=None):
    """proxies HtmlMetaHub.set_link through request._htmlmeta"""
    request = request or get_current_request()
    request._htmlmeta.set_link(k, v)


def htmlmeta_set_name(k, v, request=None):
    """proxies HtmlMetaHub.set_name through request._htmlmeta"""
    request = request or get_current_request()
    request._htmlmeta.set_name(k, v)


def htmlmeta_set_other(k, v, request=None):
    """proxies HtmlMetaHub.set_other through request._htmlmeta"""
    request = request or get_current_request()
    request._htmlmeta.set_other(k, v)


def htmlmeta_set(k, v, request=None):
    """proxies HtmlMetaHub.set through request._htmlmeta"""
    request = request or get_current_request()
    request._htmlmeta.set(k, v)


def htmlmeta_get(k, request=None):
    """proxies HtmlMetaHub.get through request._htmlmeta"""
    request = request or get_current_request()
    return request._htmlmeta.get(k)


def htmlmeta_unset(k, request=None):
    """proxies HtmlMetaHub.unset through request._htmlmeta"""
    request = request or get_current_request()
    return request._htmlmeta.unset(k)


def htmlmeta_as_html(request=None):
    """proxies HtmlMetaHub.as_html through request._htmlmeta"""
    request = request or get_current_request()
    return request._htmlmeta.as_html()
