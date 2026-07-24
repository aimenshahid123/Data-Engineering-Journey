text = " Python Data Engineering" 
word = text.split()
print(word)

date = "10-10-10"
date_split = date.split("-")
print(date_split)

email = "aimen123@gmail.com"
print(email.split("@"))
# username = email.split("@")
# print(username)

folder = ["Python","Data","Engineering"]
print(" ".join(folder))

sentence = "Python is fun"

words = sentence.split()

result = "*".join(words)

print(result)
print(len(words))