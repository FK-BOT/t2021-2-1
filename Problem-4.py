numbers=[1,2,3,4,5,6,7,8,9]#numbers stores numbers 1-9
multiples=[1,2,8,9,12,46,76,82,15,20,30]#multiples input used in this program 
count=[0]*(len(numbers))#count is used as to keep a count of number of multiples divisible by numbers
for i in range(len(numbers)):
    for j in range(len(multiples)):
        if multiples[j]%numbers[i]==0:
            count[i] +=1
result = {numbers[i]: count[i] for i in range(len(numbers))}#result is used to convert count from hash to dictionary
print(result)