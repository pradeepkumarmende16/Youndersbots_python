#2. Write a Python func9on to find the most frequently occurring element in a list
#from collec9ons import Counter



from collections import Counter

def most_frequent_element(lst):
    if not lst:
        return None  
    counter = Counter(lst)
    return counter.most_common(1)[0][0]
my_list = list(map(int,input().split()))
print(most_frequent_element(my_list))

