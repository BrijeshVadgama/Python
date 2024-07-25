# 9. Input comma separated elements, convert into list and print.

values = input("Enter elements by comma seperated values: ")

l1 = [i.strip() for i in values.split(",")]

print(f"List Elements: {l1}")
