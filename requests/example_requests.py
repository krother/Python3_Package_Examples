
import requests

r = requests.get('http://www.academis.eu')
print(r.status_code)
print(r.text[:100])
