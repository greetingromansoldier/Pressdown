import os
import shutil

def copy_static():
    file_abs_path = os.path.abspath(__file__)
    project_dir_name = os.path.dirname(os.path.dirname(file_abs_path))

    public_path = f"{project_dir_name}/public"
    static_path = f"{project_dir_name}/static"

    if os.path.exists(public_path):
        shutil.rmtree(path=public_path) 
        os.mkdir(public_path)
    else: 
        os.mkdir(public_path)

    def copy_recursive(path: str, dst: str):
        new_path, new_dst = "", ""
        for elem in os.listdir(path=path):
            if os.path.isfile(f"{path}/{elem}"):
                shutil.copy(src=f"{path}/{elem}", dst=f"{dst}/{elem}")
            else:
                os.mkdir(path=f"{dst}/{elem}")
                new_path, new_dst = copy_recursive(f"{path}/{elem}", f"{dst}/{elem}")
        return new_path, new_dst

    copy_recursive(path=static_path, dst=public_path)
