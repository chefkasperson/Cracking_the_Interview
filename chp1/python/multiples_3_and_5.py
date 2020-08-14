def solution(number):
    total = 0
    i = 0
    while i < number:
        if i % 3 == 0 or i % 5 == 0:
            total += i
        i += 1
    return total

# def solution(number):
#     return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
