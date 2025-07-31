def main():
    item = input("Item: ").title()  # Changed variable name to singular 'item'
    print(get_calorie(item))       # Print the returned value

def get_calorie(item):            # Changed parameter name to singular 'item'
    match item:
        case "Apple":
            return "Calories: 130"
        case "Avocado" | "Cantaloupe":  # Fixed spelling to "Cantaloupe"
            return "Calories: 50"
        case "Kiwifruit" | "Sweet Cherries":  # Fixed spelling to "Cantaloupe"
            return "Calories: 100"
        case _:
            return   # Better than returning empty string
main()