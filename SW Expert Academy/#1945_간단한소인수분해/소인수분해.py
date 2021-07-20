'''
N=2**a x 3**b x 5**c x 7**d x 11**e
N이 주어질 때 a, b, c, d, e 를 출력하라.
N은 2 이상 10,000,000 이하이다.

'''


N=30
my_primes=[]
prime_factors=[2,3,5,7,11]

for prime in prime_factors:
    factor=0
    
  
    while N>=1:
        
        if N % prime ==0:
            factor+=1
            N=N/prime
            
        else:
            my_primes.append(factor)
            break

print(*my_primes)








