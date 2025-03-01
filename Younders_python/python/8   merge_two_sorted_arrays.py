#8.Write a program to show the two sorted lists, merge them into a single sorted list.
def merge_sorted_lists(lst1, lst2):

    return sorted(lst1 + lst2)


list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
print("Merged sorted list:", merge_sorted_lists(list1, list2))
