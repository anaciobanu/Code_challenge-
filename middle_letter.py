def mid(text):
    if len(text) % 2 == 0:
        return ""
    return text[len(text)//2]

print (mid('Summer'))
print (mid('Sand'))
print (mid('Alligator'))        