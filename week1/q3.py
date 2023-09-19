def main():
    numbers = []

    while True:
        user_input = input("Enter a number (or a non-digit character to stop): ")

        if not user_input.isdigit():
            break

        numbers.append(int(user_input))

    if numbers:
        average = sum(numbers) / len(numbers)

        print(f"Average: {average}")
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()
