import os
import shutil

def copy_static(path: str, dst: str):

    if os.path.exists(dst):
        shutil.rmtree(path=dst) 
        os.mkdir(dst)
    else: 
        os.mkdir(dst)

    def copy_recursive(path: str, dst: str):
        new_path, new_dst = "", ""
        for elem in os.listdir(path=path):
            if os.path.isfile(f"{path}/{elem}"):
                shutil.copy(src=f"{path}/{elem}", dst=f"{dst}/{elem}")
            else:
                os.mkdir(path=f"{dst}/{elem}")
                new_path, new_dst = copy_recursive(f"{path}/{elem}", f"{dst}/{elem}")
        return new_path, new_dst

    copy_recursive(path=path, dst=dst)
