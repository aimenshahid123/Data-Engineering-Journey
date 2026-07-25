fruits =["Mango", "Banana","Kiwi"]
fruits.append("Apple")
fruits.insert(1,"Peach")
fruits.pop(1)
fruits.remove("Mango")
print(fruits)
print("Length : ", len(fruits))
for fruit in fruits:
    print(fruit.upper())

for i in range (len(fruits)):
    print(i,fruits[i])

# loop through both index and item
for i,fruit in enumerate(fruits):
    print(i,fruit)

#     enumerate()

# There's an even cleaner way to get both the index and the item: