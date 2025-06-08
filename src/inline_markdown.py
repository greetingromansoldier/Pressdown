from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        new_node = node.text.split(delimiter)
        if (len(new_node) % 2) == 0 and len(new_node) > 1:
            raise Exception("Probably invalid markdown syntax, check for second delimiter")
        else:
            for i in range(0, len(new_node)):
                if new_node[i] == "":
                    continue
                if (i % 2) == 0:
                    new_nodes.append(TextNode(new_node[i], TextType.TEXT))
                if (i % 2) != 0:
                    new_nodes.append(TextNode(new_node[i], text_type))
            
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text_yet = node.text

        while len(extract_markdown_images(text_yet)) > 0:
            image_alt = extract_markdown_images(text_yet)[0][0]
            image_link = extract_markdown_images(text_yet)[0][1]

            sections = text_yet.split(f"![{image_alt}]({image_link})", 1)
            before_image, after_image = sections[0], sections[1]

            if len(before_image) > 0:
                before_text = TextNode(before_image, TextType.TEXT)
                new_nodes.append(before_text)

            image_node = TextNode(image_alt, TextType.IMAGE, image_link)
            new_nodes.append(image_node)
            text_yet = after_image

        if len(text_yet) > 0 and text_yet != "":
            new_nodes.append(TextNode(text_yet, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text_yet = node.text

        while len(extract_markdown_links(text_yet)) > 0:
            link_alt = extract_markdown_links(text_yet)[0][0]
            link_link = extract_markdown_links(text_yet)[0][1]

            sections = text_yet.split(f"[{link_alt}]({link_link})", 1)
            before_link, after_link = sections[0], sections[1]

            if len(before_link) > 0:
                before_text = TextNode(before_link, TextType.TEXT)
                new_nodes.append(before_text)

            image_node = TextNode(link_alt, TextType.LINK, link_link)
            new_nodes.append(image_node)
            text_yet = after_link

        if len(text_yet) > 0 and text_yet != "":
            new_nodes.append(TextNode(text_yet, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes




