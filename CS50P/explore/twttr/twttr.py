input = input("Input: ")
# This script removes all vowels from the input string and prints the result.
input = input.lower().strip()
c = ""
for x in input:
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        continue
    else:
        c += ''.join(["", x])
print("Output:", c)