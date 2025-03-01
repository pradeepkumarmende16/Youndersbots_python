#7.Write a Python func9on to count the number of vowels in a given string.
def count_vowels(s):
    
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count


text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))
