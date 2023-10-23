from createhtml import *
from htmltopdf import *
from sendmail import *

import requests

pokemon = str(input("What is your pokemon?\t"))
api_url = "https://pokeapi.co/api/v2/pokemon/{}".format(pokemon.lower()) 
    
response = requests.get(api_url) # pokemon için api sorgu yapılıyor
    
if response.status_code == 200:
    data = response.json()
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    
    
    ability_descriptions = {}
    
    for ability in abilities:
        ability_url = "https://pokeapi.co/api/v2/ability/{}".format(ability) # pokemon'un yetenekleri için api sorgu yapılıyor
        
        ability_response = requests.get(ability_url)
        
        if ability_response.status_code == 200:
            ability_data = ability_response.json()
            description = ability_data['effect_entries'][1]['effect'] # Yeteneğin açıklaması ingilizce alınıyor. effect_entries[1] ingilizce tanım
            ability_descriptions[ability] = description # açıklama sözlüğe ekleniyor

table = ""
for x,y in ability_descriptions.items():
    table += "".join("<tr><td>{}</td><td>{}</td></tr>".format(x,y))

createHTML(table,pokemon)
html2pdf(pokemon)
#sendMail(pokemon)