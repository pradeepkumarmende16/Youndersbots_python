#10. Write a program to print a string, find the first non-repea9ng character.
def first_non_repeating_character(s):

    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in s:
        if char_count[char] == 1:
            return char

    return None  
string = input("Enter a string: ")
result = first_non_repeating_character(string)

if result:
    print("First Non-Repeating Character:", result)
else:
    print("No non-repeating character found.")
