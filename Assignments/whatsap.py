n = int(input("Enter the number of messages: "))
chat_data = {}

for i in range(n):
    name, chat = input().split(":", 1)
    name = name.strip()
    chat = chat.strip()
    if name in chat_data:
        chat_data[name].append(chat)
    else:
        chat_data[name] = [chat]

print(chat_data)
print(chat_data.keys())

def display_menu_options():
    options_list = [
        "Exit", "Count total number of messages", "Identify unique users in the chat",
        "Count total words in the chat", "Calculate average words per message",
        "Find the longest message sent", "Find the most active user",
        "Get message count for a specific user", "Find the most frequently used word by a specific user",
        "Retrieve the first and last message sent by a user", "Check if a user is present in the chat",
        "Find commonly repeated words", "Identify the user with the longest average message length",
        "Count how many messages mention a specific user", "Remove duplicate messages",
        "Sort messages alphabetically", "Extract all questions asked in the chat",
        "Calculate the reply ratio between two users", "Check for deleted messages"
    ]
    for i in range(len(options_list)):
        print(f"{i}. {options_list[i]}")

def count_total_messages(chat_data):
    total = 0
    for user in chat_data:
        total += len(chat_data[user])
    return total

def get_unique_users(chat_data):
    unique = []
    for user in chat_data:
        if user not in unique:
            unique.append(user)
    return len(unique), unique

def count_total_words(chat_data):
    total_words = 0
    for user in chat_data:
        for msg in chat_data[user]:
            total_words += len(msg.split())
    return total_words

def calculate_avg_words_per_message(chat_data):
    total_words = 0
    total_msgs = 0
    for user in chat_data:
        for msg in chat_data[user]:
            total_msgs += 1
            total_words += len(msg.split())
    if total_msgs == 0:
        return 0
    return total_words / total_msgs

def get_longest_message(chat_data):
    longest = ""
    for user in chat_data:
        for msg in chat_data[user]:
            if len(msg) > len(longest):
                longest = msg
    return longest

def get_most_active_user(chat_data):
    max_msgs = 0
    active_user = ""
    for user in chat_data:
        if len(chat_data[user]) > max_msgs:
            max_msgs = len(chat_data[user])
            active_user = user
    return active_user

def get_msg_count_for_user(chat_data):
    user = input("Enter the user name: ")
    if user in chat_data:
        return len(chat_data[user])
    return "User not found"

def get_most_freq_word_for_user(chat_data):
    user = input("Enter the user name: ")
    if user not in chat_data:
        return "User not found"
    all_words = []
    for msg in chat_data[user]:
        all_words += msg.split()
    word_freq = {}
    for word in all_words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    max_count = 0
    most_freq = ""
    for word in word_freq:
        if word_freq[word] > max_count:
            max_count = word_freq[word]
            most_freq = word
    return most_freq

def get_first_and_last_message(chat_data):
    user = input("Enter the user name: ")
    if user in chat_data:
        return f"First: {chat_data[user][0]}\nLast: {chat_data[user][-1]}"
    return "User not found"

def is_user_present(chat_data):
    user = input("Enter the user name: ")
    if user in chat_data:
        return "User found"
    return "User not found"

def get_common_words(chat_data):
    all_words = []
    for user in chat_data:
        for msg in chat_data[user]:
            all_words += msg.split()
    word_count = {}
    for word in all_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    repeated = []
    for word in word_count:
        if word_count[word] > 1:
            repeated.append(word)
    return repeated

def user_with_longest_avg_message(chat_data):
    max_avg = 0
    target_user = ""
    for user in chat_data:
        total_len = 0
        msg_count = len(chat_data[user])
        if msg_count == 0:
            continue
        for msg in chat_data[user]:
            total_len += len(msg)
        avg_len = total_len / msg_count
        if avg_len > max_avg:
            max_avg = avg_len
            target_user = user
    return target_user

def count_user_mentions(chat_data):
    user = input("Enter the user name: ")
    count = 0
    for sender in chat_data:
        for msg in chat_data[sender]:
            if user in msg:
                count += 1
    return count

def remove_duplicate_messages(chat_data):
    for user in chat_data:
        new_msgs = []
        for msg in chat_data[user]:
            if msg not in new_msgs:
                new_msgs.append(msg)
        chat_data[user] = new_msgs
    return chat_data

def sort_all_messages(chat_data):
    all_msgs = []
    for user in chat_data:
        for msg in chat_data[user]:
            all_msgs.append(msg)
    for i in range(len(all_msgs)):
        for j in range(i + 1, len(all_msgs)):
            if all_msgs[i] > all_msgs[j]:
                temp = all_msgs[i]
                all_msgs[i] = all_msgs[j]
                all_msgs[j] = temp
    return all_msgs

def extract_all_questions(chat_data):
    questions = []
    for user in chat_data:
        for msg in chat_data[user]:
            if '?' in msg:
                questions.append(msg)
    return questions

def get_reply_ratio(chat_data):
    a, b = input("Enter two users (User1 and User2): ").split(" and ")
    a = a.strip()
    b = b.strip()
    count = 0
    if b in chat_data:
        for msg in chat_data[b]:
            if a in msg:
                count += 1
    return f"Reply ratio from {b} to {a} is {count}"

def count_deleted_messages(chat_data):
    count = 0
    for user in chat_data:
        for msg in chat_data[user]:
            if "deleted" in msg:
                count += 1
    return count

# Main Loop
while True:
    print("=" * 45)
    print("Options:")
    display_menu_options()
    print("=" * 45)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Total messages:", count_total_messages(chat_data))
    elif choice == 2:
        total, users = get_unique_users(chat_data)
        print("Unique users:", total)
        print(users)
    elif choice == 3:
        print("Total words in chat:", count_total_words(chat_data))
    elif choice == 4:
        print("Average words per message:", calculate_avg_words_per_message(chat_data))
    elif choice == 5:
        print("Longest message:", get_longest_message(chat_data))
    elif choice == 6:
        print("Most active user:", get_most_active_user(chat_data))
    elif choice == 7:
        print("Message count:", get_msg_count_for_user(chat_data))
    elif choice == 8:
        print("Most frequent word:", get_most_freq_word_for_user(chat_data))
    elif choice == 9:
        print(get_first_and_last_message(chat_data))
    elif choice == 10:
        print(is_user_present(chat_data))
    elif choice == 11:
        print("Repeated words:", get_common_words(chat_data))
    elif choice == 12:
        print("User with longest average message:", user_with_longest_avg_message(chat_data))
    elif choice == 13:
        print("Mentions count:", count_user_mentions(chat_data))
    elif choice == 14:
        remove_duplicate_messages(chat_data)
        print("Duplicates removed.")
    elif choice == 15:
        print("Sorted messages:", sort_all_messages(chat_data))
    elif choice == 16:
        print("Questions:", extract_all_questions(chat_data))
    elif choice == 17:
        print(get_reply_ratio(chat_data))
    elif choice == 18:
        print("Deleted messages count:", count_deleted_messages(chat_data))
    elif choice == 0:
        break
    else:
        print("Invalid choice.")
