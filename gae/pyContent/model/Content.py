import logging
import re
from google.appengine.ext import db

class Content(db.Expando):
    name__ = db.StringProperty(required=True,name="name")
    creationDate=db.DateTimeProperty(required=True)

    def __init__(self, parent=None, key_name=None, _app=None, **kwds):
        kwds['name']=self.sanitize(kwds["name"])
        kwds['creationDate']=db.DateTimeProperty.now()
        db.Expando.__init__(self,parent=parent, key_name=key_name, _app=None, **kwds)
        
    def setName(self,name):
        self.name__=self.sanitize(name)
        
    def getName(self):
        return self.name__
        
    def getHandle(self):
        if self.parent():
            return self.parent().getHandle()+"/"+self.getName()
        else:
            return "/"+self.getName()
            
    def getChildren(self):
        q=db.Query()
        return q.ancestor(self.key()).filter('__key__ !=',self.key())
        
    def ancestor(self,level):
        #check magnolia/jcr code
        if level==1: 
            return self
        elif self.parent():
            return self.parent().ancestor(level-1)
    
    name=property(fget=getName,fset=setName)
    handle=property(fget=getHandle)
    children=property(fget=getChildren)
    
    def sanitize(self,name):
        sanitized_name=ContentUtils.sanitize(name)
        if (self.parent() and sanitized_name in [c.name for c in self.parent().children]):
            m=re.match(r'([-a-z]*)(\d*)$',sanitized_name)
            if m.group(2):
                index=int(m.group(2))+1
            else:
                index=0
            return self.sanitize("%s%s" % (m.group(1),index))
        return sanitized_name
                
            
    
class ContentUtils(object):
    @staticmethod
    def sanitize(text):
        return text.lower().replace(" ","-")
    
class DuplicateContentNameException(Exception):
    """Duplicate named content at the same level"""
