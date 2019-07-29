import json

# json data handling

data = """
[
    {
        "name" : "Sasha",
        "card" : {
            "number":4242424242424242,
            "type":"Visa"
        }
    },    
    {
        "name" : "Ella",
        "card" : {
            "number":4242424242424242,
            "type":"MasterCard"
        }
    }
]
"""
# loads stands for load from string
info = json.loads(data)
print(info[1]["name"])
print(info[1]["card"]["number"])

for user in info:
    print('name:', user['name'])
    print('card type:', user['card']['type'])