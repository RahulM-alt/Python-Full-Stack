import os

item = input("Enter the name of a new item: ")

if os.path.exists("items.txt"):
    # File exists: add the new item at the end
    with open("items.txt", "a") as file:
        file.write(item + "\n")
else:
    # File does not exist: create it and write the first item
    with open("items.txt", "w") as file:
        file.write(item + "\n")

# Read and show all items
print("\nFull list of items:")
with open("items.txt", "r") as file:
    print(file.read())