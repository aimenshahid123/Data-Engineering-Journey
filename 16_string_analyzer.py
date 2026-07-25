# You'll write a program that:

# Asks the user to enter a sentence.
# Counts how many words it contains.
# Prints the first word.
# Prints the last word.
# Converts it to uppercase.
# Converts it to lowercase.
# Checks if the input contains only letters.
# Replaces one word with another.
text = input ("Enter a sentence : ")
words = text.split(" ")
count = len(words)
print(f" Number of words in sentence:{count} ")
print(f"First Words :{words[0]}" )
print(f"last Words :{words[-1]}" )
print(f"Uppercase : {text.upper()}")
print(f"Lowercase  : {text.lower()}")
print(f"Only Letters : {text.isalpha()}")
print(f"replace python with java : {text.replace("python","java")}")
