import os
import sys
from textnode import TextNode
from copystatic import copy_static
from generate_page import generate_page, generate_pages_recursive

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"    
    print("Deleting public directory and copying static files to public directory...")
    copy_static(path=f"static", dst=f"docs")

    # file_abs_path = os.path.abspath(__file__)
    # project_dir_name = os.path.dirname(os.path.dirname(file_abs_path))

    generate_pages_recursive(
        dir_path_content=f"content", 
        template_path=f"template.html", 
        dest_dir_path=f"docs",
        basepath=basepath
                            )

if __name__ == "__main__":
    main()

