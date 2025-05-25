import json
import math
import numpy

PB = 0
Level = 0

stats = ['strength','dexterity','constitution', 'intelligence', 'wisdom', 'charisma']
statsSave = []
skills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
modifiers = []



with open('character5e.json', 'r') as Character:
    data = json.load(Character)
with open('CharacterSheet.json', 'r') as file:
    exportFile = json.load(file)

def clear_values(d):
    for key in d:
        if isinstance(d[key], dict):  # If the value is a dictionary, recurse into it
            clear_values(d[key])
        else:
            d[key] = '' # Set the value to None or any default value

clear_values(exportFile)


#this is for printing items in the equipment section
i = 0
for e in data['equipment']:
    exportFile['itemname' + str(i)] = str(e['name']) 
    print("equipments: " + str(e['name']))
    i+=1

# for printing armor
for e in data['armors']:
    exportFile['itemname' + str(i)] = str(e['name']) 
    print("Armors " + str(e['name']))
    i+=1

# for printing weapons
i = 0
for e in data['weapons']:
    
    exportFile['atkname' + str(i)] = str(e['name'])
    exportFile['atkdamage' + str(i)] = str(e['damageDiceAmount']) + str(e['damageDiceName'])
    print("weapons " + str(e['name']) + " Damage " + str(e['damageDiceAmount']) + str(e['damageDiceName']))
    i+=1

# printing character name
exportFile['charname'] = str(data['name'])
print('\nCharacter name: ' + str(data['name']))

# printing race
exportFile['race'] = str(data['race']['raceId'])

#printing Hp
exportFile['maxhp'] = data['hp']
print("\nHp: " + str(data['hp']))


# printing levels and classes/subclasses
for e in data['jobs']:
    print(str(e['jobId']) + " Level: " + str(e['level']))
    exportFile['classlevel'] = str(exportFile['classlevel']) + str(e['jobId']) + " Level: " + str(e['level']) + " "
    Level = Level + e['level']
print("total level: " + str(Level))



#calculating proficency bonus
PB = numpy.clip(math.floor((Level/4) +2), 2, 6)
exportFile['proficiencybonus'] = str(PB)


# for calculating the save modifiers 
for e in stats:
    if data[e]['save'] == True:
        statsSave.append(int(PB))
    else:
        statsSave.append(0)

i = 0
for e in stats:
    statsSave[i] = statsSave[i] + math.floor((data[e]['score'] - 10) /2)
    i+=1
i=0
for e in stats:
    exportFile[e.capitalize() + "-save"] = statsSave[i]
    i+=1
# for printing the modifiers
for stat in stats:
    exportFile[stat.capitalize() + "score"] = data[stat]['score']
    exportFile[stat.capitalize() + "mod"] = (math.floor((data[stat]['score'] - 10) /2))
    print(stat +": "+ str(math.floor((data[stat]['score'] - 10) /2)) + "\n")

# for printing skills and skill proficiencies
for e in data['skills']:
    print(e['typeName'] + ": " + e['proficiencyName'])
    if e['proficiencyName'] == 'NONE':
        modifiers.append(0)
    elif e['proficiencyName'] == 'FULL':
        modifiers.append(int(PB))
    else: modifiers.append(int(PB*2))
    


# for printing Feats
for e in data['feats']:
        if e['name'][0] == '-':
            exportFile['features-c'] = str(exportFile['features-c']) +str(e['name'])+ "\nDescription: " +str(e['descriptions'][0]['description'] + "\n")
        else: exportFile['features-l'] = str(exportFile['features-l']) +str(e['name'])+ "\nDescription: " +str(e['descriptions'][0]['description'] + "\n")
        print("\nFeat: " +str(e['name'])+ "\nDescription: " +str(e['descriptions'][0]['description']))




print("__________________________________________")
print("your spell slots")


spellsSlots = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth']
for e in spellsSlots:
    print(str(e) + ": " + str(data['spellSlots'][e]))

i = 1
for e in spellsSlots:
    
    exportFile['spellslots' + str(i)] = data['spellSlots'][e]
    i+=1 

i = 0
# for printing spells
for e in data['spells']:

    exportFile['spellname' + str(i)] = str(e['name'])
    exportFile['spelllevel' + str(i)] = e['level']
    print("Spell Name: " + str(e['name']) + " level " + str(e['level']) + "\nDescription " + str(e['description']))
    print("\n \n")
    i+=1 


# calculating the skills modifiers
modifiers[0] = modifiers[0] + (math.floor((data['dexterity']['score'] - 10) /2))
modifiers[1] = modifiers[1] + (math.floor((data['wisdom']['score'] - 10) /2))
modifiers[2] = modifiers[2] + (math.floor((data['intelligence']['score'] - 10) /2))
modifiers[3] = modifiers[3] + (math.floor((data['strength']['score'] - 10) /2))
modifiers[4] = modifiers[4] + (math.floor((data['charisma']['score'] - 10) /2))
modifiers[5] = modifiers[5] + (math.floor((data['intelligence']['score'] - 10) /2))
modifiers[6] = modifiers[6] + (math.floor((data['wisdom']['score'] - 10) /2))
modifiers[7] = modifiers[7] + (math.floor((data['charisma']['score'] - 10) /2))
modifiers[8] = modifiers[8] + (math.floor((data['intelligence']['score'] - 10) /2))
modifiers[9] = modifiers[9] + (math.floor((data['wisdom']['score'] - 10) /2))
modifiers[10] = modifiers[10] + (math.floor((data['intelligence']['score'] - 10) /2))
modifiers[11] = modifiers[11] + (math.floor((data['wisdom']['score'] - 10) /2))
modifiers[12] = modifiers[12] + (math.floor((data['charisma']['score'] - 10) /2))
modifiers[13] = modifiers[13] + (math.floor((data['charisma']['score'] - 10) /2))
modifiers[14] = modifiers[14] + (math.floor((data['intelligence']['score'] - 10) /2))
modifiers[15] = modifiers[15] + (math.floor((data['dexterity']['score'] - 10) /2))
modifiers[16] = modifiers[16] + (math.floor((data['dexterity']['score'] - 10) /2))
modifiers[17] = modifiers[17] + (math.floor((data['wisdom']['score'] - 10) /2))


i = 0
for e in skills:
    exportFile[e] = modifiers[i]
    i+=1


for e in data['notes']:
    exportFile['notes-l'] = str(exportFile['notes-l']) + str(e['text']) + "\n"


print(modifiers)
print(statsSave)






with open('CharacterSheet.json', 'w') as file:
    json.dump(exportFile, file, indent=4)

