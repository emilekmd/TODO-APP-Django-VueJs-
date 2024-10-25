import json

# Liste d'objets simples (dictionnaires)
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]

# Conversion en JSON
json_data = json.dumps(data, indent=4)
print(json_data)