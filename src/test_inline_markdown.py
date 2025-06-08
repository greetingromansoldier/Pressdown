import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_link,
    split_nodes_image,
    text_to_textnodes
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

    # == Extracting markdown links and images ==

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    # == Split links and images from text to TextNodes ==

    def test_split_images_normal_case(self):
        node = TextNode(
            ("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)" 
            " and another ![second image](https://i.imgur.com/3elNhQu.png)"),
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links_normal_case(self):
        node = TextNode(
            ("This is a text with link [to google](https://www.google.com)"
              " and [to youtube](https://www.youtube.com)"
             ),
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a text with link ", TextType.TEXT),
                TextNode("to google", TextType.LINK, "https://www.google.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com"
                ),
            ],
            new_nodes,
        )

    # == If no links or images in text - must return just same text node with same type ==

    def test_no_links(self):
        node = TextNode(
            ("This is text without links"),
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(
                ("This is text without links"),
                TextType.TEXT,
                )
            ],
            new_nodes
        )

    def test_no_images(self):
        node = TextNode(
            ("This is text without images"),
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode(
                ("This is text without images"),
                TextType.TEXT,
                )
            ],
            new_nodes
        )

    def test_images_on_corners(self):
        node = TextNode(
            ("![image](https://i.imgur.com/zjjcJKZ.png)" 
            " and another ![second image](https://i.imgur.com/3elNhQu.png)"),
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_links_on_corners(self):

        node = TextNode(
            ("[to google](https://www.google.com)"
              " and [to youtube](https://www.youtube.com)"
             ),
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("to google", TextType.LINK, "https://www.google.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com"
                ),
            ],
            new_nodes,
        )

    def test_image_no_text(self):

        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_link_no_text(self):
        node = TextNode(
            "[to google](https://www.google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("to google", TextType.LINK, "https://www.google.com"),
            ],
            new_nodes,
        )

    def test_invalid_markdown_image(self):
        node = TextNode(
            "here's some text and invalid image syntax "
            "!(image)[https://i.imgur.com/zjjcJKZ.png]",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
            TextNode(
            "here's some text and invalid image syntax "
            "!(image)[https://i.imgur.com/zjjcJKZ.png]",
            TextType.TEXT,
        )
            ],
            new_nodes
        )

    def test_invalid_markdown_link(self):
        node = TextNode(
            "here's some text and invalid link syntax "
            "(to google)[https://www.google.com]",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
            TextNode(
            "here's some text and invalid link syntax "
            "(to google)[https://www.google.com]",
            TextType.TEXT,
        )
            ],
            new_nodes
        )

    def test_text_to_textnodes_func(self):
        new_nodes = text_to_textnodes(
            ("This is **text** with an _italic_ word and a `code block` "
            "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
                "and a [link](https://boot.dev)")
        )
        self.assertListEqual(
                    [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
                    ],
            new_nodes)


