# -*- coding: utf-8 -*-
# stdlib
import re
import unittest

# pypi
import six

# local package for testing
import htmlmeta_hub


# ==============================================================================

# regexes to test against
re_refresh_15 = re.compile('<meta http-equiv="refresh" content="15"/>')
re_other_charset = re.compile('<meta charset="utf8"/>')
re_link = re.compile('<link rel="canonical" href="http://www.w3.org"/>')


# ==============================================================================


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
