import os
from textnode import TextNode
from copystatic import copy_static
from generate_page import generate_page, generate_pages_recursive

def main():
    test_obj = TextNode("Some Text", "link", "https://www.google.com")
    print(test_obj.__repr__())
    print("Deleting public directory and copying static files to public directory...")
    copy_static()

    file_abs_path = os.path.abspath(__file__)
    project_dir_name = os.path.dirname(os.path.dirname(file_abs_path))

    generate_pages_recursive(
        dir_path_content=f"{project_dir_name}/content", 
        template_path=f"{project_dir_name}/template.html", 
        dest_dir_path=f"{project_dir_name}/public"
                            )

if __name__ == "__main__":
    main()

