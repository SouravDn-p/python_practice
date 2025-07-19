# values = []

# for i in range(4):
#     number = int(input("Enter the value : "))
#     values.append(number)


# greatestNumber = max(values)
# print(f"greatestNumber {greatestNumber}")

#by using tuple : 

setValues = set()
for i in range (4): 
    number = int(input("Enter value: ")) 
    setValues.add(number)

print(f"max number : {max(setValues)}")