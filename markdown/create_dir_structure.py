import os
import mistune
from mistune import HTMLRenderer

def create_dir_structure(md_text, base_dir):
    #renderer = HeaderRenderer()
    #renderer = mistune.HTMLRenderer()
    renderer = mistune.HTMLRenderer()
    #markdown = mistune.Markdown(renderer, plugins=[strikethrough])
    markdown = mistune.Markdown(renderer)
    #markdown = mistune.Markdown(renderer=renderer)
    headers = markdown(md_text).split('\n')
    print(headers)

    for header in headers:
        if header:  # Exclude empty directories
            pathf = os.path.join(base_dir, header)
            print(pathf)
            os.makedirs(pathf, exist_ok=True)

