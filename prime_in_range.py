from math import sqrt

def show_all_prime(limit):
    for n in range(limit+1):
        
        max_divisor = sqrt(n)
        max_divisor = int(max_divisor)
        flag=True
        for i in range(2,max_divisor+1):
            if n % i == 0:
               flag=False
               break
        if flag==True and n>1:
            print(n,',', end='')    


n1= int(input('Enter the number:'))
show_all_prime(n1)
