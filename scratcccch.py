def fib(n):
    arr = [0, 1]
    while len(arr) < n:
        arr.append(arr[-1] + arr[-2])

    return arr[n-1]


print(fib(7))
