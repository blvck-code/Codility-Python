arr = [3, 8, 9, 7, 6];
k = 3;

def solution(Arr, K):
    n = len(Arr)

    if n == 0:
        return []

    K = K % n
    Arr = (Arr[n - K]) + (Arr[0:n-K])
    return Arr

solution(arr, k)