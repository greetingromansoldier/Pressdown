def extract_title(markdown: str):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:]
    raise Exception("No title found in provided markdown")

