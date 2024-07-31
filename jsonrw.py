import json

#adding sample data
json_data = {
    "name": "hugh jackman",
    "age": 90, #make him do til his 90s :D
    "is_student": False,
    "Character": ["Wolverine", "Wolverine with suite", "wolverine with mask"]
}

with open('dedpol.json', 'w') as json_file:
    json.dump(json_data, json_file)

print("done")

# Reading JSON data from a file
print("\nReading")
with open('dedpol.json', 'r') as json_file:
    data = json.load(json_file)
    print(data)
