from pokebase import *
from createhtml import *
from htmltopdf import *
from sendmail import *


pokemon = pokemon(str(input("What is your pokemon?\t")))

abilities = [ability.ability.name for ability in pokemon.abilities] # pokemonun yetenekleri alınıyor

ability_descriptions = {}
for aby in abilities: # ability ismi pokebase type ad'larından biriyle çakıştığı için aby adı verildi

    description = ability(aby).effect_entries[1].effect # Yeteneğin açıklaması ingilizce alınıyor. effect_entries[1] ingilizce tanım
    ability_descriptions[aby.capitalize()] = description



table = ""
for x,y in ability_descriptions.items():
    table += "".join("<tr><td>{}</td><td>{}</td></tr>".format(x,y))


createHTML(table,pokemon)
html2pdf(pokemon)
sendMail(pokemon)
