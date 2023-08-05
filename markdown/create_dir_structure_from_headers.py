import re

def create_dir_structure_from_headers(filename, base_dir):

    with open(filename, 'r') as f:
        content = f.read()

    # Regular expression pattern for Markdown headers
    pattern = r'^#{1,6}\s+(.*)$'

    headers = re.findall(pattern, content, re.MULTILINE)

    for header in headers:
        print(header)
