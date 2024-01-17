# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grades": {"math": 90, "english": 85, "history": 88},
    "is_honors_student": True
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])
print("Math Grade:", student["grades"]["math"])

# Modifying values
student["age"] = 21
student["grades"]["english"] = 87

# Adding a new key-value pair
student["major"] = "Computer Science"

# Removing a key-value pair
del student["is_honors_student"]

# Checking membership
print("Is 'grades' in the dictionary?", "grades" in student)

# Iterating through keys and values
print("Iterating through keys:")
for key in student.keys():
    print(key)

print("\nIterating through values:")
for value in student.values():
    print(value)

print("\nIterating through key-value pairs:")
for key, value in student.items():
    print(f"{key}: {value}")