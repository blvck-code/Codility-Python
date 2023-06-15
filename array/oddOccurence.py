arr = [9, 1, 9, 3, 9, 7, 9]


def solution(A):
    d = {}
    for i in A:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for k, v in d.items():
        if v % 2 == 1:
            return k


print(solution(arr))
