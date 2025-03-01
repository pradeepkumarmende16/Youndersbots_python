#6. Write a Python program to find the second largest number in a list.

def second_largest(lst):
    
    unique_numbers = list(set(lst))  
    if len(unique_numbers) < 2:
        return "No second largest number"
    
    unique_numbers.sort(reverse=True)  
    return unique_numbers[1]  


numbers = list(map(int,input().split()))
print("Second largest number:", second_largest(numbers))
