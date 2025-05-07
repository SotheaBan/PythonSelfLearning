# Ask a user to choose from a list of 3 songs. When the user does, you print out the lyrics to the song they selected.
# Example: 
# Welcome, please select a select a song from this top 3 songs:

# 1. Baby by Bieber
# 2. Hotline Bling by Drake
# 3. Flawless by Beyonce
# 4. Fall by Eminem...

songList = {
    "1": "You know you love me (Yo), I know you care (Uh-huh) Just shout whenever (Yo), and I'll be there (Uh-huh) You are my love (Yo), you are my heart (Uh-huh)And we will never, ever, ever be apart (Yo, uh-huh)",
    "2":"You used to call me on my cell phone Late night when you need my love Call me on my cell phone Late night when you need my love And I know when that hotline bling That can only mean one thing I know when that hotline bling That can only mean one thing",
    "3": "I'm out that H, town coming coming down I'm coming down, dripping' candy on the ground H, Town, Town, I'm coming down, coming down Dripping' candy on the ground...",
    "4": "Don't fall on my face Don't fall on my faith, oh Don't fall on my fate Don't fall on my faith, oh Don't fall on my fate Don't fall on my–",

}

print("Welcome, please select a select a song from this top 3 songs: ")
print("1. Baby by Bieber")
print("2. Hotline Bling by Drake")
print("3. Flawless by Beyonce")
print("4. Fall by Eminem...")

while True: 

    choice = input("Enter song number : ")
    if choice == "1":
        print(songList["1"])
        input("Press to choose the next choice")
    elif choice == "2": 
        print(songList["1"])
        input("Press to choose the next choice")
    elif choice == "3": 
        print(songList["3"])
        input("Press to choose the next choice")
    elif choice == "2": 
        print(songList["4"])
        input("Press to choose the next choice")
    elif choice == "5": 
        break
