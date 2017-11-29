def solution(A):
    number_set = set(A)
    for i in range(1,100001):
        if i not in number_set:
            return i
    return 100001