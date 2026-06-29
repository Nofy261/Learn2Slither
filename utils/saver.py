#fichier contenant les models de sessions


#load() : fera l inverse
#ouvrir le fihcier en lecture 
#le reconvertir en dictionnaire

import json #convertit le dictionnaire en texte
import ast


def save(q_table, filename) -> None:

    """ conversion du dictionnaire en texte"""

    try:
        with open(filename, "w") as file:
            data = {}
            for key, value in q_table.table.items():
                new_key = str(key)
                data[new_key] = value
            file.write(json.dumps(data)) #transforme le dictionnaire en texte
    except (PermissionError, OSError):
        print(f"Error saving {filename}")
        return


def load(filename) -> dict:

    """charger un fichier texte , convertir en dictionnaire"""

    try:
        with open(filename, "r") as file:
            text = file.read()
            data_text = json.loads(text)
            result = {}
            for key, value in data_text.items():
                new_key = ast.literal_eval(key)
                result[new_key] = value
    except FileNotFoundError:
        print(f"Error: file {filename} not found")
        return {} 
    except PermissionError:
        print(f"Error: Permission denied")
        return {}
    return result
    






