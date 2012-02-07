htmlmeta_hub gives lightweight support for managing metadata. it simply manages a dict of metadata, and prints it out. there are helpers for pylons and pyramid which will attach the object to a request, allowing you to build up metadata throughtout the request cycle and then print it out.



A typical way to use this package ( in pyramid framework ):


helpers.py:
    from htmlmeta_hub.pyramid_helpers import *

handlers/__init__.py:

    from ..lib import helpers as h
	
	class Handler(object):
		def __init__(self,request):
			self.request = request
			# set some defaults
			h.htmlmeta_setup(\
				request=request,
				title="MyApp", 
				description="awesome", 
				keywords="fun!",
			)


	class ContentPage(Handler):
		def view(self):
		    content= ...
			h.htmlmeta_set('title',content.title)
			h.htmlmeta_set('description',content.description)

templates/page.mako
	<title>${h.htmlmeta_get('title',request=request)|n}</title>
	${h.htmlmeta_as_html(request=request)|n}
