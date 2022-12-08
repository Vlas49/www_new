def recur_fib(n):
    if n <= 1:
        return n
    return recur_fib(n - 1) + recur_fib(n - 2)



if __name__ == '__main__':
    print(recur_fib(10))
    print(recur_fib(15))
