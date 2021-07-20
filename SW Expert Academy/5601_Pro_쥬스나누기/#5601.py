T = int(input())

for t in range(1, T+1):
    people = input()
    drink = '1/'+people
    result = [drink]*int(people)

    print('#{} {}'.format(t, " ".join(result)))