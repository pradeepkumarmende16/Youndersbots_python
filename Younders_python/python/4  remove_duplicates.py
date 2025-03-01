#4. Write a program to remove duplicates from a list while maintaining order.

def remove_duplicates(lst):
    seen = set()
    unique_list = []
    
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    
    return unique_list

 
numbers =  list(map(int,input().split()))

print("List after removing duplicates:", remove_duplicates(numbers))
