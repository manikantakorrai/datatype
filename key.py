student = {
    "name": "MAnikanta",
    "age": 19,
    "grade": "A"
}
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
removed_value = student.pop("age")
print("After pop('age'):", student)
print("Removed value:", removed_value)

del student["grade"]
print("After deleting 'grade':", student)
