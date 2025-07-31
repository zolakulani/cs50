def main():
    x = get_number("Enter a number: ")
    print(f"You entered: {x}")

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass