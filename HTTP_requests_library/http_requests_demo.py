# %%
import requests
import pprint
# r = requests.get('https://requests.readthedocs.io/en/master/')
r = requests.get('https://www.google.com')
print(r.status_code)

if r:
    print('Success!')
else:
    print('Fail')

pprint.pprint(r.text)
print(r.url)
print(r.headers)
print(r.encoding)
print(r.headers['content-type'])

# import pprint
# pprint.pprint(r.__dict__)
# import json
# def serialize(obj):
#     if isinstance(obj, bytes):
#         return obj.decode('utf-8', errors='ignore')  # Convert bytes to string
#     return str(obj)  # Convert other objects to strings
#
# # Serialize the dictionary safely
# print(json.dumps(r.__dict__, indent=4, default=serialize))

def google_search(query, num):
    r = requests.get('https://search.yahoo.com',
                     params={'q': query, 'num': num})
    return r.url


print(google_search('euro to rupees', 10))

# https://www.google.com/search?q=python#=1

# %%
import requests


url = 'https://docs.python.org/3/'
r = requests.get(url)

if r.encoding == 'ISO-8859-1':
    print('Right encoding!')
else:
    print('You should change the encoding.')

# %%
r = requests.get("https://requests.readthedocs.io/en/master/user/quickstart/")
pprint.pprint(r.text)

# %%
r = requests.get('https://api.github.com/events')
r.json()