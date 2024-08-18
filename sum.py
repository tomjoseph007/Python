def add_two_numbers(x, y):
    return x + y

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    result = add_two_numbers(x, y)
    print("Sum =", result)

if __name__ == "__main__":
    main()
