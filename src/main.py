from textnode import TextNode


def main():
    test_obj = TextNode("Some Text", "link", "https://www.google.com")
    print(test_obj.__repr__())

if __name__ == "__main__":
    main()

