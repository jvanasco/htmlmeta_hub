htmlmeta_hub
============

Build Status: ![Python package](https://github.com/jvanasco/htmlmeta_hub/workflows/Python%20package/badge.svg)

`htmlmeta_hub` offers lightweight support for managing metadata on webpages.

This package simply and conveniently manages a dict of "metadata"", and renders
it appropriately.

There are helpers for the Pyramid framework which will attach the metdata object
to a request, allowing you to build up metadata throughtout the request cycle
and then finally render.

A typical way to use this package in the Pyramid framework:


Include this package in your application's  `__init__.py`:

	def main(global_config, **settings):
		...
		# custom htmlmeta
		config.include("htmlmeta_hub.pyramid_helpers")


If you are using "class based views", you can set some default metadata in a core
handler:

	class Handler(object):
		def __init__(self,request):
			self.request = request
			# set some defaults
			self.reqesut.htmlmeta.set_many(\
				title="MyApp",
				description="awesome",
				keywords="fun!",
			)

and then you can add specific metadata in each view's handler:

	class ContentPage(Handler):
		def view(self):
		    content= ...
			self.request.htmlmeta.set('title', content.title)
			self.request.htmlmeta.set('description', content.description)

In a template, such as this `page.mako` example, you can access specific bits of
the metadata, or render an entire payload:

	<title>${request.htmlmeta.get('title')|n}</title>
	${request.htmlmeta.as_html()|n}


Pyramid helpers existed until version `0.3.x` but were dropped in favor of the
`@reify` request method offered by the `config.include` method.

Pylons helpers existed until version `0.1.2` but were dropped.


