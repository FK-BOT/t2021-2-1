ip=int(input("enter the value")) #ip used for input
arr=[] #arr used to store output values
j=1 #j is used as counter to print only odd numbers
for i in range(ip):
    arr.append(j)
    j +=2
print(arr)