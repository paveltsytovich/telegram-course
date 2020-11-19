import os

def filter_handler(message):
    result = message
    path = os.getcwd() + '\\data\\'
    with open(path + 'bad_words.txt',encoding='utf-8') as b:
        bads = [ c[:len(c)-1] for c in b]
    for c in bads:
        result = result.replace(c,'***')
    return result