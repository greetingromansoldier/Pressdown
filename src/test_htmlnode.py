import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_before_props_to_html(self):
        node1 = HTMLNode("h1", None, None, {"href": "https://www.google.com"})
        node2 = HTMLNode("h1", None, None, {"href": "https://www.google.com"})
        self.assertEqual(node1.__repr__(), node2.__repr__())

    def test_props_to_html(self):
        node1 = HTMLNode("h1", None, None, {"href": "https://www.google.com"})
        node1.props_to_html()
        self.assertEqual(node1.__repr__(), "HTMLNode(h1, None, None,  href=https://www.google.com)")

    def test_general_inequality(self):
        node1 = HTMLNode("href", "Here's some text for you to consider", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("h1", "Here's some another text", None, {"href": "https://www.bing.com"})
        self.assertNotEqual(node1.__repr__(), node2.__repr__())






