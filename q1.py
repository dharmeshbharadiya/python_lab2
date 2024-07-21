
def myfun(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

list1 = [12, 35, 9, 56, 24]
list2 = myfun(list1)
print(list2)