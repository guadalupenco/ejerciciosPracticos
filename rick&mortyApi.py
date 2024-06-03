
import requests
import json

#request simple
url = "https://rickandmortyapi.com/api/character/2"
r = requests.get(url)
j = r.json()

status = j["status"]
print(status)

i = 1

while i < 11:

        url = "https://rickandmortyapi.com/api/character/{}".format(i)
        r = requests.get(url)
        j = r.json()
        name = j["name"]
        status = j["status"]
        print("El personaje {} tiene status: {}".format(name,status))
        i += 1



#request al primer episodio
url = "https://rickandmortyapi.com/api/episode/1"
r = requests.get(url)
j = r.json()
personajes = j["characters"]
list_names_human = list()
list_names_other = list()

for personaje in personajes:
    req = requests.get(personaje)
    js = req.json()
    name = js["name"]
    if js["species"] == "Human":
        list_names_human.append(name)
    else:
        list_names_other.append(name)


print(list_names_human)
print(list_names_other)

    






