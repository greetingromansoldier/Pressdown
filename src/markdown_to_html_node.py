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
import textnode

# for now I not only do code for nodes but also use node.to_html()
# for representing results and checking if it works as intended
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
            print(f"unordered list transformed to html:\n"
                  +f"{markdown_ordered_list_to_html_node(block)}"
                  )
            print("*"*50)
    return blocks
    
def markdown_paragraph_to_html_node(block):
    print("="*50)
    print(f"func md paragraph to html node, block:\n{block}")
    text_nodes = text_to_textnodes(block)
    html_nodes = []
    parent = ParentNode(tag="p", children=html_nodes)
    print(f"func md paragraph to html node, text_node:\n{text_nodes}")
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
        print(f"node in textnodes:{node}")
    print(f"func md paragraph to html node, html_nodes:\n{html_nodes}")
    print(parent.to_html())

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
    children = block_to_children(block)
    unordered_list_parent = ParentNode(tag="ul", children=children)
    return unordered_list_parent.to_html()

def markdown_ordered_list_to_html_node(block):
    children = block_to_children(block)
    unordered_list_parent = ParentNode(tag="ol", children=children)
    return unordered_list_parent.to_html()

def block_to_children(block):
    if block_to_block_type(block) == BlockType.UNORDERED_LIST:
        block_values = []
        list_elem_nodes = []
        for inline in block.split("1. "):
            if inline != "":
                block_values.append(inline.strip("\n"))
        for value in block_values:
            text_nodes = text_to_textnodes(value)
            html_nodes = []
            for node in text_nodes:
                html_nodes.append(text_node_to_html_node(node))
            parent = ParentNode(tag="li", children=html_nodes)
            list_elem_nodes.append(parent)
        return list_elem_nodes
    elif block_to_block_type(block) == BlockType.ORDERED_LIST:
        block_values = []
        list_elem_nodes = []
        for inline in block.split("- "):
            if inline != "":
                block_values.append(inline.strip("\n"))
        for value in block_values:
            text_nodes = text_to_textnodes(value)
            html_nodes = []
            for node in text_nodes:
                html_nodes.append(text_node_to_html_node(node))
            parent = ParentNode(tag="li", children=html_nodes)
            list_elem_nodes.append(parent)
        return list_elem_nodes





md = """
Hello my little friend. I want some _italic_ text here. This would be awesome. 
That's a good thing to add **bold text** also, and of course some [image](http://link to an image)

# Heading

## Heading 2

####### Heading ???

>THis is block with *italic* text
>And just another text in one block

And here's the much much better block
with **bolded** text

- unordered list 1
- unordered list 2
- unordered list 3
- unordered list with _italic text_ 4

1. and this
2. is
3. some
4. ordered list
5. with **some bold** and _some italic_ text
"""

markdown_to_html_node(md)

# ok. I am overwhelmed and unerstand kind of NOTHING
# and it's the time to prepare food for a week
