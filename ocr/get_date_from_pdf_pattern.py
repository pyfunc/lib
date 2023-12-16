class get_date_from_pdf_pattern():
    format_out_list = ['%Y', '%m.%Y']

    pattern_clean_list = ['[^A-Za-z0-9 .\-\/]+', 'remove_all_spaces']

    ##def pattern_clean_list = ['[^A-Za-z0-9 .-]+', '[^A-Za-z0-9.-]+'],

    pattern_input_list = [
        #[r'\d{2}\.\d{2}\.\d{4}'],
        [r'\d{4}\.\d{2}\.\d{2}'],
        [r'\d{4}-\d{2}-\d{2}', '%Y-%m-%d'],
        [r'\d{2}-\d{2}-\d{4}', '%d-%m-%Y'],
        [r'Order Date (\d{1,2}\/\d{1,2}\/\d{4})', '%m/%d/%Y'],
        [r'\d{1,2}\/\d{1,2}\/\d{4}', '%d/%m/%Y'],
        [r'\d{1,2}\. \w{2,5} \d{4}'],

        [r'ate (\d{1,2} \w{3} \d{4})', '%d %b %Y'],
        [r'ate(\d{1,2}t\w{3}t\d{4})', r't', '%d%b%Y'],
        [r'ate (\d{1,2}th \w{3} \d{4})', r'(?<=\d)(st|nd|rd|th)\b|\s', '%d%b%Y'],
        [r'ate (\w{3,12} \w{3,12} \d{1,2}\w{2} \w{4})', r'(?<=\d)(st|nd|rd|th)\b|\s', '%A%B%d%Y'],
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
