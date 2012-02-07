from . import HtmlMetaHub
from pylons import c 

def htmlmeta_setup( **kwargs ):
    """Attaches a HtmlMetaHub to a request as 'c._htmlmeta'
    
        You'd probably have something like this in your base controller:

        from htmlmeta_hub.pylons_helpers import *
        class Handler(object):
            def __init__(self,request):
                h.htmlmeta_init( title='MySite', keywords='abc', description='awesome website')
                
        The helpers should allow you to easily and cleanly manage metadata within views/handlers and templates.
    """
    c._htmlmeta= HtmlMetaHub( **kwargs )

def htmlmeta_set_http_equiv(k,v):
    """proxies HtmlMetaHub.set_http_equiv through c._htmlmeta"""
    c._htmlmeta.set_http_equiv(k,v)

def htmlmeta_set_name(k,v):
    """proxies HtmlMetaHub.set_name through c._htmlmeta"""
    c._htmlmeta.set_name(k,v)

def htmlmeta_set(k,v):
    """proxies HtmlMetaHub.set through c._htmlmeta"""
    c._htmlmeta.set(k,v)

def htmlmeta_get(k):
    """proxies HtmlMetaHub.get through c._htmlmeta"""
    return c._htmlmeta.get(k)

def htmlmeta_unset(k):
    """proxies HtmlMetaHub.unset through c._htmlmeta"""
    c._htmlmeta.unset(k)

def htmlmeta_as_html():
    """proxies HtmlMetaHub.as_html through c._htmlmeta"""
    return c._htmlmeta.as_html()
