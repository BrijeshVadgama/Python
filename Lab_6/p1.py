# 1. WAP to sort python dictionary by key or value without function

d = {"a": 3, "b": 1, "c": 2}

# Sorting by key

sorted_d_by_key = dict(sorted(d.items()))
print("Sorted Dictionary by Key:", sorted_d_by_key)

# Sorting by value

sorted_d_by_value = dict(sorted(d.items(), key=lambda item: item[1]))
print("Sorted Dictionary by Value:", sorted_d_by_value)
