import json



with open('CharacterSheet.json', 'r') as file:
    exportFile = json.load(file)

def clear_values(d):
    for key in d:
        if isinstance(d[key], dict):  # If the value is a dictionary, recurse into it
            clear_values(d[key])
        else:
            d[key] = '' # Set the value to None or any default value

clear_values(exportFile)



with open('CharacterSheet.json', 'w') as file:
    json.dump(exportFile, file, indent=4)

