from textnode import (
    TextType,
    TextNode,
    text_node_to_html_node
)
from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode
)
from block_markdown import (
    BlockType,
    markdown_to_blocks, 
    block_to_block_type
)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.PARAGRAPH:
            print(f"'{block}'\nis paragraph")
            print(f"Results of to_html func:\n{block_is_paragraph(block)}")
            print("*"*50)
        if block_to_block_type(block) == BlockType.HEADING:
            print(f"'{block}'\nis heading")
            print("*"*50)
        if block_to_block_type(block) == BlockType.CODE:
            print(f"'{block}'\nis code")
            print("*"*50)
        if block_to_block_type(block) == BlockType.QUOTE:
            print(f"'{block}'\nis quote")
            print("*"*50)
        if block_to_block_type(block) == BlockType.UNORDERED_LIST:
            print(f"'{block}'\nis unordered list")
            print("*"*50)
        if block_to_block_type(block) == BlockType.ORDERED_LIST:
            print(f"'{block}'\nis ordered list")
            print("*"*50)
    return blocks
    
def block_is_paragraph(block):
    node = LeafNode("p", None, block)
    node.to_html()
    return(node)


md = """
Hello

>THis is block with *italic* text
>And just another text in one block

And here's the much much better block
with **bolded** text
"""

markdown_to_html_node(md)

# ok. I am overwhelmed and unerstand kind of NOTHING
# and it's the time to prepare food for a weak
