# AI Vintage Clothes Manager
import json
from openai import OpenAI



def main():
    closet = {}
    client = OpenAI()

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
            print("Edit Clothing Selected")
            print()
            edit_clothing(closet)

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
            search_closet(closet)

        elif choice == 6:
            print("Save Closet Selected")
            print()
            save_closet(closet)

        elif choice == 7:
            print("Load Closet Selected")
            print()
            closet = load_closet()

        elif choice == 8:
            print("Generate Resell Listing Selected")
            print()
            generate_resell(closet, client)

        elif choice == 9:
            while True:
                choice = input("Would you like to save before exiting? Y/N: ").strip().upper()

                if choice != "Y" and choice != "N":
                    print("ERROR: Invalid Input")

                elif choice == "Y":
                    save_closet(closet)
                    break

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
                print("ERROR: Enter a Number 1", high)
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
    clothing['Purchase Price'] = purchase_price

    closet[name] = clothing

    return closet


def example_add_clothing():
    clothing = {"Brand": "Stussy", "Clothing Type": "T-Shirt", "Year": "2007", "Style": "Streetwear",
                    "Color": "Black", "Size": "Meduim", "Condition": "Very Good", 
                    "Description": "Black stussy t-shirt with distressed front emblem and large back graphic", 
                    "Purchase Price": "$69"}

    for key, value in clothing.items():
        print(f"{key}: {value}")


def edit_clothing(closet):
    if not closet:
        print("Closet is Empty")
        return
    
    else: 
        while True:
            names = list(closet.keys())

            print()

            for i in range(len(names)):
                print(f"{i + 1}. {names[i]}")
            print(f"{len(names) + 1}. Exit")
            print()

            choice = validate_choice(1, (len(names) + 1))

            if choice == (len(names) + 1):
                print("Exit Selected")
                return
            
            else:
                key = names[choice - 1]
                print(f"{key} Selected")
                print()

                selected_keys = list(closet[key].keys())

                while True:
                    for i in range(len(selected_keys)):
                        print(f"{i + 1}. {selected_keys[i]}: {closet[key][selected_keys[i]]}")
                    print(f"{len(selected_keys) + 1}. Exit")
                    print()
                
                    choice1 = validate_choice(1, (len(selected_keys) + 1))

                    print(f"{selected_keys[choice1 - 1]} selected")
                    print()

                    if choice1 == (len(selected_keys) + 1):
                        print("Exit Selected")
                        break

                    else:
                        selected_key1 = selected_keys[choice1 - 1]

                        if selected_key1 == "Year" or selected_key1 =="Purchase Price":
                            while True:
                                try:
                                    new_num = int(input("Enter new value: "))
                                    closet[key][selected_key1] = new_num

                                    print(f"{selected_key1} updated successfully")
                                    break

                                except ValueError:
                                    print("ERROR: Not a number")

                        else:
                            choice2 = input("Enter change: ")

                            closet[key][selected_key1] = choice2
                            print(f"{selected_key1} updated successfully")

                        while True: 
                            choice2 = input("Would you like to edit another attribute of this clothing? Y/N: ").upper()

                            if choice2 != "Y" and choice2 !="N":
                                print("ERROR: Invalid Input")
                            else:
                                break
                        
                        if choice2 == "N":
                            break


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
            print()

            for key, value in values.items():
                print(f"{key}: {value}")
            print()
    

def search_closet(closet):
    if not closet:
        print("Closet is Empty")
        return
    
    else: 
        while True:
            searchable_list = ["Brand", "Clothing Type", "Year", "Style", "Color", "Size", "Condition"]

            for i in range(len(searchable_list)):
                print(f"{i + 1}. {searchable_list[i]}")
            print("8. Exit")

            choice = validate_choice(1, 8)

            if choice == 8:
                return
            
            elif choice == 3:
                try: 
                    year = int(input("Enter year to search for: "))

                    found_searches = []
                    
                    for name, values in closet.items():
                            if values["Year"] == year:
                                    found_searches.append(name)
                    
                    if not found_searches:
                        print("No Found Matches")

                    else: 
                        print(f"{len(found_searches)} found matches")

                        for i in range(len(found_searches)):
                            print(f"{found_searches[i]}, ", end="")
                        print()

                except ValueError:
                    print("ERROR: Invalid Input")

            else: 
                attribute = searchable_list[choice - 1]
                search = input(f"Enter {attribute} to search for: ")

                found_searches = []

                for name, values in closet.items():
                    if values[attribute].lower() == search.lower():
                            found_searches.append(name)

                if not found_searches:
                    print("No Found Matches")

                else: 
                    print(f"{len(found_searches)} found matches")

                    for i in range(len(found_searches)):
                        print(f"{found_searches[i]}, ", end="")
                    print()


def save_closet(closet):
    with open("closet.json", "w") as file:
        json.dump(closet, file)

    print("File Saved Successfully")


def load_closet():
    try: 
        with open("closet.json", "r") as file:
            closet = json.load(file)

        print("File Successfully Loaded")
        return closet

    except FileNotFoundError:
        print("No Saved File")
        return {}


def generate_resell(closet, client):
    if not closet:
            print("Closet is Empty")
            return
        
    else: 
        names = list(closet.keys())
    
        for i in range(len(names)):
            print(f"{i + 1}. {names[i]}")
        print()
        
    try: 
            choice = int(input("Select Clothing to Generate Resale Listing: "))
    
            if 1 <= choice < (len(names) + 1):
                key = names[choice - 1]
                clothing = closet[key]

                AI_resale(clothing, client)
    
            else:
                print("ERROR: Not an Option")
    
    except ValueError:
        print("ERROR: Not a Number") 


def AI_resale(clothing, client):

    desired_keys = ["Brand", "Clothing Type", "Year", "Style",
                    "Color", "Size", "Condition", "Description"]
    clothing_info = ""

    for key in desired_keys:
        value = clothing[key]
        clothing_info += f"{key}: {value}\n"

    response = client.responses.create(
    model = "gpt-5.6",
    instructions = "Write a marketplace-friendly, concise resale listing for the clothing item provided. Do not invent details that are not included.",
    input = clothing_info)

    print(response.output_text)


main()