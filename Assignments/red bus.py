import random

print("===== Welcome to RedBus =====")

users = []
buses = [
    {"id": 1, "source": "Khammam", "destination": "Hyderabad", "fare": 600, "seats": 20, "rating": 4.6, "bookings": []},
    {"id": 2, "source": "Hyderabad", "destination": "Vijayawada", "fare": 1000, "seats": 15, "rating": 4.3, "bookings": []},
    {"id": 3, "source": "Hyderabad", "destination": "Pune", "fare": 1800, "seats": 10, "rating": 4.5, "bookings": []}
]

logged_in = False
current_user = None

while not logged_in:
    print("\n1. Register\n2. Login")
    choice = input("Select option: ")

    if choice == "1":
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        exists = any(user["username"] == username for user in users)
        if exists:
            print("Username already exists. Try another.")
        else:
            users.append({"username": username, "password": password, "bookings": []})
            print("Registered successfully. Please login now.")

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        for user in users:
            if user["username"] == username and user["password"] == password:
                logged_in = True
                current_user = user
                print("Login successful! Welcome", username)
                break
        if not logged_in:
            print("Invalid credentials.")

while True:
    print("\n===== REDBUS MAIN MENU =====")
    print("1. Show All Buses")
    print("2. Search Buses and Book")
    print("3. My Bookings")
    print("4. Cancel Booking")
    print("5. Logout")

    option = input("Choose an option: ")

    if option == "1":
        print("\n--- Available Buses ---")
        for bus in buses:
            print(f"Bus ID: {bus['id']} | {bus['source']} -> {bus['destination']} | Fare: ₹{bus['fare']} | Seats Left: {bus['seats']} | Rating: {bus['rating']}")

    elif option == "2":
        src = input("Enter Source City: ").strip().lower()
        dest = input("Enter Destination City: ").strip().lower()
        matches = [bus for bus in buses if bus["source"].lower() == src and bus["destination"].lower() == dest]

        if not matches:
            print("No buses found for this route.")
        else:
            print("\nMatching Buses:")
            for bus in matches:
                print(f"Bus ID: {bus['id']} | Fare: ₹{bus['fare']} | Seats Left: {bus['seats']} | Rating: {bus['rating']}")

            bus_id = int(input("Enter Bus ID to book (0 to cancel): "))
            selected_bus = next((b for b in buses if b["id"] == bus_id), None)

            if selected_bus:
                if selected_bus["seats"] > 0:
                    num_passengers = int(input("Enter number of passengers: "))
                    if num_passengers > selected_bus["seats"]:
                        print("Not enough seats available.")
                        continue

                    passengers = []
                    for i in range(num_passengers):
                        name = input(f"Enter name of passenger {i+1}: ")
                        seat_no = f"S{random.randint(1, 40)}"
                        booking = {
                            "bus_id": selected_bus["id"],
                            "source": selected_bus["source"],
                            "destination": selected_bus["destination"],
                            "fare": selected_bus["fare"],
                            "seat_no": seat_no,
                            "passenger": name
                        }
                        passengers.append(booking)

                    confirm = input(f"Total fare: ₹{selected_bus['fare'] * num_passengers}. Confirm payment? (yes/no): ").lower()
                    if confirm == "yes":
                        for booking in passengers:
                            selected_bus["bookings"].append(booking)
                            current_user["bookings"].append(booking)
                            selected_bus["seats"] -= 1
                        print("Booking confirmed!")
                        for b in passengers:
                            print(f"Passenger: {b['passenger']} | Seat: {b['seat_no']}")
                    else:
                        print("Payment cancelled. Booking not done.")
                else:
                    print("No seats available.")
            elif bus_id != 0:
                print("Invalid Bus ID.")

    elif option == "3":
        print("\n--- My Bookings ---")
        if not current_user["bookings"]:
            print("No bookings found.")
        else:
            for i, booking in enumerate(current_user["bookings"]):
                print(f"{i+1}. {booking['source']} -> {booking['destination']} | ₹{booking['fare']} | Seat: {booking['seat_no']} | Passenger: {booking['passenger']}")

    elif option == "4":
        print("\n--- Cancel Booking ---")
        if not current_user["bookings"]:
            print("No bookings to cancel.")
        else:
            for i, booking in enumerate(current_user["bookings"]):
                print(f"{i+1}. {booking['source']} -> {booking['destination']} | ₹{booking['fare']} | Seat: {booking['seat_no']} | Passenger: {booking['passenger']}")
            cancel_idx = int(input("Enter booking number to cancel (0 to cancel): "))
            if 1 <= cancel_idx <= len(current_user["bookings"]):
                cancel_booking = current_user["bookings"].pop(cancel_idx - 1)
                for bus in buses:
                    if bus["id"] == cancel_booking["bus_id"]:
                        bus["seats"] += 1
                        bus["bookings"] = [b for b in bus["bookings"] if b["seat_no"] != cancel_booking["seat_no"]]
                        break
                print("Booking cancelled successfully.")
            elif cancel_idx != 0:
                print("Invalid choice.")

    elif option == "5":
        print("Logged out successfully.")
        break

    else:
        print("Invalid option.")
