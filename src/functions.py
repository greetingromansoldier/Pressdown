from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
    # make this work later I guess, I REALLY don't want to do it now
    # if text_node.text_type not in [
    #                                TextType.TEXT, TextType.BOLD, TextType.ITALIC, 
    #                                TextType.CODE, TextType.LINK, TextType.IMAGE
    #                               ]:
    #     raise ValueError("Invalid TextType")

    if text_node.text_type is TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type is TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type is TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type is TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type is TextType.LINK:
        return LeafNode("a", text_node.text, {"href":"some link here"})
    if text_node.text_type is TextType.IMAGE:
        return LeafNode("img", "", {"src": "source", 
                                    "alt":"alt text"})

