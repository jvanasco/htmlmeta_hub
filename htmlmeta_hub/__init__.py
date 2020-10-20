from metadata_utils import html_attribute_escape


__VERSION__ = "0.4.0"


# ==============================================================================


_http_equivs = ("content-type", "expires", "refresh")
_link_rels = ("canonical", "link")


class HtmlMetaHub(object):
    data_struct = None

    def __init__(self, **kwargs):
        """Sets up self.data_struct dict which we use for storage of metadata.

        This package is rather silly, but it affords a consistent way to manage metadata across multiple projects.
        """
        self.data_struct = {
            "http-equiv": {},
            "name": {},
            "other": {},
            "link": {},
            "_multi": {},  # private namespace for setmulti
        }
        self.set_many(**kwargs)

    def set_http_equiv(self, key, value):
        self.data_struct["http-equiv"][key] = value

    def set_link(self, rel, value):
        self.data_struct["link"][rel] = value

    def set_name(self, key, value):
        self.data_struct["name"][key] = value

    def set_other(self, key, value):
        self.data_struct["other"][key] = value

    def set(self, key, value):
        """set uses (k,v) as there exists valid meta names which are not kwarg safe"""
        if key.lower() in _http_equivs:
            self.data_struct["http-equiv"][key] = value
        elif key.lower() in _link_rels:
            self.data_struct["link"][key] = value
        else:
            self.data_struct["name"][key] = value

    def set_many(self, **kwargs):
        """ set simply iterates over the **kwargs; here for legacy compatibility"""
        for key, value in kwargs.items():
            self.set(key, value)

    def get(self, key):
        if key.lower() in _http_equivs:
            return self.data_struct["http-equiv"].get(key, None)
        elif key.lower() in _link_rels:
            return self.data_struct["link"].get(key, None)
        else:
            return self.data_struct["name"].get(key, None)

    def unset(self, key):
        if key.lower() in _http_equivs:
            if key in self.data_struct["http-equiv"]:
                del self.data_struct["http-equiv"][key]
        elif key.lower() in _link_rels:
            if key in self.data_struct["link"]:
                del self.data_struct["link"][key]
        else:
            if key in self.data_struct["name"]:
                del self.data_struct["name"][key]

    # --------------------------------------------------------------------------
    # these are used for multile items.
    # sometimes you'll have several 'authors' in a link

    def _hasmulti(self, section, key, value):
        if section in self.data_struct["_multi"]:
            if key in self.data_struct["_multi"][section]:
                if value in self.data_struct["_multi"][section][key]:
                    return True
        return False

    def _setmulti(self, section, key, value):
        if section not in self.data_struct["_multi"]:
            self.data_struct["_multi"][section] = {}
        if key not in self.data_struct["_multi"][section]:
            self.data_struct["_multi"][section][key] = []
        if not self._hasmulti(section, key, value):
            self.data_struct["_multi"][section][key].append(value)

    def _unsetmulti(self, section, key, value):
        if self._hasmulti(section, key, value):
            self.data_struct["_multi"][section][key] = [
                i for i in self.data_struct["_multi"][section][key] if i != value
            ]

    def _clearmulti(self, section, key):
        if section in self.data_struct["_multi"]:
            if key in self.data_struct["_multi"][section]:
                del self.data_struct["_multi"][section][key]

    def setmulti_link(self, key, value):
        """sets a value for a non-unique key"""
        self._setmulti("link", key, value)

    def unsetmulti_link(self, key, value):
        """unsets a value for a non-unique key"""
        self._unsetmulti("link", key, value)

    def clearmulti_link(self, key):
        """clears a value for a non-unique key"""
        self._clearmulti("link", key)

    # --------------------------------------------------------------------------

    def as_html(self):
        """helper function. prints out metadata for you.

        You'd probably call it like this in a Mako template:
            <head>
                ${meta.as_html()|n}
            </head>

        Notice that you have to escape under Mako.   For more information on mako escape options - http://www.makotemplates.org/docs/filtering.html
        """
        output = []
        _others = self.data_struct["other"].items()
        _equivs = self.data_struct["http-equiv"].items()
        _others_2 = []
        _equivs_2 = []
        for (k, v) in _others:
            if k.lower() == "charset":
                output.append(
                    u"""<meta %s="%s"/>"""
                    % (html_attribute_escape(k), html_attribute_escape(v))
                )
            else:
                _others_2.append((k, v))
        for (k, v) in _equivs:
            if "charset" in v.lower():
                output.append(
                    u"""<meta http-equiv="%s" content="%s"/>"""
                    % (html_attribute_escape(k), html_attribute_escape(v))
                )
            else:
                _equivs_2.append((k, v))
        for (k, v) in _equivs_2:
            output.append(
                u"""<meta http-equiv="%s" content="%s"/>"""
                % (html_attribute_escape(k), html_attribute_escape(v))
            )
        for (k, v) in self.data_struct["name"].items():
            output.append(
                u"""<meta name="%s" content="%s"/>"""
                % (html_attribute_escape(k), html_attribute_escape(v))
            )
        for (k, v) in _others_2:
            output.append(
                u"""<meta %s="%s"/>"""
                % (html_attribute_escape(k), html_attribute_escape(v))
            )
        for (rel, v) in self.data_struct["link"].items():
            output.append(
                u"""<link rel="%s" href="%s"/>"""
                % (html_attribute_escape(rel), html_attribute_escape(v))
            )
        if self.data_struct["_multi"]:
            if "link" in self.data_struct["_multi"]:
                for rel in self.data_struct["_multi"]["link"]:
                    for v in self.data_struct["_multi"]["link"][rel]:
                        output.append(
                            u"""<link rel="%s" href="%s"/>"""
                            % (html_attribute_escape(rel), html_attribute_escape(v))
                        )
        return u"\n".join(output)
