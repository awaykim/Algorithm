s = input()
for c in s:
    if c.isalpha():
        i = ord(c)
        rot_code = i + 13
        if 64 < i < 91:
            if rot_code > 90:
                rot_code = rot_code - 26
        else:
            if not chr(rot_code).isalpha():
                rot_code = rot_code -26
        print(chr(rot_code), end='')
    else:
        print(c, end='')