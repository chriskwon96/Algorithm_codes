T = 10

for t in range(1, T+1):
    
    tc = int(input())
    nums = list(map(int, input().split()))
    while nums[7]>0:
        for cycle in range(1,6):
                        
            zero = nums[0]
            for i in range(7):
                nums[i]=nums[i+1]
                
            if zero - cycle <0:
                nums[-1] = 0


            else:
                nums[-1] = zero-cycle
            
            if nums[7]<=0:
     
                break
    

    print('#{} {}'.format(t, ' '.join(list(map(str, nums)))))
        