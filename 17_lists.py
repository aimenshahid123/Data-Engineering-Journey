fruits = ["Apple","Banana","Mango"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
fruits[0]="Kiwi"
fruits[2]="Water Melon"
print(fruits)
fruits.append("Peach")
fruits.insert(1,"Apple")
print(fruits)
print(len(fruits))
print(fruits[2].count("a"))

# remove by its value 
numbers = [10, 20, 30]

numbers.remove(20)

print(numbers)
# remove by its index
numbers.pop(1)
print(numbers)   