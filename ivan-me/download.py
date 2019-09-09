import requests, shutil, os
s='http://cdn.iz.ru/sites/default/files/styles/900x506/public/news-2019-03/BED_1956.jpg'
(dirname, filename) = os.path.split(s)
r = requests.get(s, stream=True)
if r.status_code == 200:
    with open(filename, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
