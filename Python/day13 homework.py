from pathlib import Path

file_name = Path("students.txt")

# Show existing names if the file already exists
if file_name.exists():
    print("Existing student names:")
    with file_name.open("r", encoding="utf-8") as file:
        print(file.read())

# Ask how many names to add
number = int(input("How many student names do you want to add? "))

# Add new names without deleting the old ones
with file_name.open("a", encoding="utf-8") as file:
    for i in range(number):
        name = input(f"Enter student name {i + 1}: ")
        file.write(name + "\n")

# Display the complete updated list
print("\nUpdated student list:")
with file_name.open("r", encoding="utf-8") as file:
    print(file.read())