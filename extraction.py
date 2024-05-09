from bs4 import BeautifulSoup
import re
import pandas as pd

#Using beautifulsoup and regex to extract valuable parts of the document
def extract(filepath):
    filing = open(filepath, "r")
    filing = filing.read()

    doc_start_pattern = re.compile(r'<DOCUMENT>')
    doc_end_pattern = re.compile(r'</DOCUMENT>')
    type_pattern = re.compile(r'<TYPE>[^\n]+')

    doc_start_is = [x.end() for x in doc_start_pattern.finditer(filing)]
    doc_end_is = [x.start() for x in doc_end_pattern.finditer(filing)]

    doc_types = [x[len('<TYPE>'):] for x in type_pattern.findall(filing)]

    document = {}

    for doc_type, doc_start, doc_end in zip(doc_types, doc_start_is, doc_end_is):
        if doc_type == '10-K':
            document[doc_type] = filing[doc_start:doc_end]
    regex = re.compile(r'(>Item(\s|&#160;|&nbsp;)(1A|1B|7A|7|8)\.{0,1})|(ITEM\s(1A|1B|7A|7|8))')
    matches = regex.finditer(document['10-K'])

    # Create the dataframe
    test_df = pd.DataFrame([(x.group(), x.start(), x.end()) for x in matches])

    test_df.columns = ['item', 'start', 'end']
    test_df['item'] = test_df.item.str.lower()

    # Get rid of unnesesary charcters from the dataframe
    test_df.replace('&#160;', ' ', regex=True, inplace=True)
    test_df.replace('&nbsp;', ' ', regex=True, inplace=True)
    test_df.replace(' ', '', regex=True, inplace=True)
    test_df.replace('\.', '', regex=True, inplace=True)
    test_df.replace('>', '', regex=True, inplace=True)

    # Drop duplicates
    pos_dat = test_df.sort_values('start', ascending=True).drop_duplicates(subset=['item'], keep='last')

    # Set item as the dataframe index
    pos_dat.set_index('item', inplace=True)

    # Get Item 7
    item_7_raw = document['10-K'][pos_dat['start'].loc['item7']:pos_dat['start'].loc['item7a']]

    item_7_content = BeautifulSoup(item_7_raw, 'lxml').get_text("\n\n")

    return item_7_content
