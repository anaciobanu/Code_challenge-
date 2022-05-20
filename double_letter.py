#def double_letters(string):
    #for i in range(len(string) - 1):
     #   letter1 = string[i]
     #   letter2 = string[i+1]
      #  if letter1 == letter2:
      #      return True
    #return False

def double_letters(text):
    return any([a == b for a, b in zip(text, text[1:])])

print(double_letters('hippopotamus'))
print(double_letters('oops'))
print(double_letters('cook'))

