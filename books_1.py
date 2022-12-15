import json
import requests

name_of_the_book = input()
 
querry = name_of_the_book.lower()
querry = querry.replace(' ', '+')

URL = "https://openlibrary.org/search.json?"
parameters = {
    "q": querry
}

resp = requests.get(URL, parameters)

print(resp.json())['docs'][0]['author_name']

author= resp.json()['docs'][0]['author_name'][0]
first_publish= resp.json()['docs'][0]['first_publish_year']

print("Author of '"+name_of_the_book+"' is "+str(author)+". It was first published in "+str(first_publish))


 