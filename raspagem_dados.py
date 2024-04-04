  # python -m http.server -d aula_190_site/ 3333  

import requests 
from bs4 import BeautifulSoup
import re
# http:// -> porta 80
# https:// -> porta 443

url = 'http://localhost:3333/'
response = requests.get(url)

print(response.status_code)

if response.status_code == 200:
    raw_html = response.text
    conv_html = BeautifulSoup(raw_html, 'html.parser')
    textos = conv_html.select_one('#intro > div > div > article > h2').parent
    for p in textos:
        print(re.sub(r'\s{1,}', ' ', p.text).strip())   # \s+ tbm funciona
