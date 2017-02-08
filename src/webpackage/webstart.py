# Created by labattula on 13/01/16.

import requests

r = requests.get('https://api.github.com/events')
print(r.text)
print(r.status_code)