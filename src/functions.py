from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
    if text_node.text_type is TextType.TEXT:
        return LeafNode(None, [text_node][0])

