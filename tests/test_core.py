# -*- coding: utf-8 -*-
import htmlmeta_hub
import htmlmeta_hub.pyramid_helpers

# core testing facility
import unittest

import six


# regexes to test against
import re

re_refresh_15 = re.compile('<meta http-equiv="refresh" content="15"/>')
re_other_charset = re.compile('<meta charset="utf8"/>')
re_link = re.compile('<link rel="canonical" href="http://www.w3.org"/>')

# pyramid testing requirements
from pyramid import testing


class TestCore(unittest.TestCase):
    def test_basic(self):
        a = htmlmeta_hub.HtmlMetaHub()
        a.set_http_equiv("refresh", "15")
        a.set_name("description", "awesome")
        a.set_name("title", u"greeñ")  # test unicode values
        a.set("content-type", "text/html;charset=UTF-8")
        a.set_other("charset", "utf8")
        b = a.get("description")
        a.unset("description")
        b = a.as_html()
        self.assertEqual(
            b,
            u"""<meta charset="utf8"/>
<meta http-equiv="content-type" content="text/html;charset=UTF-8"/>
<meta http-equiv="refresh" content="15"/>
<meta name="title" content="greeñ"/>""",
        )

    def test_set_http_equiv_1(self):
        a = htmlmeta_hub.HtmlMetaHub()
        a.set_http_equiv("refresh", "15")
        b = a.as_html()
        six.assertRegex(self, b, re_refresh_15)

    def test_set_http_equiv_2(self):
        a = htmlmeta_hub.HtmlMetaHub()
        a.set("refresh", "15")
        b = a.as_html()
        six.assertRegex(self, b, re_refresh_15)

    def test_unset_http_equiv_2(self):
        a = htmlmeta_hub.HtmlMetaHub()
        a.set("refresh", "15")
        b = a.as_html()
        six.assertRegex(self, b, re_refresh_15)
        a.unset("refresh")
        b = a.as_html()
        self.assertNotRegexpMatches(b, re_refresh_15)

    def test_set_other(self):
        a = htmlmeta_hub.HtmlMetaHub()
        a.set_other("charset", "utf8")
        b = a.as_html()
        six.assertRegex(self, b, re_other_charset)

    def test_set_link(self):
        a = htmlmeta_hub.HtmlMetaHub()
        a.set_link("canonical", "http://www.w3.org")
        b = a.as_html()
        six.assertRegex(self, b, re_link)


class TestMulti(unittest.TestCase):
    def test_basic(self):
        a = htmlmeta_hub.HtmlMetaHub()
        a.setmulti_link("author", "Jonathan")
        a.setmulti_link("author", "Lindsey")
        a.setmulti_link("author", "Jonathan")
        a.setmulti_link("author", "Jonathan")
        a.setmulti_link("author", "Lindsey")
        a.setmulti_link("author", "Debbie")
        a.unsetmulti_link("author", "Jonathan")
        result = """<link rel="author" href="Lindsey"/>\n<link rel="author" href="Debbie"/>"""
        self.assertEqual(result, a.as_html())


class TestPyramid(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.context = testing.DummyResource()
        self.request = testing.DummyRequest()
        self.html_meta_object = htmlmeta_hub.pyramid_helpers.htmlmeta_setup(
            request=self.request
        )

    def tearDown(self):
        testing.tearDown()

    def test_setup(self):
        self.assertEqual(self.html_meta_object, self.request._htmlmeta)

    def test_basic(self):
        htmlmeta_hub.pyramid_helpers.htmlmeta_set_http_equiv(
            "refresh", "15", request=self.request
        )
        htmlmeta_hub.pyramid_helpers.htmlmeta_set_name(
            "description", "awesome", request=self.request
        )
        htmlmeta_hub.pyramid_helpers.htmlmeta_set(
            "content-type", "text/html;charset=UTF-8", request=self.request
        )
        htmlmeta_hub.pyramid_helpers.htmlmeta_set_other(
            "charset", "utf8", request=self.request
        )
        b = htmlmeta_hub.pyramid_helpers.htmlmeta_get(
            "description", request=self.request
        )
        htmlmeta_hub.pyramid_helpers.htmlmeta_unset("description", request=self.request)
        b = htmlmeta_hub.pyramid_helpers.htmlmeta_as_html(request=self.request)

    def test_set_http_equiv_1(self):
        htmlmeta_hub.pyramid_helpers.htmlmeta_set_http_equiv(
            "refresh", "15", request=self.request
        )
        b = htmlmeta_hub.pyramid_helpers.htmlmeta_as_html(request=self.request)
        six.assertRegex(self, b, re_refresh_15)

    def test_set_http_equiv_2(self):
        htmlmeta_hub.pyramid_helpers.htmlmeta_set("refresh", "15", request=self.request)
        b = htmlmeta_hub.pyramid_helpers.htmlmeta_as_html(request=self.request)
        six.assertRegex(self, b, re_refresh_15)

    def test_unset_http_equiv_2(self):
        htmlmeta_hub.pyramid_helpers.htmlmeta_set("refresh", "15", request=self.request)
        b = htmlmeta_hub.pyramid_helpers.htmlmeta_as_html(request=self.request)
        six.assertRegex(self, b, re_refresh_15)
        htmlmeta_hub.pyramid_helpers.htmlmeta_unset("refresh", request=self.request)
        b = htmlmeta_hub.pyramid_helpers.htmlmeta_as_html(request=self.request)
        self.assertNotRegexpMatches(b, re_refresh_15)

    def test_set_other(self):
        htmlmeta_hub.pyramid_helpers.htmlmeta_set_other(
            "charset", "utf8", request=self.request
        )
        b = htmlmeta_hub.pyramid_helpers.htmlmeta_as_html(request=self.request)
        six.assertRegex(self, b, re_other_charset)