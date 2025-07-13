from textnode import TextNode
from copystatic import copy_static

def main():
    test_obj = TextNode("Some Text", "link", "https://www.google.com")
    print(test_obj.__repr__())
    print("Deleting public directory and copying static files to public directory...")
    copy_static()

if __name__ == "__main__":
    main()

