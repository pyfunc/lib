import re
import os
import sys

sys.path.append('../')
from pyfunc.markdown.get_url_list import get_url_list
from pyfunc.markdown.get_header_list import get_header_list


# markdown_file
# source - path to source folder
# pattern - regular expression pattern for Markdown headers
def get_dictionary_structure_by_separator_list2(markdown_lines = [], separator_list=['```bash', '```']):
    data = {}
    current_section = None

    h1 = separator_list[0]
    h2 = separator_list[1]
    for line in markdown_lines:
        if line.startswith(h1):
            current_section = line.strip().replace(h1, "")
            data[current_section] = ""
        elif line.startswith(h2):
            current_section = line.strip().replace(h2, "")
            data[current_section] = ""
        elif current_section is not None:
            data[current_section] += line

    return data

def get_dictionary_structure_by_separator_list(markdown = "", separator_list=['```bash', '```']):

    pattern = re.compile(r'`{3}.*?`{3}|`.*?`', re.DOTALL)
    code_blocks = pattern.findall(markdown)

    # remove back ticks
    code_blocks = [block.replace('`', '') for block in code_blocks]

    return code_blocks


