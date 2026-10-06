paragraph = """Python is a popular programming language used for web development,
data analysis, automation, and artificial intelligence. This course introduces
Python fundamentals through simple examples and practical exercises."""

paragraph = paragraph.strip()

print("Length:", len(paragraph))
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])
print("Preview:", paragraph[:50])

updated_paragraph = paragraph.replace("Python", "PYTHON")
print("\nReplaced paragraph:\n", updated_paragraph)

lowercase_paragraph = paragraph.lower()
print("\nLowercase paragraph:\n", lowercase_paragraph)

words = paragraph.split()
print("\nWords list:", words)

if "course" in lowercase_paragraph:
    print("\nThe word 'course' was found.")
else:
    print("\nThe word 'course' was not found.")

final_message = "The course description is {} characters long and has {} words.".format(
    len(paragraph), len(words)
)

print("\n" + final_message)