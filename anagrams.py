def is_anagram(text1, text2):
    return sorted(text1) == sorted(text2)

print(is_anagram("typhoon", "opython"))  
print(is_anagram("Alice", "Bob")) 
print(is_anagram("credit", "debit")) 
print(is_anagram("cipfioca", "pacific")) 

