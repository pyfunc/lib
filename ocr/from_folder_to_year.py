import os
import datetime
import dateutil.parser as dparser
# pip3 install python-dateutil
# pip3 install pillow
# pip3 install image
# pip3 install regex
import sys

sys.path.append('../')
from pyfunc.ocr.get_date_from_pdf import get_date_from_pdf


# move from IN to selected month
def from_folder_to_year(source="./", subfolder="", extension_list=['.pdf']):
    # print(source, dest)
    root = '../'
    # path = os.path.join(root, source)
    paths = source
    if not os.path.exists(paths):
        print(f"folder not exist {paths}")
        exit()

    for directory, subdir_list, file_list in os.walk(paths):
        for name in file_list:
            for extension in extension_list:
                if name.endswith(extension):
                    print(name)
                    path_in = os.path.join(directory, name)
                    print("path_in: ", path_in)
                    # timestamp = os.path.getmtime(source_name)
                    try:
                        invoice_date = get_date_from_pdf(
                            path_in,
                            ['%Y', '%m.%Y'],
                            # ['[^A-Za-z0-9 .-]+', '[^A-Za-z0-9.-]+'],
                            ['[^A-Za-z0-9 .\-\/]+', 'remove_all_spaces'],
                            [
                                [r'\d{2}\.\d{2}\.\d{4}'],
                                [r'\d{4}\.\d{2}\.\d{2}'],
                                [r'\d{4}-\d{2}-\d{2}', '%Y-%m-%d'],
                                [r'\d{2}-\d{2}-\d{4}', '%d-%m-%Y'],
                                [r'\d{1,2}\/\d{1,2}\/\d{4}', '%d/%m/%Y'],
                                [r'\d{1,2}\. \w{2,5} \d{4}'],

                                [r'ate (\d{1,2} \w{3} \d{4})', '%d %b %Y'],
                                [r'ate(\d{1,2}t\w{3}t\d{4})', r't', '%d%b%Y'],
                                [r'ate (\d{1,2}th \w{3} \d{4})', r'(?<=\d)(st|nd|rd|th)\b|\s', '%d%b%Y'],
                                [r'ate (\w{3,12} \w{3,12} \d{1,2}\w{2} \w{4})', r'(?<=\d)(st|nd|rd|th)\b|\s',
                                 '%A%B%d%Y'],
                                [r'ays(\d{1,2}\w{3,14}\d{4})', r'st|nd|rd|th', '%d%B%Y'],

                                [r'issue(\w{3,12}\d{5,6})', '%B%d%Y'],
                                [r'due(\w{3}\d{5,6})', '%b%d%Y'],
                                [r'Address(\w{3}\d{5,6})', '%b%d%Y'],
                                [r'due(\w{3,12}\d{5,6})', '%B%d%Y'],
                                [r'on(\w{3,12}\d{5,6})', '%B%d%Y'],
                                [r'paid(\w{3,12}\d{5,6})', '%B%d%Y'],

                                [r'Date (\d{6,8})', '%d%m%Y'],
                                [r'DATE (\d{6,8})', '%d%m%Y'],
                                [r'CI (\d{6,8})', '%d%m%Y'],
                                [r'PAID (\d{6,8})', '%d%m%Y'],

                                # [r'\d{2}\w{3}\d{4}'],
                                [r'\w{3}\d{1,2},\d{4}'],
                                [r'Date\s+:\s+(\d+ .+ \d{4})'],

                            ]
                        )

                        if len(invoice_date):
                            print("invoice_date: ", invoice_date)

                            path_folder = os.path.join(root, str(invoice_date[0]), "expenses",
                                                       str(invoice_date[1]), subfolder)
                            print("path_folder: ", path_folder)

                            if not os.path.exists(path_folder):
                                os.makedirs(path_folder)

                            path_out = os.path.join(path_folder, name)

                            print(path_out)
                            # exit()
                            # modified_date = str(datetime.datetime.fromtimestamp(timestamp)).replace(':', '.')
                            # target_name = os.path.join(directory, f'{modified_date}_{name}')
                            # target_name = os.path.join(directory, f'{modified_date}_{name}')

                            print(f'FROM: {path_in} TO: {path_out}')
                            os.rename(path_in, path_out)
                    except Exception as e:
                        print(e)
                        continue
                    # exit()
