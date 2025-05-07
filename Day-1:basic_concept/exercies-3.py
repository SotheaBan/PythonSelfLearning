# Tags: variable, string,  input, print
# Ask the user what's on their mind. Then after the user responds, count the number of words in the sentence and print that as an output.
# Example:
# Prompt: what's on your mind today?
# Input: well, it's just a day for me to be an expert in coding
# Output: oh nice, you just told me what's on your mind in 13 words!


# print(), input(), len(), type(), int(), str(), float(), range(),
# sum(), max(), min(), abs(), round(), sorted(), list(), dict()

print ("Prompt : what's on your minde today ?")
user= input("input: ")
word_count= len(user.split())

print(f"Output: {word_count}")