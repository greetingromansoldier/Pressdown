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

# for now I not only do code for nodes but also use node.to_html()
# for representing results to myself and checking if it works like it supposed to
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.PARAGRAPH:
            print(f"'{block}'\nis paragraph")
            print(f"Results of to_html func:\n{markdown_paragraph_to_html_node(block)}")
            print("*"*50)
        if block_to_block_type(block) == BlockType.HEADING:
            print(f"'{block}'\nis heading")
            print(f"Results of to_html func:\n"+
                  f"{markdown_heading_to_html_node(block)}")
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
    
def markdown_paragraph_to_html_node(block):
    node = LeafNode(tag="p", value=block, props=None)
    html_text = node.to_html()
    return html_text # making it text only for the test representation

def markdown_heading_to_html_node(block):
    # find a way to count # in markdown headings and turn into h1-h6 for html
    heading_value = 0
    block_value = ""
    if block.startswith("# "):
        heading_value = 1
        block_value = block.strip().split("#")[1].strip()
    elif block.startswith("## "):
        heading_value = 2
        block_value = block.strip().split("##")[1].strip()
    elif block.startswith("### "):
        heading_value = 3
        block_value = block.strip().split("###")[1].strip()
    elif block.startswith("#### "):
        heading_value = 4
        block_value = block.strip().split("####")[1].strip()
    elif block.startswith("##### "):
        heading_value = 5
        block_value = block.strip().split("#####")[1].strip()
    elif block.startswith("###### "):
        heading_value = 6
        block_value = block.strip().split("######")[1].strip()
    node = LeafNode(tag=f'h{heading_value}', value=block_value, props=None)
    return node.to_html()


md = """
Hello

# Heading

## Heading 2

>THis is block with *italic* text
>And just another text in one block

And here's the much much better block
with **bolded** text
"""

markdown_to_html_node(md)

# ok. I am overwhelmed and unerstand kind of NOTHING
# and it's the time to prepare food for a week
