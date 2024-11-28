# Find the kth smallest element in a tuple
tuple_user = eval(input())
number_ = int(input())
list_tuple = list(tuple_user)
list_tuple.sort()
print(list_tuple[number_ - 1])