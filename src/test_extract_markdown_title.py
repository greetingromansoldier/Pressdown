import unittest

from extract_markdown_title import extract_title

class TestExtractMarkdownTitle(unittest.TestCase):

    def test_one_line(self):
        markdown = "# Hello"
        result = "Hello"
        self.assertEqual(
            extract_title(markdown),
            result
        )
    
    def test_blocks(self):
        markdown = """There's some text
And # False heading
# And here's real heading which should be considered as Title
"""
        result = "And here's real heading which should be considered as Title"
        self.assertEqual(
            extract_title(markdown),
            result
        )

    def test_exception(self):
        markdown = """There's no heading

## Only h2 heading 
"""
        with self.assertRaises(Exception):
            extract_title(markdown)








