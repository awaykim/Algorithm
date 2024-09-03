while True:
    num = input()
    if num == '0': break

    num_list = list(num)
    front = num_list[:len(num_list) // 2]
    back = list(reversed(num_list[len(num_list) // 2:]))
    if len(num) % 2 != 0: back.pop()

    if front == back: print('yes')
    else: print('no')
    