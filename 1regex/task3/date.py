import re

def find_dates(text):
    return re.findall(r'\b\d{1,2}\.\d{1,2}\.\d{1,4}\b', text)