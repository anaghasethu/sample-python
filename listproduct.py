list = []
product = 1
length = int(input("Enter the number of elements:"))
for i in range(0,length):
    ele = int(input("Element:"))
    list.append(ele)
    product = product * ele
print("The product is " ,product)
