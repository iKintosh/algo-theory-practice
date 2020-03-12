def fib_mod(n, m):
    pisano = [0, 1]
    for _ in range(n-1):
        new_element = (pisano[-1] + pisano[-2]) % m
        pisano.append(new_element)
        if (pisano[-2], pisano[-1]) == (0, 1):
            period = len(pisano) - 2
            return pisano[n % period]
    return pisano[-1]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()