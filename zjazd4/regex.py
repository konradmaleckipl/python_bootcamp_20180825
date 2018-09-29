import re

post_code_pattern = re.compile('\d{2}-\d{3}')
#email_pattern = re.compile('[a-zA-Z0-9]+-[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+')
email_pattern = re.compile('[\w.-]+@[\w.-]+\.[\w]+')
date_pattern = re.compile('[0-9]{2} [a-zA-Z]+ [0-9]{4}')

with open('praca_z_plikami\pliki_wejsciowe\input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

kody = post_code_pattern.findall(text)
print(kody)
maile = email_pattern.findall(text)
print(maile)
daty = date_pattern.findall(text)
print(daty)