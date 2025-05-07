# Tags: list, dictionary, input, print

# Ask the user to enter the full meaning of an organization or concept and you'll provide the acronym to the user. For example:
# Input -> As Soon As Possible.
# Output -> ASAP.
# Input -> Laughing Out Loud
# Output -> LOL.
# List of acronyms

# ASAP - As Soon As Possible
# BBL - Be Back Later
# BBS - Be Back Soon
# BTW - By The Way
# IDK - I Don't Know
# IMO - In My Opinion
# KISS - Keep It Simple, Stupid
# LOL - Laughing Out Loud
# OMG - Oh My God
# YOLO - You Only Live Once
# WTH - What The Heck

input = input("Input: ")

print(input.split())

userinput = input.split()
text = ""

for i in userinput: 
    text = text+i[0]

print(text)