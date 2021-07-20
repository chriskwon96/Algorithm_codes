T= int(input())
vowels= ['a','e','i','o','u']

for t in range(1,T+1):
    word = input()
    for vowel in vowels:
        word = word.replace(vowel, "")

    print('#{} {}'.format(t,word))


