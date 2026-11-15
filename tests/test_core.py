# -*- coding: utf-8 -*-
# stdlib
import re
import unittest

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
        a.set_name("title", "greeñ")  # test unicode values
        a.set("content-type", "text/html;charset=UTF-8")
        a.set_other("charset", "utf8")
        b = a.get("description")
        a.unset("description")
        b = a.as_html()
        self.assertEqual(
            b,
            """<meta charset="utf8"/>
<meta http-equiv="content-type" content="text/html;charset=UTF-8"/>
<meta http-equiv="refresh" content="15"/>
<meta name="title" content="greeñ"/>""",
        )

    def test_set_http_equiv_1(self):
        a = htmlmeta_hub.HtmlMetaHub()
        a.set_http_equiv("refresh", "15")
        b = a.as_html()
        self.assertRegex(b, re_refresh_15)

    def test_set_http_equiv_2(self):
        a = htmlmeta_hub.HtmlMetaHub()
        a.set("refresh", "15")
        b = a.as_html()
        self.assertRegex(b, re_refresh_15)

    def test_unset_http_equiv_2(self):
        a = htmlmeta_hub.HtmlMetaHub()
        a.set("refresh", "15")
        b = a.as_html()
        self.assertRegex(b, re_refresh_15)
        a.unset("refresh")
        b = a.as_html()
        self.assertNotRegex(b, re_refresh_15)

    def test_set_other(self):
        a = htmlmeta_hub.HtmlMetaHub()
        a.set_other("charset", "utf8")
        b = a.as_html()
        self.assertRegex(b, re_other_charset)

    def test_set_other_preserves_valid_attribute_names(self) -> None:
        """Render a custom name literally and escape its quoted value."""
        hub = htmlmeta_hub.HtmlMetaHub()
        hub.set_other("data-label", '"A&B"')
        hub.set_other("data-a&b", "value")
        self.assertEqual(
            hub.as_html(),
            '<meta data-label="&quot;A&amp;B&quot;"/>\n<meta data-a&b="value"/>',
        )

    def test_set_other_rejects_malformed_attribute_names(self) -> None:
        """Reject malformed names before storing metadata."""
        hub = htmlmeta_hub.HtmlMetaHub()
        for name in ("", "a b", "a\tb", "a/b", "a=b", 'a"b', "a<b", "a\0b", "a\uffff"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                hub.set_other(name, "value")
        self.assertEqual(hub.as_html(), "")

    def test_as_html_rejects_malformed_stored_attribute_name(self) -> None:
        """Validate attributes inserted directly into the public data structure."""
        hub = htmlmeta_hub.HtmlMetaHub()
        hub.data_struct["other"]["invalid name"] = "value"
        with self.assertRaises(ValueError):
            hub.as_html()

    def test_set_link(self):
        a = htmlmeta_hub.HtmlMetaHub()
        a.set_link("canonical", "http://www.w3.org")
        b = a.as_html()
        self.assertRegex(b, re_link)


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
