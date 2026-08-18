# AI Vintage Clothes Manager


def main():

    closet = {}

    while True:
        display_menu()

        choice = validate_choice(1, 9)

        if choice == 1:

            print("Add Clothing Selected")
            print()

            while True:

                display_add_clothing_menu()
                add_choice = validate_choice(1, 4)

                if add_choice == 1:

                    print("Add Clothing Manually Selected")
                    print()
                    closet = add_clothing(closet)
                elif add_choice == 2:

                    # add_using_AI
                    # AI_add_clothing()
                    print("Feature Coming Soon")
                    print()
                elif add_choice == 3:

                    print("View an Example Selected")
                    print()
                    example_add_clothing()
                else: 
                    break

                print()

        elif choice == 2:

            # to do 
            print("Edit Clothing Selected")
            print()
            edit_clothing()

        elif choice == 3:

            print("Remove Clothing Selected")
            print()
            remove_clothing(closet)

        elif choice == 4:

            print("View Closet Selected")
            print()
            view_closet(closet)

        elif choice == 5:

            print("Search Closet Selected")
            print()
            search_closet()
        elif choice == 6:

            print("Save Closet Selected")
            print()
            save_closet()

        elif choice == 7:

            print("Load Closet Selected")
            print()
            load_closet()
        elif choice == 8:

            print("Generate Resell Listing Selected")
            print()
            generate_resell()
        elif choice == 9:

            # exit_menu()
            while True:
                choice = input("Would you like to save before exiting? Y/N: ").strip().upper()
                if choice != "Y" and choice != "N":
                    print("ERROR: Invalid Input")
                elif choice == "Y":
                    save_closet()
                else: 
                    print("Have a Nice Day!")
                    return


def display_menu():

    print("==== Archive AI ====")
    print()
    print("1. Add Clothing")
    print("2. Edit Clothing")
    print("3. Remove Clothing")
    print("4. View Closet")
    print("5. Search Closet")
    print("6. Save Closet")
    print("7. Load Closet")
    print("8. Generate Resell Listing")
    print("9. Exit")
    print()


def validate_choice(low, high):

    while True:
        try:
            choice = int(input("Select an Option: "))

            if low <= choice <= high:
                return choice
            else: 
                print("ERROR: Enter a Number 1-9")
                continue
        except ValueError:
            print("ERROR: Not a Number")


def display_add_clothing_menu():

    print("1. Add Clothing Manually")
    print("2. Add Clothing Using AI Image")
    print("3. View an Example")
    print("4. Exit")
    print()


def add_clothing(closet):

    clothing = {"Brand": None, "Clothing Type": None, "Year": None, "Style": None,
                "Color": None, "Size": None, "Condition": None, "Description": None, "Purchase Price": None}

    name = input("Enter clothing name: ")

    brand = input("Enter clothing brand: ")
    clothing['Brand'] = brand
    clothing_type = input("Enter clothing type: ")
    clothing['Clothing Type'] = clothing_type
    year = int(input("Enter year/era: "))
    clothing['Year'] = year
    style = input("Enter Style: ")
    clothing['Style'] = style
    color = input("Enter color(s): ")
    clothing['Color'] = color
    size = input("Enter size: ")
    clothing['Size'] = size
    condition = input("Enter condition: ")
    clothing['Condition'] = condition
    description = input("Enter a description: ")
    clothing['Description'] = description
    purchase_price = int(input("Enter purchased price ($): "))
    clothing['Purchasing Price'] = purchase_price

    closet[name] = clothing

    return closet


def example_add_clothing():

    clothing = {"Brand": "Stussy", "Clothing Type": "T-Shirt", "Year": "2007", "Style": "Streetwear",
                    "Color": "Black", "Size": "Meduim", "Condition": "Very Good", 
                    "Description": "Black stussy t-shirt with distressed front emblem and large back graphic", 
                    "Purchase Price": "$69"}

    for key, value in clothing.items():
        print(f"{key}: {value}")


# def edit_clothing():


def remove_clothing(closet):

    if not closet:
        print("Closet is Empty")
        return
    else: 
        names = list(closet.keys())

        for i in range(len(names)):
            print(f"{i + 1}. {names[i]}")

    print()

    try: 
        choice = int(input("Select Clothing to Remove: "))

        if 1 <= choice < (len(names) + 1):

            key = names[choice - 1]

            closet.pop(key)
            print(f"{key} deleted")

        else:
            print("ERROR: Not an Option")

    except ValueError:
        print("ERROR: Not a Number") 


def view_closet(closet):

    if not closet:
        print("Closet is empty")
    else:

        for name, values in closet.items():
            print(f"{name}: ")
            for key, value in values.items():
                print(f"{key}: {value}")
    

# def search_closet():


# def save_closet():


# def load_closet():


def generate_resell():

    # Needs AI Implementation
    print("Generate Resell Listing Feature Coming Soon")


main()