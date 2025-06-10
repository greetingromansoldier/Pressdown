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
        print(f"line_num: {line_num}")
        quote_line_num = 0
        for n in block.strip().split("\n"):
            if n[0] == ">":
                quote_line_num += 1
        if quote_line_num == line_num:
            return BlockType.QUOTE
        else:
            return BlockType.PARAGRAPH
    elif block.strip().split("\n")[0][:2] == "- ":
        return BlockType.UNORDERED_LIST

    else:
        return BlockType.PARAGRAPH

md = """
- hello
>> hello world
 hellooooo world
"""
print(block_to_block_type(md))
