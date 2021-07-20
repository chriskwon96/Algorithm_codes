import sys
#
#
# def quicksort(my_list):
#     if len(my_list) <= 1:
#         return my_list
#     pivot = my_list[len(my_list)//2]
#     less, equ, big = [], [], []
#     for i in my_list:
#         if i < pivot:
#             less.append(i)
#         elif i > pivot:
#             big.append(i)
#         else:
#             equ.append(i)
#     return quicksort(less) + equ + quicksort(big)


N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()
for i in nums:
    print(i)
