states = {
    "q0": {"message": "Choose a drink!\nType:\nC for Coffee\nT for Tea\nA for Cappuccino\nH for Hot Choco", "next_state": "q1"},
    "q1": {"message": "You chose Coffee", "next_state": "q4"},
    "q2": {"message": "You chose Tea", "next_state": "q4"},
    "q3": {"message": "You chose Cappuccino", "next_state": "q4"},
    "q4": {"message": "You chose Hot Choco", "next_state": "q4"}
}

current_state = "q0"

while True:
    print(states[current_state]["message"])
    choice = input().upper()

    if choice in ["C", "T", "A", "H"]:
        if choice == "C":
            current_state = "q1"
        elif choice == "T":
            current_state = "q2"
        elif choice == "A":
            current_state = "q3"
        elif choice == "H":
            current_state = "q4"

        print(states[current_state]["message"])

        confirmation = input("To confirm type OK.\n").upper()
        if confirmation != "OK":
            print("Invalid input. Try again.")
            continue

        current_state = "q4"
        more_drinks = input("To select another drink type OK.\n").upper()
        if more_drinks != "OK":
            break
        else:
            current_state = "q0"
    else:
        print("Invalid input. Choose something else.")
