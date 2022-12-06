mitupla = ["España", "Francia", "Reino Unido", "Alemania"]
midiccionarie = {mitupla[0]: "Madrid", mitupla[1]: "Paris", mitupla[2]: "London", mitupla[3]: "Berlin"}

print(midiccionarie)
print(midiccionarie[mitupla[1]])
print(midiccionarie["Francia"])


mynewdiccionarie = {23: "Jorda", "name": "Jordan", "team": "Chicago", "rings": {
    "sessons": [1991, 1992, 1993, 1997, 1998]}}
print(mynewdiccionarie.keys())
print(mynewdiccionarie.values())
print(len(mynewdiccionarie))
print(mynewdiccionarie)
