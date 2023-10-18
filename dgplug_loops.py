#WAP to print the first 10 numbers using while loop.

n = 0;
while(n<10):
    print(n);
    n = n+1;

#WAP to print the first n numbers where the `n` is given by the user

n = int(input())
i = 0;
while(i<n):
    print(i);
    i = i+1;

#WAP to find the sum of first n numbers where the `n` is given by the user. Also, print the average.
    
n = int(input())
x= n*(n+1)/2
    
print(x, x/n);

#WAP to print the multiplication table from 1-10

n = 10;
i = 1;
while(i<=n):
    print(str(n)+'*'+str(i)+'='+str(n*i));
    i = i+1;

#WAP to print "power of 2" for 0-20 i.e 2 to the power (0-20) and negative power i.e. 2 to the power -ve(0-20)

n = 2;
i = -20;
while(i<=20):
    print(n**i);
    i = i+1;
 
