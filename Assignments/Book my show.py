# BookMyShow 

print("=" * 60)
print(" Welcome to BookMyShow Event Listing Portal ")
print("=" * 60)

# Take Event/Movie Details as Input
print("\nPlease enter the event/movie details below:\n") 

event_id = int(input(" Enter Event ID: "))
event_name = input(" Enter Event/Movie Name: ")
ticket_price = float(input(" Enter Ticket Price (in ₹): "))

genres_input = input(" Enter Genres (comma-separated): ")
genres = list(map(str, genres_input.split(',')))  

available_seats = int(input(" Enter Available Seats: "))
booked_seats = int(input(" Enter Booked Seats: "))
seat_details = (available_seats, booked_seats)

discount = float(input(" Enter Discount Percentage: "))

features_input = input(" Enter Event Features (comma-separated): ")
event_features = set( features_input.split(','))  

organizer_name = input(" Enter Organizer Name: ")
organizer_contact = input(" Enter Organizer Contact Number: ")
event_location = input(" Enter Event Location: ")
organizer_details = {
    "name": organizer_name,
    "contact": organizer_contact,
    "location": event_location
}

# Displaying Using Different Formatting Methods
print("\n" + "=" * 60)
print("  Event Summary on BookMyShow")
print("=" * 60)

# 1. Using Comma Separation
print("\n1️Using Comma Separation (sep=','):")
print("Event ID, Name, Price:", event_id, event_name, ticket_price, sep=',')

# 2. Using Percentage Formatting
print("\n2️Using Percentage Formatting (% operator):")
print("Discount on Tickets: %.2f%%" % discount)

# 3. Using f-strings
print("\n3️Using f-strings (f\"\"):")
print(f" Event Name: {event_name}")
print(f" Ticket Price: ₹{ticket_price:.2f}")
print(f" Discount: {discount}%")
print(f" Seats Available: {seat_details[0]} seats")
print(f" Seats Booked: {seat_details[1]} seats")

# 4. Using .format() method
print("\n4️Using .format() method:")
print(" Organizer Details: Name - {0}, Contact - {1}, Location - {2}".format(
    organizer_details['name'], organizer_details['contact'], organizer_details['location']
))

# Additional Display
print("\n Genres:", ", ".join(genres))
print(" Features:", ", ".join(event_features))

print("=" * 60)
print("  Event successfully listed on BookMyShow!")
print("=" * 60)
