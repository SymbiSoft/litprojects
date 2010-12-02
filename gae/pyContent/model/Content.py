import logging
from google.appengine.ext import db

class Content(db.Expando):
    name__ = db.StringProperty(required=True,name="name")

    def __init__(self, name, **kwds):
        #logging.debug(kwds)
        _name=name.lower().replace(" ","-")
        db.Expando.__init__(self,name=_name,**kwds)
        
    def setName(self,name):
        self.name__=name.lower().replace(" ","-")
        
    def getName(self):
        return self.name__
        
    def getHandle(self):
        if self.parent():
            return self.parent().getHandle()+"/"+self.getName()
        else:
            return "/"+self.getName()
            
    def getChildren(self):
        #q = db.GqlQuery('SELECT * WHERE ANCESTOR IS :1 ', self.key())
        q=db.Query()
        return q.ancestor(self.key())
            
    name=property(fget=getName,fset=setName)
    handle=property(fget=getHandle)
    children=property(fget=getChildren)
        
