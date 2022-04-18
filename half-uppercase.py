string = input("Enter the string: ")

length = len(string)
half = len(string)/2

result = ''

for i in range(0,length):
    if i >= half:
        result = result + string[i].upper()
    else:
        result = result + string[i]

print(result)

