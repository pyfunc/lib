# import PyPDF2
from pdfreader import SimplePDFViewer
# python -m pip install pdfreader
import datefinder
# https://pypi.org/project/datefinder/
import re
import numpy as np
from datetime import datetime

# Install:
# python -m pip install pdfreader
# python -m pip install datefinder

# format
# Extracting a date from a PDF invoice file involves several steps, namely 1) reading the PDF file, 2) extracting the text data from the file, and 3) searching the text for dates, which can appear in a variety of formats. In this case, we will be using the PyPDF2 module to read the PDF and the datefinder module to identify dates within the text.

import dateutil.parser as dparser

import sys
from pypdf import PdfReader


# pip3 install pypdf

def convertPdf2String(path):
    # load PDF file
    reader = PdfReader(path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    return text


# https://dateutil.readthedocs.io/en/stable/parser.html
# pip install python-dateutil
def remove_extra_spaces(text):
    no_extra_spaces_text = ' '.join(text.split())
    return no_extra_spaces_text


def remove_all_spaces(text):
    no_spaces_text = text.replace(" ", "")
    return no_spaces_text


def remove_only_single_spaces(text):
    return re.sub(r'(?<=\S) (?=\S)', '', text)


def remove_new_lines(text):
    text_out = text.replace("\n", "")
    return text_out


def find_string_in_pdf(file_path, find_text="", find_text_list=[]):
    fd = open(file_path, "rb")

    # text = convertPdf2String(fd).encode("ascii", "xmlcharrefreplace")
    text = convertPdf2String(fd)
    text = text.lower()
    text = remove_new_lines(text)

    find_text = find_text.lower()
    find_text_list = [find_text]

    # print("find_string_in_pdf find_text_list: ", find_text, find_text_list)

    # if len(find_text) > 2:
    #    find_text_list.append(find_text)

    if len(find_text_list) < 1:
        print("find_text_list empty")
        exit()

    text_list_out = multiple_search(text, find_text_list, [])

    if not text_list_out:
        text = remove_only_single_spaces(text)
        # print(text)
        text_list_out = multiple_search(text, find_text_list)

    # print("text_list_out: ", text_list_out)
    return text_list_out
    # return [file_path, text_list_out]


def multiple_search(text, search_list=[], text_list_out=[]):
    text_occ_list = {}
    # print(search_list)

    for search in search_list:

        matches = text.find(search)
        # print(text, search, matches, len(search))
        # print(search, matches, len(search))

        if matches >= 0:
            # text_list_out.append(text)
            text_occ_list[search] = matches

    sorted(text_occ_list)
    # print("text_occ_list: ", text_occ_list)
    text_list_out = list(text_occ_list.keys())

    # print("text_list_out: ", text_list_out)

    return text_list_out
