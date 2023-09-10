"""
Generate the random password using random module
1. input max number of elements- 7 digit passeord or 8 digit password
2. ex: 5 digits, it should include aB%4*S
"""
import string
import random
alpha_dig_punc=string.ascii_letters+string.digits+string.punctuation
password=''
for x in range(0,8):
    ran=random.choice(alpha_dig_punc)
    password+=ran
print(password)
