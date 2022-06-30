y=[]
b=['a','b','c','d','e','f']

for i in range(len(b)):
    print(b[i])
    x=int(input())
    try:
        x=int(input())
        if 1 <= x < 7:
            #print('invalid input')
            y.append(x)
        else:
            continue
            y.clear()
    except ValueError:
        print('give input from 1 to 7')
        continue

print(a)

