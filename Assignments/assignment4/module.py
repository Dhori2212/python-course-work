def is_prime_program():
    return '''
    **Check Prime Number**

    num = int(input("Enter the number: "))
    def is_prime(num):
        if num < 2:
            return False
        for j in range(2, (num // 2) + 1):
            if num % j == 0:
                return False
        return True
    print(is_prime(num))

    ==========================================
    Testcase-1:
    Enter the number: 5
    Output:
    True
    ------------------------------------------
    Testcase-2:
    Enter the number: 4
    Output:
    False
    ===========================================
    '''

def find_factors_program():
    return '''
    **Find Factors**

    def find_factors(n):
        print(f'Factors of {n}:', end=' ')
        for i in range(1, n + 1):
            if n % i == 0:
                print(i, end=' ')

    n = int(input("Enter the number: "))
    find_factors(n)

    ==========================================
    Testcase-1:
    Enter the number: 5
    Output:
    Factors of 5: 1 5
    ------------------------------------------
    Testcase-2:
    Enter the number: 4
    Output:
    Factors of 4: 1 2 4
    ===========================================
    '''

def sum_of_divisible_by_five_program():
    return '''
    **Sum of Numbers Divisible by 5 in List**

    def sum_of_divisible_by_five(lst):
        total = 0
        for i in lst:
            if i % 5 == 0:
                total += i
        return total

    lst = list(map(int, input("Enter the list: ").split()))
    result = sum_of_divisible_by_five(lst)
    print(f'Sum of numbers divisible by 5: {result}')

    ==========================================
    Testcase-1:
    Enter the list: 5 10 15 3
    Output:
    Sum of numbers divisible by 5: 30
    ------------------------------------------
    Testcase-2:
    Enter the list: 1 2 3 4
    Output:
    Sum of numbers divisible by 5: 0
    ===========================================
    '''

def greater_than_average_program():
    return '''
    **Print Numbers Greater Than Average**

    def calculate_average(lst):
        return sum(lst) / len(lst)

    def print_greater_than_average(lst, avg):
        print('Numbers greater than average:', end=' ')
        for i in lst:
            if i > avg:
                print(i, end=' ')

    lst = list(map(int, input("Enter the list: ").split()))
    avg = calculate_average(lst)
    print(f'Average: {avg}')
    print_greater_than_average(lst, avg)

    ==========================================
    Testcase-1:
    Enter the list: 1 2 3 4 5
    Output:
    Average: 3.0
    Numbers greater than average: 4 5
    ------------------------------------------
    Testcase-2:
    Enter the list: 10 20
    Output:
    Average: 15.0
    Numbers greater than average: 20
    ===========================================
    '''


def remove_vowels_program():
    return '''
    **Remove Vowels from String**

    def remove_vowels(s):
        vowels = 'aeiouAEIOU'
        result = ''
        for char in s:
            if char not in vowels:
                result += char
        return result

    st = input("Enter a string: ")
    no_vowel_str = remove_vowels(st)
    print('String without vowels:', no_vowel_str)

    ==========================================
    Testcase-1:
    Enter a string: abcd
    Output:
    String without vowels: bcd
    ------------------------------------------
    Testcase-2:
    Enter a string: efgh
    Output:
    String without vowels: fgh
    ===========================================
    '''

def first_repeated_char_program():
    return '''
    **Find First Repeated Character**

    def find_first_repeated_char(st):
        seen = set()
        for char in st:
            if char in seen:
                return char
            else:
                seen.add(char)
        return None  

    st = input("Enter a string: ")
    result = find_first_repeated_char(st)
    if result:
        print("First repeated character:", result)
    else:
        print("No repeated characters found.")

    ==========================================
    Testcase-1:
    Enter a string: abcada
    Output:
    First repeated character: a
    ------------------------------------------
    Testcase-2:
    Enter a string: abcde
    Output:
    No repeated characters found.
    ===========================================
    '''

def anagram_checker_program():
    return '''
    **Check if Two Strings are Anagrams**

    def are_anagrams(s1, s2):
        if len(s1) != len(s2):
            return False
        return sorted(s1) == sorted(s2)

    st1 = input("String 1: ")
    st2 = input("String 2: ")

    if are_anagrams(st1, st2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")

    ==========================================
    Testcase-1:
    String 1: listen
    String 2: silent
    Output:
    The strings are anagrams.
    ------------------------------------------
    Testcase-2:
    String 1: apple
    String 2: banana
    Output:
    The strings are not anagrams.
    ===========================================
    '''

