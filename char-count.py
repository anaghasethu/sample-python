string = input("Enter the string: ")
count =0
for i in range(0,len(string)):
    if string[i] == ' ':
        continue
    else:
        count += 1
print("Length of string exclusing white spaces: ",count)
