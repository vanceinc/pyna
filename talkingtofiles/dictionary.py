import json

family = {"kids": 3, "wife": 1}
pets = {"dogs": ["hoover", "rex", "spot"], "cats": ["fluffy", "poppy", "rex_jr"]}
#index (pos)       0         1      2                  0        1         2
#index (neg)       -3       -2     -1                 -3       -2        -1

print(pets["dogs"])
print(pets["cats"])
print(pets["cats"][2])
print(type(pets))

jpets = json.dumps(pets)
print(type(jpets))      
print(jpets)
with open("davidspets.json", "w") as petfile:
    petfile.write(jpets)


