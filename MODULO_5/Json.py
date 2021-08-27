import json

data = {"cientifico": {"nombre": "Alan Mathison Turing","edad": "42"}}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
json_string = json.dumps(data, indent=2)

print(json_string)
