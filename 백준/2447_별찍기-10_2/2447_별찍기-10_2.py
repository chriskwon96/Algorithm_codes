def draw_star(n):
    if n == 1:
        return ['*']
    else:
        sub_star_block = draw_star(n//3)
        star_block = []

        first_line, second_line, third_line = [] , [], []

        first_line.extend(sub_star_block * 3)
        second_line.extend(sub_star_block)
        second_line.extend([" "]*(n//3))
        second_line.extend(sub_star_block)
        third_line.extend(sub_star_block*3)

        star_block.append(first_line)
        star_block.append(second_line)
        star_block.append(third_line)

        return star_block

N  = int(input())
star_block = draw_star(N)
for i in range(N):
    print(star_block[i])