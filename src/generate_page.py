import os
from markdown_to_html_node import markdown_to_html_node
from extract_markdown_title import extract_title

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_source = open(from_path).read()
    template_text = open(template_path).read()

    html_source = markdown_to_html_node(markdown_source).to_html()
    title = extract_title(markdown_source)
    full_html = template_text.replace("{{ Title }}", title).replace("{{ Content }}", html_source)

    dest_file = open(f"{dest_path}/index.html", "w")
    dest_file.write(full_html)

def generate_pages_recursive(dir_path_content: str,
                             template_path: str,
                             dest_dir_path: str
                             ):
    current_path, current_dst = "", ""
    for elem in os.listdir(dir_path_content):
        if os.path.isfile(f"{dir_path_content}/{elem}"):
            generate_page(from_path=f"{dir_path_content}/{elem}",
                          template_path=template_path,
                          dest_path=f"{dest_dir_path}")
        else:
            os.mkdir(path=f"{dest_dir_path}/{elem}")
            current_path, current_dst = generate_pages_recursive(
                dir_path_content=f"{dir_path_content}/{elem}",
                template_path=template_path,
                dest_dir_path=f"{dest_dir_path}/{elem}"
            )
    return current_path, current_dst
            



