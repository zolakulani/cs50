# # Ask user for their name
# name = input("What's your name? ")

# # Remove whitespace from str
# name = name.strip().title()

# # Say hello to user
# print(f"hello, {name}")

# # Ask user for their name
# name = input("What's your name? ").strip().title()

# # Split user's name into first name and last name
# first, last = name.split(" ")

# # Say hello to user
# print(f"hello, {first}")

text = "one two three"
first, second, third = text.split()
print(text.split())  # Output: ['one', 'two', 'three']
print(first)  # Output: ['one', 'two', 'three']