# Largest prime factor on a number
#Num = int(input("Enter Number: "))
Num = 600851475143
for i in range(2, Num + 1):
    if(Num % i == 0):
        isprime = 1
        for j in range(2, (i //2)):
            if(i % j == 0):
                isprime = 0
                break
        if (isprime == 1):
            k = i
print(k)