def single_digit_sum_program():
    return '''
    **Get Single Digit Sum**

    def get_single_digit_sum(num):
        tot_sum = num
        while tot_sum > 9:
            cur_sum = 0
            while num > 0:
                cur_sum += num % 10
                num //= 10
            tot_sum = cur_sum
            num = cur_sum
        return tot_sum

    num = int(input("Enter the number: "))
    result = get_single_digit_sum(num)
    print(f'Single digit: {result}')

    ==========================================
    Testcase-1:
    Enter the number: 1234
    Output:
    Single digit: 1
    ------------------------------------------
    Testcase-2:
    Enter the number: 5678
    Output:
    Single digit: 8
    ===========================================
    '''
def word_search_program():
    return '''
    **Find Word in Sentence**

    def find_word_in_sentence(sentence, word):
        if word in sentence:
            print(f"The word '{word}' is found in the sentence.")
        else:
            print(f"The word '{word}' is not found in the sentence.")

    sen = input("Enter sentence: ")
    word = input("Enter word to find: ")
    find_word_in_sentence(sen, word)

    ==========================================
    Testcase-1:
    Enter sentence: python is a good language
    Enter word to find: python
    Output:
    The word 'python' is found in the sentence.
    ------------------------------------------
    Testcase-2:
    Enter sentence: we are going to school
    Enter word to find: java
    Output:
    The word 'java' is not found in the sentence.
    ===========================================
    '''

def target_sum_pairs_program():
    return '''
    **Find Pairs with Target Sum**

    def find_target_sum_pairs(lst, target):
        res = []
        temp_lst = lst.copy()  
        while temp_lst:
            f = temp_lst[0]
            s = target - f
            temp_lst.remove(f)
            if s in temp_lst:
                res.append((f, s))
                temp_lst.remove(s)
        return res

    lst = list(map(int, input("Enter list elements: ").split()))
    tar = int(input("Target sum: "))
    result = find_target_sum_pairs(lst, tar)
    print(f"Pairs with sum {tar}: {result}")

    ==========================================
    Testcase-1:
    Enter list elements: 1 2 3 4 5
    Target sum: 5
    Output:
    Pairs with sum 5: [(1, 4), (2, 3)]
    ------------------------------------------
    Testcase-2:
    Enter list elements: 10 20 30
    Target sum: 100
    Output:
    Pairs with sum 100: []
    ===========================================
    '''

def max_min_digit():
  return '''
  **maximum and minimum digit in a number**

  n = int(input("Enter a number: "))
  digits = [int(d) for d in str(abs(n))]  

  max_digit = max(digits)
  min_digit = min(digits)
  print(f"Maximum digit: {max_digit}")
  print(f"Minimum digit: {min_digit}")
  ==========================================
  Testcase-1:
  Enter a number: 5391
  output:
  Maximum digit: 9
  Minimum digit: 1
  ------------------------------------------
  Testcase-2:
  Enter a number: 88002
  output:
  Maximum digit: 8
  Minimum digit: 0
  ===========================================
  '''

def find_mode():
  return '''
  **find mode in a given array**

  from collections import Counter

  arr = list(map(int, input("Enter array elements separated by space: ").split()))
  freq = Counter(arr)
  mode = max(freq, key=freq.get)
  print(f"Mode of the array: {mode}")
  ==========================================
  Testcase-1:
  Enter array elements separated by space: 1 2 2 3 4 2 5
  output:
  Mode of the array: 2
  ------------------------------------------
  Testcase-2:
  Enter array elements separated by space: 4 4 1 2 1 4 3 1 1
  output:
  Mode of the array: 1
  ===========================================
  '''

def change_case():
  return '''
  **change case of each character in a string**

  s = input("Enter a string: ")
  result = ''
  for char in s:
    if char.isupper():
      result += char.lower()
    elif char.islower():
      result += char.upper()
    else:
      result += char
  print(f"Changed case string: {result}")
  ==========================================
  Testcase-1:
  Enter a string: HelloWorld
  output:
  Changed case string: hELLOwORLD
  ------------------------------------------
  Testcase-2:
  Enter a string: PyTHon123!
  output:
  Changed case string: pYthON123!
  ===========================================
  '''

