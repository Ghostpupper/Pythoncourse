tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # outputs: 4

d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)
print(d3)

l = ["car", "Ford", "flower", "Tulip"]

t = tuple(l)
print(t)

colors = (("green", "#008000"), ("blue", "#0000FF"))

colDict = dict(colors)

print(colDict)