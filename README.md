htmlmeta_hub gives lightweight support for managing metadata. it simply manages a dict of metadata, and prints it out. there are helpers for pyramid which will attach the object to a request, allowing you to build up metadata throughtout the request cycle and then print it out.



A typical way to use this package ( in pyramid framework ):


__init__.py:

	def main(global_config, **settings):
		...
		# custom htmlmeta
		config.include("htmlmeta_hub.pyramid_helpers")


handlers/__init__.py:

	class Handler(object):
		def __init__(self,request):
			self.request = request
			# set some defaults
			self.reqesut.htmlmeta.set_many(\
				title="MyApp",
				description="awesome",
				keywords="fun!",
			)


	class ContentPage(Handler):
		def view(self):
		    content= ...
			self.request.htmlmeta.set('title', content.title)
			self.request.htmlmeta.set('description', content.description)


templates/page.mako
	<title>${request.htmlmeta.get('title')|n}</title>
	${request.htmlmeta.as_html()|n}


pylons helpers existed until version 0.1.2 but were dropped