import re
import os
from bs4 import BeautifulSoup

for filename in os.listdir("."):
    f = os.path.join(os.getcwd(), filename)
    if os.path.isfile(f):
        with open(f, 'r') as file:
            soup = BeautifulSoup(file, 'lxml')
            new_hrefs=[]
            for link in soup.find_all('a'):
                new_hrefs.append(link.get('href'))
                new_hrefs=list(filter(None, new_hrefs))
            for i in new_hrefs:
                file2 = open('hrefs.txt', 'a')
                file2.write(i + '\n')
                file2.close()