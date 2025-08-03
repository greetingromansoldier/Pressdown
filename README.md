# Pressdown

Pressdown (WordPress + Markdown) is a lightweight static site generator written in Python. 

**See it in action:** [https://greetingromansoldier.github.io/Pressdown/](https://greetingromansoldier.github.io/Pressdown/)

-----

## Description

This project is a from-scratch implementation of a static site generator such as _Hugo_. 
It's built entirely in Python, leveraging object-oriented principles and custom data structures 
to handle the conversion process. 
The generator parses Markdown files for both block-level elements 
(like headings, lists, and code blocks) 
and inline elements (like bold, italic, and links) and converts them into valid HTML.

### Core Technologies

* **Python 3 & Standard Library:** Built with vanilla Python, using standard modules like `os`, `shutil`, and `re` for file system operations and RegEx-based text parsing. Each module is validated by a corresponding test suite.

* **Object-Oriented Programming (OOP):** The conversion pipeline is structured around custom classes (`HTMLNode`, `TextNode`, `ParentNode`) that represent the document as a tree. The HTML rendering methods and structural integrity of these classes are thoroughly tested.

* **Unit Testing:** The native `unittest` framework is used to assert the correctness of every component, from individual parsing functions to the end-to-end Markdown-to-HTML conversion logic.

## Why?

As a long-time user of **Obsidian**, I've always been fascinated 
by the simplicity and power of Markdown for organizing thoughts and notes. 

**Pressdown** is the result of that curiosity—an educational 
exercise in understanding the fundamentals of text processing 
and web generation using the tools and logic I use every day.

## Quick Start

Get your site up and running in a few simple steps.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/pressdown.git
    cd pressdown
    ```

2.  **Add your content:**

      * Put your Markdown files (`.md`) inside the `./content` directory. You can create subdirectories to organize your pages.
      * Place your static assets (like `index.css`, images, etc.) inside the `./static` directory.

3.  **Generate the site:**

      * Run the main script from the root directory of the project:

    <!-- end list -->

    ```bash
    python3 src/main.py
    ```

      * Your complete static website will be generated in the `./docs` folder.

-----

## Usage

### Project Structure

The generator relies on a specific folder structure to work correctly:

  * `./content/` - This is where all your Markdown source files live. The generator will recursively search this directory and replicate its structure in the final output. For example, `content/blog/first-post.md` becomes `docs/blog/first-post.html`.
  * `./static/` - This directory is for all static assets. Everything inside it (CSS, JavaScript, images, fonts) is copied directly to the root of the output folder (`./docs/`).
  * `./template.html` - This is the master HTML template for all pages. The generator injects your content into this file. It must contain two placeholders:
      * `{{ Title }}` - This will be replaced by the page's title.
      * `{{ Content }}` - This will be replaced by the generated HTML from your Markdown file.
  * `./docs/` - This is the output directory. It's automatically created and will contain the final, generated static site. You should not edit files in this directory directly, as they will be overwritten.

### Writing Content

The generator automatically extracts the page title from the **first H1 heading** in your Markdown file. Make sure your files start with a title like this:

```markdown
# This Is My Awesome Page Title

This is the first paragraph of my page. The generator will use the heading above as the content for the `{{ Title }}` tag in the template.
```

### Generating the Site for Deployment

The `main.py` script can take an optional command-line argument to set the base path for all links. This is crucial for deploying to subdirectories, like with GitHub Pages.

  * **For local development (or deploying to a root domain):**

    ```bash
    python3 src/main.py
    ```

  * **For GitHub Pages:** If your repository is named `Pressdown` and your GitHub username is `greetingromansoldier`, you would run:

    ```bash
    python3 src/main.py /Pressdown/
    ```

    This command ensures that all links like `href="/index.css"` are correctly rewritten to `href="/Pressdown/index.css"`, preventing broken links on the live site.
