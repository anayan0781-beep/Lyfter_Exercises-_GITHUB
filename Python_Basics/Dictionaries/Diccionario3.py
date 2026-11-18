student = {
    "name": "Yanssi",
    "age": 45,
    "city": "Heredia",
    "grade": 85,
    "country": "Costa Rica"
}

deleted_item = ["age", "city"]

for key in deleted_item:
    student.pop(key)

print(student)