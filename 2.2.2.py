def fib_digit(n):
    a, b = 0, 1
    for _ in range(end=n-1):
        a, b = b, (a + b) % 10
    return b


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()