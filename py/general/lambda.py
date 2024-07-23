people = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 22},
    {"name": "Dave", "age": 25},
    {"name": "Alice", "age": 22},
    {"name": "Eve", "age": 30}
]

sorted_people = sorted(people, key=lambda person: (person["age"], person["name"]))

print(sorted_people)
