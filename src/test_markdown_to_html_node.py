import unittest

from markdown_to_html_node import (
    markdown_to_html_node,
)


class TestMarkdownToHtmlNode(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        print("*"*50)
        print(f"html 2:\n{html}")
        print("*"*50)
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        print("*"*50)
        print(f"html 2:\n{html}")
        print("*"*50)
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

# will be transfered to tests
# md = """
# Hello my little friend. I want some _italic_ text here. This would be awesome. 
# That's a good thing to add **bold text** also, and of course some [image](http://link to an image)
#
# # Heading
#
# ## Heading 2
#
# ####### Heading ???
#
# >THis is quote block with _italic_ text
# >And just another quote text in one block
#
# And here's the much much better block
# with **bolded** text
#
# - unordered list 1
# - unordered list 2
# - unordered list 3
# - unordered list with _italic text_ 4
#
# 1. and this
# 2. is
# 3. some
# 4. ordered list
# 5. with **some bold** and **some italic** text
#
# > this
# > is
# > block
# > quote
#
# ```
# and finally we are **doing** codeblock
# and some other stuff
# ```
# """

# html_page = markdown_to_html_node(md)
# print(html_page)


