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
    print(f"public_path: {public_path}")
    static_path = f"{project_dir_name}/static"
    print(f"static_path: {static_path}")

    if os.path.exists(public_path):
        shutil.rmtree(path=public_path) 
        os.mkdir(public_path)
    else: 
        os.mkdir(public_path)

    def copy_recursive(path: str, dst: str):
        print(f"current path:{path}")
        new_path, new_dst = "", ""
        for elem in os.listdir(path=path):
            print(f"list directory at path:\n{os.listdir(path=path)}")
            print(f"elem: {elem}")
            if os.path.isfile(f"{path}/{elem}"):
                print(f"printing elem because it's file {elem}")
                shutil.copy(src=f"{path}/{elem}", dst=f"{dst}/{elem}")
            else:
                os.mkdir(path=f"{dst}/{elem}")
                new_path, new_dst = copy_recursive(f"{path}/{elem}", f"{dst}/{elem}")
        return new_path, new_dst

    copy_recursive(path=static_path, dst=public_path)

        


if __name__ == "__main__":
    main()

