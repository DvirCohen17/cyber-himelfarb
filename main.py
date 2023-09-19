def factorial(num):
    if num <= 0:
        return 1
    return num * factorial(num - 1)

def main():
    try:
        m = int(input("Please enter an integer: "))
        result = factorial(m)
        print(f"The Ackermann value for ({m}) is {result}")
    except ValueError:
        print("Please enter integers only.")
if __name__ == "__main__":
    main()
