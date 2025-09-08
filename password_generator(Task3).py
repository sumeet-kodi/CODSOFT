import random
import string

print("Password Generator")

length = int(input("Enter password length: "))

letters = string.ascii_lowercase
capitals = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all_chars = letters + capitals + digits + symbols

password = ""

#one capital
password = password + random.choice(capitals)

#one symbol
password = password + random.choice(symbols)

i = 2
while i < length:
    ch = random.choice(all_chars)
    # no sequence allowed
    if len(password) > 0:
        if ord(ch) == ord(password[-1]) + 1:
            continue
    password = password + ch
    i = i + 1

print("Generated password:", password)
import random
import string

print("Password Generator")

length = int(input("Enter password length: "))

letters = string.ascii_lowercase
capitals = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all_chars = letters + capitals + digits + symbols

password = ""

# make sure at least one capital
password = password + random.choice(capitals)

# make sure at least one symbol
password = password + random.choice(symbols)

i = 2
while i < length:
    ch = random.choice(all_chars)
    # check for sequence
    if len(password) > 0:
        if ord(ch) == ord(password[-1]) + 1:
            continue
    password = password + ch
    i = i + 1

print("Generated password:", password)
