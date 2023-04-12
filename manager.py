import os
import json 
import requests

import glob as gl

date = {
    'teste': 'teste'
}

for i in range(10):
    file = open(fr'.\arquivos\arquivo_{i}.json', 'x')
    file.write(date)
    file.close()

gl.glob(r'.\arquivos\arquivo_*.txt')