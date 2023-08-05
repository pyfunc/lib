import re
import os
import sys

sys.path.append('../')
from pyfunc.markdown.get_url_list import get_url_list
from pyfunc.markdown.get_dictionary_structure_from_headers_content import get_dictionary_structure_from_headers_content


# markdown_file
# source - path to source folder
# pattern - regular expression pattern for Markdown headers
def create_folders_files(markdown_file="",
                                      path="",
                                      pattern_list=[r'^#{1,6}\s+(.*)$', r'\[([^\]]+)\]\(([^)]+)\)']):

    markdown_data = get_dictionary_structure_from_headers_content(markdown_file)
    for section, content in markdown_data.items():
        #print(f"Section: {section}\nContent: {content}\n")

        for url in get_url_list(section, pattern_list[1]):
            #print(path_folder)
            #exit()
            try:
                path_folder = os.path.join(path, str(url))

                if not os.path.exists(path_folder):
                    os.makedirs(path_folder)

                filename = 'README.md'
                path_file = os.path.join(path_folder, filename)
                print(path_file)
                f = open(path_file, "w")
                f.write(content)
                f.close()

            except Exception as e:
                print(e)
                continue

