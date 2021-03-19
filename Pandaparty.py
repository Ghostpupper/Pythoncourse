import pandas as pd


class Person:
    def __init__(self, name = [], city = [], age = [], py_score = []):
        if 'list' in type(name):
            self.name = name
        else:
            self.name = []
            self.name.append(name)
        if 'list' in type(city):
            self.city = city
        else:
            self.city = []
            self.city.append(city)
        if 'list' in type(age):
            self.age = age
        else:
            self.age = []
            self.age.append(age)
        if 'list' in type(py_score):
            self.py_score = py_score
        else:
            self.py_score = []
            self.py_score.append(py_score)

    def get_dict(self):
        dictionary = {
            self.name,
            self.city,
            self.age,
            self.py_score
        }
        return dictionary


data = {'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
        'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
                 'Manchester', 'Cairo', 'Osaka'],
        'age': [41, 28, 33, 34, 38, 31, 37],
        'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
 }

row_labels = [i + 101 for i in range(data['name'].__len__())]

df = pd.DataFrame(data, row_labels)

print(df.head(3))
