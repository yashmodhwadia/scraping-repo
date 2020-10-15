import os
from bs4 import BeautifulSoup
import subprocess


p1 = subprocess.run(['ls'], capture_output=True, text=True)
text = str(p1.stdout)

k = []
k = text.split()[1:]

x = 0

for file in k:
    with open(file, 'r') as f:
        data = f.read()
        soup = BeautifulSoup(data, "lxml")
        t = soup.docno.text
        print(t)
        x += 1
        if x==2:
            break
        
    