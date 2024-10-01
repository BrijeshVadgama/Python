# 10. Write a python program to implement all function arguments type
# Positional arguments
# Default argument
# Keyword arguments (named arguments)
# Arbitrary arguments (variable-length arguments args and kwargs)


# Function with all types of arguments
def all_arguments(pos1, pos2, def_arg="default", *args, **kwargs):
    print("Positional arguments:", pos1, pos2)
    print("Default argument:", def_arg)
    print("Variable-length argument list:", args)
    print("Keyword arguments:", kwargs)


all_arguments(1, 2)
all_arguments(1, 2, "changed_default")
all_arguments(1, 2, "changed_default", 3, 4, 5)
all_arguments(1, 2, "changed_default", 3, 4, 5, key1="value1", key2="value2")
