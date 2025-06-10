from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        new_block = block.strip()
        if len(block) < 1:
            continue
        new_blocks.append(new_block)
    return new_blocks

# takes block of markdown text, returns BlockType which represents type of block it is
def block_to_block_type(block):

    if block[0] == "#":
        head_count = 1
        for n in range(1, 8):
            if head_count > 6:
                continue
            if block[n] == "#":
                head_count += 1
            elif block[n] == " ":
                return BlockType.HEADING
            else:
                continue
    elif block.strip().split("\n")[0] == "```" and block.strip().split("\n")[-1] == "```":
        return BlockType.CODE
    elif block.strip().split("\n")[0][0] == ">":
        line_num = len(block.strip().split("\n"))
        quote_line_num = 0
        for n in block.strip().split("\n"):
            if n[0] == ">":
                quote_line_num += 1
        if quote_line_num == line_num:
            return BlockType.QUOTE
        raise Exception("Markdown Quote Block is not properly formatted")
    elif block.strip().split("\n")[0][:2] == "- ":
        line_num = 0
        list_line_num = 0
        for n in block.strip().split("\n"):
            line_num += 1
            if n[:2] == "- ":
                list_line_num += 1
        if line_num == list_line_num:
            return BlockType.UNORDERED_LIST
        raise Exception("Unordered Markdown List is not properly formatted")
    elif block.strip().split("\n")[0][:2] == "1.":
        line_num = 0
        list_line_num = 0
        for n in block.strip().split("\n"):
            line_num += 1
            print(f"n[:2]: {n[:2]}\line_num: {line_num}")
            if (
                # I wanted add some other check here but don't remember 
                # what in particular

                # YEP THIS: check if number line de facto is the same as
                # number which expected in list order
                n[:2] == f"{line_num}."
            ):
                list_line_num += 1
            raise Exception("Ordered Markdown List is not properly formatted")
        if line_num == list_line_num:
            return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

md = """
1. sdfsdf
2. sdfsdf
3. sdfsdf
"""
print(block_to_block_type(md))
