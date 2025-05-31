import unittest
from inline_markdown import (
    split_nodes_delimiter
)
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):

    def test_normal_case(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
                        new_nodes,
                        [
                        TextNode("This is text with a ", TextType.TEXT),
                        TextNode("code block", TextType.CODE),
                        TextNode(" word", TextType.TEXT),
                        ])

    def test_two_nodes_list(self):
        node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)

        self.assertEqual(
                        new_nodes,
                        [
                        TextNode("This is text with a ", TextType.TEXT),
                        TextNode("code block", TextType.CODE),
                        TextNode(" word", TextType.TEXT),
                        TextNode("This is text with a ", TextType.TEXT),
                        TextNode("code block", TextType.CODE),
                        TextNode(" word", TextType.TEXT),
                        ])

    def test_one_node_delimiter_exception(self):
        node = TextNode("This is text with a code block` word", TextType.TEXT)

        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    def test_normal_italic(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(
                        new_nodes,
                        [
                        TextNode("This is text with a ", TextType.TEXT),
                        TextNode("italic block", TextType.ITALIC),
                        TextNode(" word", TextType.TEXT),
                        ])


    def test_normal_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(
                        new_nodes,
                        [
                        TextNode("This is text with a ", TextType.TEXT),
                        TextNode("bold block", TextType.BOLD),
                        TextNode(" word", TextType.TEXT),
                        ])

    def test_different_delimiters(self):
        node = TextNode(
                        "This is text with _italic block_ and with **bold block**",
                        TextType.TEXT
                        )
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)


        self.assertEqual(
                        new_nodes,
                        [
                        TextNode("This is text with ", TextType.TEXT),
                        TextNode("italic block", TextType.ITALIC),
                        TextNode(" and with **bold block**", TextType.TEXT),
                        ])
    
    def test_several_delimeters_normal_case(self):
        node = TextNode(
                        "This is _actual text_ with _few_ italic blocks '_ _'",
                        TextType.TEXT
                        )
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(
                         new_nodes,
                         [
                         TextNode("This is ", TextType.TEXT),
                         TextNode("actual text", TextType.ITALIC),
                         TextNode(" with ", TextType.TEXT),
                         TextNode("few", TextType.ITALIC),
                         TextNode(" italic blocks '", TextType.TEXT),
                         TextNode(" ", TextType.ITALIC),
                         TextNode("'", TextType.TEXT),
                         ])

        
    def test_several_delimeters_exception_case(self):
        node = TextNode(
                        "This is _actual text_ with _few italic blocks '_ _'",
                        TextType.TEXT
                        )

        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

    # == Regex search for images ==


