Capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid",
    "Portugal": "Lisben",
    "Italy": "Rome"
            }
print(Capitals)
print(Capitals["Germany"])
print(Capitals.keys())
print(Capitals.values())
print(Capitals.items())
for key in Capitals.keys():
    print(key, Capitals[key])
for key,value in Capitals.items():
    print(key,value)
Capitals["Portugal"] = "Lisbon"
Capitals["Austria"] = "Vienna"
del(Capitals["Spain"])
if "Lisbon" in Capitals.values():
    print("Lisbon is present")
else:
    Capitals["Portugal"] = "Lisbon"
print(Capitals)