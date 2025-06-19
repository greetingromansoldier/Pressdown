import unittest
from block_markdown import (
    BlockType,
    markdown_to_blocks,
    block_to_block_type
)

class TestBlockMarkdown(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

# == Here are tests for checking block type ==

    def test_block_type_text(self):
        md_text = """
Just a raw text here
"""
        block = markdown_to_blocks(md_text)
        print(f"md_text: {md_text}")
        print(f"block: {block}")


md_text = """
paragraph here

#looks like heading but this is paragraph

# heading 1

##### heading 5

```code must be here```

> some
> quotes
> here

- just
- unordered
- list

1. Just an ordered list here
2. another text
"""
blocks = markdown_to_blocks(md_text)
print(f"md_text: {md_text}")
print(f"block: {blocks}")
print("="*50)
for block in blocks:
    block_type = block_to_block_type(block)
    print(f"current block:\n{block}")
    print(f"block_type:\n{block_type}")
    print(f"-"*50)

