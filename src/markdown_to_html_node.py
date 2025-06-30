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
        
    # html_node = text_node_to_html_node(text_nodes)
    # print(f"func md paragraph to html node, html_node:\n{html_node}")
    # html_node = LeafNode(tag="p", value=block, props=None)
    # html_text = html_node.to_html()
    # return html_text # making it text only for the test representation

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

    parent_list_elems = []
    list_elem_inline = []

    parent_list = ParentNode(tag="ul", children=parent_list_elems)
    return block_to_children(block)

def block_to_children(block):
    if block_to_block_type(block) == BlockType.UNORDERED_LIST:
        block_values = []
        for inline in block.split("- "):
            if inline != "":
                block_values.append(inline.strip("\n"))
        return block_values

    # children = []
    # text = text.split("\n")
    # for obj in text:
    #     child = LeafNode(tag="li", value=obj)
    #     children.append(child)
    # return children



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
"""

markdown_to_html_node(md)

# ok. I am overwhelmed and unerstand kind of NOTHING
# and it's the time to prepare food for a week
