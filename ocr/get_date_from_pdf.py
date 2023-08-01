# import PyPDF2
from pdfreader import SimplePDFViewer
# python -m pip install pdfreader
import datefinder
# https://pypi.org/project/datefinder/
import re
from datetime import datetime

# Install:
# python -m pip install pdfreader
# python -m pip install datefinder

# format
# Extracting a date from a PDF invoice file involves several steps, namely 1) reading the PDF file, 2) extracting the text data from the file, and 3) searching the text for dates, which can appear in a variety of formats. In this case, we will be using the PyPDF2 module to read the PDF and the datefinder module to identify dates within the text.

import dateutil.parser as dparser


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

def get_date_from_pdf(file_path,
                      format_out_list=['%Y'],
                      pattern_clean_list='[^A-Za-z0-9 .-]+',
                      pattern_input_list=[r'\d{2}\.\d{2}\.\d{4}']):
    fd = open(file_path, "rb")
    viewer = SimplePDFViewer(fd)
    viewer.render()

    # text = viewer.canvas.text_content
    text = str(viewer.canvas.strings)
    # text = ''.join(e for e in text if e.isalnum())
    for pattern_clean in pattern_clean_list:
        if pattern_clean == "remove_extra_spaces":
            text = remove_extra_spaces(text)
        elif pattern_clean == "remove_all_spaces":
            text = remove_all_spaces(text)
        elif pattern_clean == "remove_only_single_spaces":
            text = remove_only_single_spaces(text)
        else:
            text = re.sub(pattern_clean, '', text)
        # text = re.sub('\W+', '', text)
        print(text)

        # print(match)
        # date = datetime.strptime(match.group(), '%Y-%m-%d').date()
        # dates = datetime.strptime(match.group(), '%Y').date()

        for pattern in pattern_input_list:

            matches = re.findall(pattern[0], text)
            print(matches, len(matches))
            if len(matches):
                for match in matches:

                    print(pattern[0])
                    datestr = str(match)
                    print(datestr)

                    #date_format='%b%d%Y'
                    if len(pattern) > 1:
                        print(pattern[1])
                        dates = datetime.strptime(datestr, pattern[1])
                    else:
                        dates = dparser.parse(datestr, fuzzy=True)
                    print(dates)

                    out_by_format_list=[]
                    for format_out in format_out_list:
                        out_by_format_list.append(
                            dates.strftime(format_out)
                        )

                    return out_by_format_list
    return []
                #print()
                # current_day = datetime.now().strftime('%Y')
    # dates = datetime.strptime(match.group(), '%Y').date()
    # print(dates)

    # for page_num in range(num_pages):
    #    page_obj = pdf_reader.getPage(page_num)
    #    text += page_obj.extractText()

    # matches = datefinder.find_dates(str(text))

    # for match in matches:
    #    print(match)
    # return match