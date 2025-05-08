import module as m

def display_menu():
    print("\n=== Select an option ===")
    print("1. Check if Prime")
    print("2. Find Factors")
    print("3. Sum of Numbers Divisible by 5")
    print("4. Numbers Greater Than Average")
    print("5. Remove Vowels from String")
    print("6. Find First Repeated Character")
    print("7. Check Anagrams")
    print("8. Get Single Digit Sum")
    print("9. Find Word in Sentence")
    print("10. Find Target Sum Pairs")
    print("11. max_min_digit")
    print("12.find_mode")
    print("13.change_case")
    print("14.sort_characters")
    print("15.capitalize_first_last")
    print("16.sum_digits_in_string")
    print("17.replace_zeros_with_ones")
    print("18.sum_of_primes")
    print("19.sum_of_odds")
    print("20.sum_of_whole_numbers")
    print("0. Exit")

while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(m.is_prime_program())
    elif choice == 2:
        print(m.find_factors_program())
    elif choice == 3:
        print(m.sum_of_divisible_by_five_program())
    elif choice == 4:
        print(m.greater_than_average_program())
    elif choice == 5:
        print(m.remove_vowels_program())
    elif choice == 6:
        print(m.first_repeated_char_program())
    elif choice == 7:
        print(m.anagram_checker_program())
    elif choice == 8:
        print(m.single_digit_sum_program())
    elif choice == 9:
        print(m.word_search_program())
    elif choice == 10:
        print(m.target_sum_pairs_program())
    elif choice == 11:
        print(m. max_min_digit())
    elif choice == 12:
        print(m.find_mode())
    elif choice == 13:
        print(m.change_case())
    elif choice == 14:
        print(m.sort_characters())
    elif choice == 15:
        print(m.capitalize_first_last())
    elif choice == 16:
        print(m.sum_numbers_in_string())
    elif choice == 17:
        print(m.replace_zeros_with_ones())
    elif choice == 18:
        print(m.sum_of_primes())
    elif choice == 19:
        print(m.sum_of_odds())
    elif choice == 20:
        print(m.sum_of_whole_numbers())
    
    elif choice == 0:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
