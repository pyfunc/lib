import re
import os
import sys

sys.path.append('../')
from pyfunc.markdown.get_url_list import get_url_list
from pyfunc.markdown.get_header_list import get_header_list


# markdown_file
# source - path to source folder
# pattern - regular expression pattern for Markdown headers
def get_dictionary_structure_from_headers_content(markdown_file=""):
    with open(markdown_file, 'r') as file:
        lines = file.readlines()

    data = {}
    current_section = None

    for line in lines:
        if line.startswith('# '):
            current_section = line.strip().replace("# ", "")
            data[current_section] = ""
        elif line.startswith('## '):
            current_section = line.strip().replace("## ", "")
            data[current_section] = ""
        elif current_section is not None:
            data[current_section] += line

    return data
