from createhtml import *
from htmltopdf import *
from sendmail import *

import requests



def getPokemonResponse(pokemon):
    return requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(pokemon.lower())) # pokemon için api sorgu yapılıyor

def getAbilityResponse(ability):
    return requests.get("https://pokeapi.co/api/v2/ability/{}".format(ability)) # pokemon'un yetenekleri için api sorgu yapılıyor)


def setDict(data):

    abilities = [ability['ability']['name'] for ability in data['abilities']]
        
    ability_descriptions = {}
        
    for ability in abilities:
        if getAbilityResponse(ability).status_code == 200:
            ability_descriptions[ability] = getAbilityResponse(ability).json()['effect_entries'][1]['effect'] # Yeteneğin açıklaması ingilizce alınıyor. effect_entries[1] ingilizce tanım
    
    return ability_descriptions

def setTable(pokemon):

    data = setDict(getPokemonResponse(pokemon).json())

    info = ""
    for x,y in data.items():
        info += "".join("<tr><td>{}</td><td>{}</td></tr>".format(x,y))
    
    return """
    <table> 
        <h2>{0}</h2>
            <tr>
                <th>Ability</th>
                <th>Description</th>
            </tr>
            {1}
    </table>""".format(pokemon,info)



content = ""

while True:
    pokemon = str(input("What is your pokemon?\tif it is finish, press enter\n"))
    if pokemon == "": break

    if getPokemonResponse(pokemon).status_code == 200:
        data = getPokemonResponse(pokemon).json()
        content += str(setTable(pokemon))
    else:
        print("There is not a pokemon")


    

createHTML(content)
html2pdf()
main()


