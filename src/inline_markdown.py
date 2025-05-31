from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)

        new_node = node.text.split(delimiter)
        if (len(new_node) % 2) == 0 and len(new_node) > 1:
            raise Exception("Probably invalid markdown syntax, check for second delimiter")
        else:
            for i in range(0, len(new_node)):
                if (i % 2) == 0:
                    new_nodes.append(TextNode(new_node[i], TextType.TEXT))
                if (i % 2) != 0:
                    new_nodes.append(TextNode(new_node[i], text_type))
            
    return new_nodes

def extract_markdown_images(text):
    output_tuples = []
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    print(matches)
    
