import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_enum_equality(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType("bold"))
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_wrong_not_equal(self):
        node = TextNode("This is one text", TextType.BOLD)
        node2 = TextNode("This is another text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_not_none(self):
        node = TextNode("This is a text node", TextType.BOLD, TextType.LINK)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)

    # def test_non_exist_type(self):
    #     node = TextNode("This is a text node", TextType.BOLD, TextType.LINK)
    #     with self.assertRaises(ValueError):
    #         parent_node.to_html()


if __name__ == "__main__":
    unittest.main()
