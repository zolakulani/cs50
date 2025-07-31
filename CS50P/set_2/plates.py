def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length
    if not (2 <= len(s) <= 6):
        return False
    # Must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    # No periods, spaces, or punctuation marks
    if not s.isalnum():
        return False
    number_started = False
    for i, c in enumerate(s):
        if c.isdigit():
            if not number_started:
                number_started = True
                # First number cannot be '0'
                if c == '0':
                    return False
            # If a letter appears after a number, invalid
        else:
            if number_started:
                return False
    return True

main()