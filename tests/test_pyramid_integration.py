# -*- coding: utf-8 -*-
# stdlib
import re
import unittest

# pypi
import six

# pyramid testing requirements
from pyramid import testing
from pyramid.interfaces import IRequestExtensions

# local package for testing
import htmlmeta_hub
import htmlmeta_hub.pyramid_helpers


# ==============================================================================


class TestPyramid(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.include("htmlmeta_hub.pyramid_helpers")
        self.context = testing.DummyResource()
        self.request = testing.DummyRequest()

        # mare sure we have it...
        exts = self.config.registry.getUtility(IRequestExtensions)
        self.assertTrue("htmlmeta" in exts.descriptors)

        # intiialize a writer for the request
        htmlmeta = exts.descriptors["htmlmeta"].wrapped(self.request)
        # copy the writer onto the request...
        self.request.htmlmeta = htmlmeta

    def tearDown(self):
        testing.tearDown()

    def test_configured(self):
        self.assertIsInstance(self.request.htmlmeta, htmlmeta_hub.HtmlMetaHub)
