from text_node_to_html_node import text_node_to_html_node
from textnode import (
    TextType,
    TextNode,
)
from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode
)
from inline_markdown import (
    text_to_textnodes,
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
            print(f"unordered list transformed to html:\n"
                  +f"{markdown_unordered_list_to_html_node(block)}"
                  )
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

def markdown_unordered_list_to_html_node(block):
    
    def extract_text(md_block):
        new_text = ""
        for line in block.split("\n"):
            new_text += line[2:] + "\n"
        return new_text.rstrip("\n")

    child_nodes = text_to_children(extract_text(block))

    # for child in child_nodes:
    #     if child.TextType == 

    parent_node = ParentNode(tag="ul", children=child_nodes,)
    return parent_node.to_html()

def text_to_children(text):
    child_nodes = []
    for node in text_to_textnodes(text):
        print(f"node:{node}")
        child_nodes.append(text_node_to_html_node(node))
    return child_nodes

    # children = []
    # text = text.split("\n")
    # for obj in text:
    #     child = LeafNode(tag="li", value=obj)
    #     children.append(child)
    # return children



md = """
Hello

# Heading

## Heading 2

>THis is block with *italic* text
>And just another text in one block

And here's the much much better block
with **bolded** text

- unordered list 1
- unordered list 2
- unordered list 3
- unordered list with _italic text_ 4
"""

markdown_to_html_node(md)

# ok. I am overwhelmed and unerstand kind of NOTHING
# and it's the time to prepare food for a week
