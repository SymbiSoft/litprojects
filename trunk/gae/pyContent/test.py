import unittest
import logging

import pdb

from model.Content import Content
#import unittest.TestCase as t

class ContentModelTest(unittest.TestCase):
    def content_creation_test(self):
        c=Content(name="dsas")
        c.put()
        
    def content_difficult_name_test(self):
        c=Content(name="D d")
        self.assertEquals(c.name,"d-d")
        
    def content_difficult_name_2_test(self):
        c=Content(name="test")
        c.name="D d"
        self.assertEquals(c.name,"d-d")
        
    def dinamic_property_test(self):
        c=Content(name="test",title="Content title")
        c.put()
        self.assertEquals(c.title,"Content title")
        
    def content_parent_test(self):
        p=Content(name="parent")
        p.put()
        c=Content(name="children",parent=p)
        self.assertEquals(c.parent().name,"parent")
        
    def content_children_test(self):
        p=Content(name="parent")
        p.put()
        c1=Content(name="children1",parent=p)
        c2=Content(name="children2",parent=p)
        c1.put()
        c2.put()
        children=[c.key() for c in p.children]
        self.assertEquals(len(children),2)
        self.assertTrue(c1.key() in children and c2.key() in children)
        c1.delete()
        c2.delete()
        p.delete()
        
        
    def handle_test(self):
        p=Content(name="parent")
        p.put()
        c=Content(name="children",parent=p)
        self.assertEquals(c.handle,"/parent/children")

    def ancestor__disabled(self):
        gp=Content(name="grandpa_ancestor")
        gp.put()
        p=Content(name="parent_ancestor",parent=gp)
        p.put()
        c=Content(name="child_ancestor",parent=p)
        c.put()
        self.assertEquals(c.ancestor(1).key() ,gp.key())        
        
