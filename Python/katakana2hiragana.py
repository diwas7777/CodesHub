'''
Japanese words are always written by katakana， but only hiragana can be searched in the dictionary, 
this script can convert katakana to hiragana quickly.
'''

import re
InputText = 'チョコチョコ'


def ConverHina2kata(InputText):
    ProcessTexts = []
    for gana in InputText:
        if 12448 < int(ord(gana)) < 12543:
            hira = chr(int(ord(gana) - 96))
            ProcessTexts.append(hira)
    OutputText = ''.join(ProcessTexts)
    return OutputText


if re.search(r'^[\u30a0-\u30ff]*?$', InputText) != None:
    print(ConverHina2kata(InputText))
