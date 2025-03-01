#9. Write a Python func9on to find the intersecton (common elements) of two lists.


def list_intersection(lst1, lst2):
    
    return list(set(lst1) & set(lst2))


list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
print("Common elements:", list_intersection(list1, list2))
