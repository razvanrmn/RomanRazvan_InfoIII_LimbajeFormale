class ParkingLot:
    def __init__(self, num_spaces):
        self.num_spaces = num_spaces
        self.spaces = [False] * num_spaces

    def park_car(self, space_number):
        if space_number < 1 or space_number > self.num_spaces:
            print("Invalid space number. Please choose a valid space.")
        elif self.spaces[space_number - 1]:
            print("Space is already occupied. Please choose another space.")
        else:
            self.spaces[space_number - 1] = True
            print(f"Car parked in space {space_number}.")

    def drive_away(self, space_number):
        if space_number < 1 or space_number > self.num_spaces:
            print("Invalid space number. Please choose a valid space.")
        elif not self.spaces[space_number - 1]:
            print("Space is already free. No car to drive away.")
        else:
            self.spaces[space_number - 1] = False
            print(f"Car driven away from space {space_number}.")

    def check_status(self):
        print("Parking lot status:")
        for i in range(self.num_spaces):
            status = "Occupied" if self.spaces[i] else "Free"
            print(f"Space {i + 1}: {status}")


# Test the ParkingLot class
if __name__ == "__main__":
    num_spaces = 5
    parking_lot = ParkingLot(num_spaces)

    while True:
        print("\nMenu:")
        print("1. Park car")
        print("2. Drive away car")
        print("3. Check parking lot status")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            space_number = int(input("Enter the space number to park the car: "))
            parking_lot.park_car(space_number)
        elif choice == "2":
            space_number = int(input("Enter the space number to drive away the car: "))
            parking_lot.drive_away(space_number)
        elif choice == "3":
            parking_lot.check_status()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
