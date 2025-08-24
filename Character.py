# Take the word from the user
word = str(input("Enter any word of your choice:"))
# Take a letter from the word
char = str(input("Enter any letter in the word"))

i = 0
count = 0
while i<len(word):
    if word[i] == char:
        count=count+1
    i=i+1

print("The letter", char, "has", count, "occurences")