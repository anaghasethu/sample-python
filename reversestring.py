string = input("Enter the string: ")
print("Reversed string:",string[::-1])
result = ""
for i in range(0,len(string)):
    result =  string[i] + result
print("Reversed using loop: ", result)
