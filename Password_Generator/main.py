import random
from art import text2art

ascii_art = text2art("PASSWORD_GEN")
print(ascii_art)
print(f"Hello! How about we generate a random password for you?")

Characters = "!ABCDE!FGHIJK!@#$LMNOPQRSTUVWXYZ1234567890abcdefghijk%^&*()_+lmnopqrstuvwxy!z"

passlen = int(input("How long should your password be?: "))

newPass =[]

for i in range(passlen):
    newPass.append(random.choice(Characters))
    
yourPass = ''.join(map(str, newPass)) # Converts the list into a string then joins them w/ spacing

print(f"Your awesome password is: {yourPass}")
