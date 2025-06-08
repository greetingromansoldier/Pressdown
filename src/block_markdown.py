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
                return BlockType.PARAGRAPH
            if block[n] == "#":
                head_count += 1
            elif block[n] == " ":
                return BlockType.HEADING
            else:
                return BlockType.PARAGRAPH

        return BlockType.PARAGRAPH
    
    print(block.strip().split("\n"))
    if block.strip().split("\n")[0] == "```" and block.strip().split("\n")[-1] == "```":
        return BlockType.CODE
    else:
        return None

md = """
```
helloworld
```
"""
print(block_to_block_type(md))
