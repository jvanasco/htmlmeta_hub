_http_equivs= ('content-type','expires','refresh',)
_link_rels = ('canonical','link',)

class HtmlMetaHub(object):
    data_struct= None

    def __init__(self,**kwargs):
        """Sets up self.data_struct dict which we use for storage of metadata.

        This package is rather silly, but it affords a consistent way to manage metadata across multiple projects.
        """
        self.data_struct= { 'http-equiv':{} , 'name':{} , 'other':{} , 'link':{}}
        for key,value in kwargs.iteritems():
            self.set(key,value)

    def set_http_equiv(self,key,value):
        self.data_struct['http-equiv'][key]= value

    def set_link(self,rel,value):
        self.data_struct['link'][rel]= value

    def set_name(self,key,value):
        self.data_struct['name'][key]= value

    def set_other(self,key,value):
        self.data_struct['other'][key]= value

    def set( self, key, value ):
        """ set uses (k,v) as there exists valid meta names which are not kwarg safe
        """
        if key.lower() in _http_equivs :
            self.data_struct['http-equiv'][key]= value
        elif key.lower() in _link_rels:
            self.data_struct['link'][key]= value
        else:
            self.data_struct['name'][key]= value

    def get(self,key):
        if key.lower() in _http_equivs :
            return self.data_struct['http-equiv'][key]
        elif key.lower() in _link_rels :
            return self.data_struct['link'][key]
        else:
            return self.data_struct['name'][key]

    def unset(self,key):
        if key.lower() in _http_equivs :
            if key in self.data_struct['http-equiv']:
                del self.data_struct['http-equiv'][key]
        elif key.lower() in _link_rels :
            if key in self.data_struct['link']:
                del self.data_struct['link'][key]
        else:
            if key in self.data_struct['name']:
                del self.data_struct['name'][key]

    def as_html(self):
        """helper function. prints out metadata for you.

        You'd probably call it like this in a Mako template:
            <head>
                ${meta.as_html()|n}
            </head>

        Notice that you have to escape under Mako.   For more information on mako escape options - http://www.makotemplates.org/docs/filtering.html
        """
        output= []
        for k,v in self.data_struct['http-equiv'].iteritems():
            output.append( """<meta http-equiv="%s" content="%s"/>""" % ( k , v ) )
        for k,v in self.data_struct['name'].iteritems():
            output.append( """<meta name="%s" content="%s"/>""" % ( k , v.replace("'","\'") ) )
        for k,v in self.data_struct['other'].iteritems():
            output.append( """<meta %s="%s"/>""" % ( k , v.replace("'","\'") ) )
        for rel,v in self.data_struct['link'].iteritems():
            output.append( """<link rel="%s" href="%s"/>""" % ( rel , v.replace("'","\'") ) )
        return "\n".join(output)