def sort_characters():
  return '''
  **sort characters from a string**

  s = input("Enter a string: ")
  sorted_s = ''.join(sorted(s))
  print(f"Sorted characters: {sorted_s}")
  ==========================================
  Testcase-1:
  Enter a string: python
  output:
  Sorted characters: hnopty
  ------------------------------------------
  Testcase-2:
  Enter a string: Hello123
  output:
  Sorted characters: 123Hello
  ===========================================
  '''

def capitalize_first_last():
  return '''
  **capitalize first and last character of each word**

  s = input("Enter a sentence: ")
  words = s.split()
  result = []
  for word in words:
    if len(word) == 1:
      result.append(word.upper())
    else:
      result.append(word[0].upper() + word[1:-1] + word[-1].upper())
  print(" ".join(result))
  ==========================================
  Testcase-1:
  Enter a sentence: hello world
  output:
  HellO WorlD
  ------------------------------------------
  Testcase-2:
  Enter a sentence: python is fun
  output:
  PythoN IS FuN
  ===========================================
  '''


def sum_digits_in_string():
  return '''
  **sum of the digits in strings**

  import re
  s = input("Enter a string with numbers: ")
  t=0
  for i in s:
    if i.isdigit():
        t+=int(i)

  print(f"Sum of numbers: {t}")
  ==========================================
  Testcase-1:
  Enter a string with numbers: abc123def45gh6
  output:
  Sum of numbers: 21
  ------------------------------------------
  Testcase-2:
  Enter a string with numbers: 10a20b30
  output:
  Sum of numbers: 6
  ===========================================
  '''

def replace_zeros_with_ones():
  return '''
  **replace all zeros with ones in a given integer**

  n = input("Enter an integer: ")
  replaced = n.replace('0', '1')
  print(f"Modified number: {replaced}")
  ==========================================
  Testcase-1:
  Enter an integer: 102030
  output:
  Modified number: 112131
  ------------------------------------------
  Testcase-2:
  Enter an integer: 50006
  output:
  Modified number: 51116
  ===========================================
  '''

def sum_of_primes():
  return '''
  **sum of all prime numbers in given range**

  def is_prime(n):
    if n < 2:
      return False
    for i in range(2, int(n**0.5)+1):
      if n % i == 0:
        return False
    return True

  start = int(input("Enter start of range: "))
  end = int(input("Enter end of range: "))
  total = sum(i for i in range(start, end+1) if is_prime(i))
  print(f"Sum of primes: {total}")
  ==========================================
  Testcase-1:
  Enter start of range: 1
  Enter end of range: 10
  output:
  Sum of primes: 17
  ------------------------------------------
  Testcase-2:
  Enter start of range: 10
  Enter end of range: 20
  output:
  Sum of primes: 60
  ===========================================
  '''

def sum_of_odds():
  return '''
  **sum of all odd numbers in given range**

  start = int(input("Enter start of range: "))
  end = int(input("Enter end of range: "))
  total = sum(i for i in range(start, end+1) if i % 2 != 0)
  print(f"Sum of odd numbers: {total}")
  ==========================================
  Testcase-1:
  Enter start of range: 1
  Enter end of range: 10
  output:
  Sum of odd numbers: 25
  ------------------------------------------
  Testcase-2:
  Enter start of range: 5
  Enter end of range: 15
  output:
  Sum of odd numbers: 66
  ===========================================
  '''


def sum_of_whole_numbers():
  return '''
  **sum of whole numbers up to a given number**

  n = int(input("Enter a non-negative integer: "))
  total = n * (n + 1) // 2
  print(f"Sum of whole numbers from 0 to {n}: {total}")
  ==========================================
  Testcase-1:
  Enter a non-negative integer: 10
  output:
  Sum of whole numbers from 0 to 10: 55
  ------------------------------------------
  Testcase-2:
  Enter a non-negative integer: 5
  output:
  Sum of whole numbers from 0 to 5: 15
  ===========================================
  '''










