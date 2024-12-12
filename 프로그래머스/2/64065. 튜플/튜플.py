def solution(s):
    answer = []
    numbers = []
    string_number = []
    idx = 0
    for ch in s:
        if ch == "{":
            numbers.append([])
            idx = len(numbers) - 1
        elif ch.isdigit():
            string_number.append(ch)
        else:
            if string_number:
                num_string = ''.join(string_number)
                numbers[idx].append(int(num_string))
                string_number.clear()
            
    numbers.sort(key=lambda x: len(x))
    for num_set in numbers:
        for num in num_set:
            if num not in answer:
                answer.append(num)
    return answer