def extract_title(markdown: str):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line.strip("# ")
    raise Exception("No title header found in provided markdown")

