string = input("Enter string: ")
length = len(string)
print("Length of the tring: ",length)

num = int(input("Enter index to remove: "))

result_string = ""

for i in range(0,length):
    if i != num :
        result_string = result_string + string[i]
print("After removing: ",result_string)
        
        
