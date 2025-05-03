import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    pass

# if __name__ == "__main__":
#     unittest.main()

node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

# node = ParentNode(
#     "p",
#     [
#     ],
# )
print(node.to_html())
