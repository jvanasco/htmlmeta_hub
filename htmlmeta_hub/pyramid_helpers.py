from . import HtmlMetaHub
from pyramid.threadlocal import get_current_request

def htmlmeta_setup( request=None , **kwargs ):
    """Attaches a HtmlMetaHub to a request as 'request._htmlmeta'
    
        You'd probably have something like this in your base controller:

        from htmlmeta_hub.pyramid_helpers import *
        class Handler(object):
            def __init__(self,request):
                self.request = request
                h.htmlmeta_init( self.request , title='MySite', keywords='abc', description='awesome website')
                
        All the commands in the module accept an optional 'request' kwarg, but you should really pass it in.
        
        If no 'request' is submitted, it will call pyramid.threadlocal.get_current_request()
        
        The helpers should allow you to easily and cleanly manage metadata within views/handlers and templates.
    """
    if request is None:
       request= get_current_request()
    request._htmlmeta= HtmlMetaHub( **kwargs )

def htmlmeta_set_http_equiv(k,v,request=None):
    """proxies HtmlMetaHub.set_http_equiv through request._htmlmeta"""
    if request is None:
       request= get_current_request()
    crequest._htmlmeta.set_http_equiv()

def htmlmeta_set_name(k,v,request=None):
    """proxies HtmlMetaHub.set_name through request._htmlmeta"""
    if request is None:
       request= get_current_request()
    request._htmlmeta.set_name(k,v)

def htmlmeta_set(k,v,request=None):
    """proxies HtmlMetaHub.set through request._htmlmeta"""
    if request is None:
       request= get_current_request()
    request._htmlmeta.set(k,v)
    
def htmlmeta_get(k,request=None):
    """proxies HtmlMetaHub.get through request._htmlmeta"""
    if request is None:
       request= get_current_request()
    return request._htmlmeta.get(k)

def htmlmeta_unset(k,request=None):
    """proxies HtmlMetaHub.unset through request._htmlmeta"""
    if request is None:
       request= get_current_request()
    return request._htmlmeta.unset(k)

def htmlmeta_as_html(request=None):
    """proxies HtmlMetaHub.as_html through request._htmlmeta"""
    if request is None:
       request= get_current_request()
    return request._htmlmeta.as_html()
