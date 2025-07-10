import os
from os.path import isfile
import shutil 
from textnode import TextNode


def main():
    test_obj = TextNode("Some Text", "link", "https://www.google.com")
    print(test_obj.__repr__())
    current_directory = os.getcwd()
    print(f"current_directory {current_directory}")
    file_abs_path = os.path.abspath(__file__)
    print(f"probably path to the executed file:{file_abs_path}")
    project_dir_name = os.path.dirname(os.path.dirname(file_abs_path))
    print(f"probably path to directory where executed file is:{project_dir_name}")

    public_path = f"{project_dir_name}/public"
    static_files = os.listdir(path=f"{project_dir_name}/static")

    print(static_files)
    for elem in static_files:
        print(elem)
        if os.path.isfile(f"{project_dir_name}/static/{elem}"):
            print(f"printing elem because it's file {elem}")
    
    if os.path.exists(public_path):
        shutil.rmtree(path=public_path) 
        os.mkdir(public_path)
    else: 
        os.mkdir(public_path)


if __name__ == "__main__":
    main()

