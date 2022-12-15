import json
import requests
def get_subject(name_of_the_book):
    querry = name_of_the_book.lower()
    querry = querry.replace(' ', '+')
    URL = "https://openlibrary.org/search.json?title="
    parameters = {
        "q": querry
    }
    resp = requests.get(f"https://openlibrary.org/search.json?title={querry}")
    subjects= resp.json()['docs'][0]['subject']
    return subjects
# print(get_subject(sub1))
# print(get_subject(sub2))

s1=set(get_subject(sub1))
s2= set(get_subject(sub2))

common = s1 & s2 
common = list(common)
common.sort()

print("Common subjects are:",end=" ")
for subject in common:
    print(subject, end=' ')
print()
