import unittest

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
        c1=Content(name="children1",parent=p)
        c2=Content(name="children2",parent=p)
        self.assertTrue(c1 in p.children)
        self.assertTrue(c2 in p.children)
        
    def handle_test(self):
        p=Content(name="parent")
        p.put()
        c=Content(name="children",parent=p)
        self.assertEquals(c.handle,"/parent/children")
