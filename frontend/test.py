import requests

r=requests.get('http://130.61.244.34:5000/sentence')
print(r.json()['sentence'])