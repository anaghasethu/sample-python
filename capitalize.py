string = input("Enter the string: ")
length = len(string)
result = ''
for i in range(0,length):
    if i == 0 or i == length-1:
        result = result + string[i].upper()
    else:
        result = result + string[i]
print("REsult: ", result)
