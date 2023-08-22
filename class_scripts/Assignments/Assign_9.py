# program to count vowels,consonant,digits and special characters
word=input("Enter any Given string: ")
vowel_count=0
consonant_count=0
digit_count=0
special_count=0
word.lower()
for c in word:
    if (c=='a' or c=='e' or c=='i'or c=='o' or c=='u'):
        vowel_count+=1
    elif c.isalpha():
        consonant_count+=1
    elif c.isdigit():
        digit_count+=1
    else:
        special_count+=1
print("the vowels in string:", vowel_count)
print("the consonants in string: ", consonant_count)
print("the didgits in string : ", digit_count)
print("the special characters in string :", special_count)

# Enter any Given string: helloHo@#$$167
# the vowels in string: 3
# the consonants in string:  4
# the didgits in string :  3
# the special characters in string : 4