import json

import requests

data = {
    "name": "Atharva",
    "age": "19"
}

json_string = json.dumps(data, indent=4)  # have string

# print(json_string)

# converting in json format is called serializing
# from json to string deserialinzation

decoded = json.loads(json_string)  # have dict
# print(decoded);

# if your are reading from the file use dump and load methods

# with open("sample.json") as file:
#     json_string = json.dump(data)

# print(json_stirng)

'''
api = application programming interface
define rules of interaction between software

data type is json - javascript object notation
http protocol 

post- create a resource
,get- read resource
, put - update
, patch - update parts of resource
, delete - delete a resource
;

when u use api there is req of key or authentication for security purpose

there are some public apis which do not req keys

apod api best for me 

'''

'''
Most APIs over the internet happen over HTTP -  a very well-defined protocol.

HTTP has many verbs, but the primary or most-commonly-used HTTP verbs (or methods, as they are properly called) are POST, GET, PUT, PATCH, and DELETE.

The POST verb is most-often utilized to create new resources. Example: create a new user account
The GET method is used to read (or retrieve) a representation of a resource
Example: get information about a user account
PUT is most-often utilized for update capabilities
Example: update all details of a user account
PATCH is used for modify capabilities.
Example: update only 1 or 2 details, like name or age, of a user account
DELETE is pretty easy to understand. It is used to delete a resource
Example: delete a user account
If you wish to deep-dive into the world of HTTP verbs, be sure to pick up Web Development once you complete the basics of Python.
'''

# actual link api GET https://api.nasa.gov/planetary/apod
URL = "https://api.nasa.gov/planetary/apod"

# definging parameters for querry as dict
parameters = {
    "api_key": "OyiFzt09iKde7hCy2Ecki9scNdwdWwVl1qrbIwAl",
    "date": "2003-01-21"
}

# requesting our querry from the api for the data
resp = requests.get(URL, parameters)

print(resp)  # 200 means ok

print(resp.json())  # print the json object received from the api
# majedar atharva bhai

image_link = resp.json()["url"]
print("The link of the image is:"+image_link)
