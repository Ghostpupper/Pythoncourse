dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
print(dict.keys())
print(dict.values())
print(dict.__len__())
print(dict.items())
for key in dict.keys():
    print(key, "->", dict[key])