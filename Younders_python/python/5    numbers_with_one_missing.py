#5. Write a program to show a list of numbers from 1 to n with one missing,
#find the missing number
def find_missing_number(list1, n):
    
    expected_sum = n * (n + 1) // 2  
    actual_sum = sum(list1)  
    return expected_sum - actual_sum


n = int(input("Enter the value of n: "))
numbers = list(map(int, input(f"Enter {n-1} numbers separated by space: ").split()))
missing_number = find_missing_number(numbers, n)
print(f"The missing number is: {missing_number}")
