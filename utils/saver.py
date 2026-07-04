import json
import ast
from agent.q_table import QTable


def save(q_table: QTable, filename: str) -> None:

    """ conversion du dictionnaire en texte"""

    try:
        with open(filename, "w") as file:
            data = {}
            for key, value in q_table.table.items():
                new_key = str(key)
                data[new_key] = value
            file.write(json.dumps(data))
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
        print("Error: Permission denied")
        return {}
    return result
