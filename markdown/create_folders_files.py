import re
import os
import sys
import string

sys.path.append('../')
from pyfunc.markdown.get_url_list import get_url_list
from pyfunc.markdown.get_dictionary_structure_from_headers_content import get_dictionary_structure_from_headers_content
from pyfunc.markdown.get_dictionary_structure_by_separator_list import get_dictionary_structure_by_separator_list


# markdown_file
# source - path to source folder
# pattern - regular expression pattern for Markdown headers
def create_folders_files(markdown_file="",
                         path="",
                         pattern_list=[r'^#{1,6}\s+(.*)$', r'\[([^\]]+)\]\(([^)]+)\)'],
                         extension_list=['bash', 'php', 'js', 'javascript', 'shell', 'sh'],
                         extension_head_list={
                             'bash': '#!/bin/bash',
                             'shell': '#!/bin/shell',
                             'sh': '#!/bin/sh',
                             'php': '<?php'
                         }
                         ):
    markdown_data = get_dictionary_structure_from_headers_content(markdown_file)
    for section, content in markdown_data.items():
        # print(f"Section: {section}\nContent: {content}\n")
        # print(content.splitlines())
        # exit()
        # markdown_data = get_dictionary_structure_by_separator_list(content.splitlines())

        # print(markdown_data)
        # continue

        for url in get_url_list(section, pattern_list[1]):
            # print(path_folder)
            # exit()
            try:
                path_folder = os.path.join(path, str(url))

                if not os.path.exists(path_folder):
                    os.makedirs(path_folder)

                filename = 'README.md'
                path_file = os.path.join(path_folder, filename)
                # print(path_file)

                f = open(path_file, "w")
                f.write(content)
                f.close()

                code_blocks = get_dictionary_structure_by_separator_list(content)
                for i, block in enumerate(code_blocks, 1):
                    #print(f"Code Block {i}:\n{block}\n")
                    extension = block.splitlines(True)[0]
                    if len(extension) < 1:
                        extension = "txt"
                    else:
                        code_list = extension.split(' ')
                        if len(code_list) >= 1:
                            code = re.sub('[^A-Za-z0-9]+', '', code_list[0])
                            if code in extension_list:
                                extension = code
                                postString = block.split("\n", 1)[1]
                                block = extension_head_list[code] + '\n' + postString
                            else:
                                extension = "txt"
                        else:
                            extension = "txt"

                    path_file = os.path.join(path_folder, "CODE" + str(i) + '.' + extension)
                    f = open(path_file, "w")
                    f.write(block)
                    f.close()


            except Exception as e:
                print(e)
                continue
