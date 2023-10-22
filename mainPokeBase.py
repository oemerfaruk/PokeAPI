from pokebase import *
from createhtml import *
from htmltopdf import *
from sendmail import *


pokemon = pokemon(str(input("What is your pokemon?\t")))

abilities = [ability.ability.name for ability in pokemon.abilities]

print("{}'nun Yetenekleri: ".format(pokemon))

ability_descriptions = {}
for aby in abilities:
    print(aby)

    print("{} Yeteneğinin Özellikleri".format(aby.capitalize()))

    print("Tanım: {}".format(ability(aby).effect_entries[1].effect))

    description = ability(aby).effect_entries[1].effect
    ability_descriptions[aby.capitalize()] = description



table = ""
for x,y in ability_descriptions.items():
    table += "".join("<tr><td>{}</td><td>{}</td></tr>".format(x,y))


createHTML(table)
html2pdf()