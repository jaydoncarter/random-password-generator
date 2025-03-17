import random
import string
import time

def print_title(): # Displays the title text
    print("----------------------------\n"
          "Random Password Generator\n"
          "© 2025 Jaydon Carter\n"
          "----------------------------\n")
    time.sleep(1)

def get_length(): # Prompts the user for the password length
    while True:
        try:
            length = int(input("Enter the password length (4-32): "))
            if 4 <= length <= 32:
                print(f"Password length: {length}\n")
                time.sleep(1)
                return length
            else:
                print("Please enter a length between 4 and 32.")
        except ValueError:
            print("Please enter a valid number.")

def get_input(prompt, type): # Validates and stores user input for a prompt as a boolean value
    bool_dict = {"y": True, "n": False}
    phrase_dict = {"y": "at least one", "n": "no"}
    while True:
        user_input = input(prompt).strip().lower()
        if not user_input in ["y", "n"]:
            print("Please enter 'y' (yes) or 'n' (no). ")
        else:
            break

    if type:
        print(f"The password will have {phrase_dict[user_input]} {type}.\n")
        time.sleep(1)
    return bool_dict[user_input]

def generate_password(length, capital, number, special): # generates the password using certain randomly generated ASCII characters
    # determines which characters can be part of the password
    characters = string.ascii_lowercase
    if capital:
        characters += string.ascii_uppercase
    if number:
        characters += string.digits
    if special:
        characters += string.punctuation

    password = []

    # at least one of each selected character type
    if capital:
        password.append(random.choice(string.ascii_uppercase))
    if number:
        password.append(random.choice(string.digits))
    if special:
        password.append(random.choice(string.punctuation))

    # fills in the rest of the password to the desired length
    for i in range(length - len(password)):
        password.append(random.choice(characters))

    # reorders the values in the password list, since the first 1-3 can be predictable
    random.shuffle(password)
    # returns the list as one string
    return "".join(password)

def print_ellipsis(): # displays a simple loading text
    print("Generating ", end="", flush=True)
    time.sleep(0.5)
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")

def main(): # main function to run the program
    print_title()
    while True:
        length = get_length()
        capital = get_input("Include at least one uppercase letter [y/n]: ", "uppercase letter(s)")
        number = get_input("Include at least one number [y/n]: ", "number(s)")
        special = get_input("Include at least one special character [y/n]: ", "special character(s)")

        password = generate_password(length, capital, number, special)

        print_ellipsis()
        time.sleep(0.5)
        print(f"Password: {password}\n")

        run_again = get_input("Would you like to generate another password [y/n]: ", None)
        if not run_again:
            print("Thank you, have a nice day.\n")
            break
        else:
            print("")
            time.sleep(1)

    input("Press Enter to exit")

if __name__ == "__main__":
    main() # Only runs the program if it's being run as the main module