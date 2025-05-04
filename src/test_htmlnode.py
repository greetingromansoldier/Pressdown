import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from functions import *

class TestHTMLNode(unittest.TestCase):

    # tests for html node
    def test_before_props_to_html(self):
        node1 = HTMLNode("h1", None, None, {"href": "https://www.google.com"})
        node2 = HTMLNode("h1", None, None, {"href": "https://www.google.com"})
        self.assertEqual(node1.__repr__(), node2.__repr__())

    def test_props_to_html(self):
        node1 = HTMLNode("h1", None, None, {"href": 'https://www.google.com'})
        node1.props_to_html()
        self.assertEqual(node1.__repr__(), 'HTMLNode(h1, None, None,  href="https://www.google.com")')

    def test_general_inequality(self):
        node1 = HTMLNode("href", "Here's some text for you to consider", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("h1", "Here's some another text", None, {"href": "https://www.bing.com"})
        self.assertNotEqual(node1.__repr__(), node2.__repr__())

    # tests for leaf node
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_tag_none(self):
        node = LeafNode(None, "something")
        self.assertEqual(node.to_html(), "something")

    def test_leaf_with_prop(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_prop_none(self):
        node = LeafNode("a", "Click me!")
        self.assertNotEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    # tests for parent node
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandgrandchildren(self):
        grandgrandchild_node = LeafNode("p", "grandgrandchild")
        grandchild_node = ParentNode("b", [grandgrandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b><p>grandgrandchild</p></b></span></div>",
        )

    def test_tag_is_none(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
        
    def test_child_is_none(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_multiple_children(self):
        parent_node = ParentNode( "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(parent_node.to_html(), 
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_children_parent_switched(self):

        child_node = LeafNode("span", "child")
        parent_node = ParentNode([child_node], "p")
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_tag_is_integer(self):

        child_node = LeafNode("span", "child")
        parent_node = ParentNode(5, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    # tests for text_node_to_html_node
    def test_text_type_is_text (self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()

