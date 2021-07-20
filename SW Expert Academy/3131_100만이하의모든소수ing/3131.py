prime = [2, 3]
print(2, 3, end = ' ')
for i in range(4, 1000000):
    for k in range(len(prime)):
        if i % prime[k] == 0 :
            break
        else:
            if prime[k] > (i//2):
                prime.append(i)
                print(i, end = ' ')
                break

