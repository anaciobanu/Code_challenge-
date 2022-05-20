def only_ints(e, f):
    if type(e) == int and type (f) == int:
        return True
    else:
        return False
print(only_ints(3, 5))
print(only_ints('k',7))
print(only_ints(1,'3'))
print(only_ints(0, 9))
print(only_ints(3,True))