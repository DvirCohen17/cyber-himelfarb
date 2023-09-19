def main():
    while True:
        try:
            hex_value = input("Enter a hexadecimal value, enter 'exit' to quit: ")

            if hex_value.lower() == 'exit':
                break

            decimal_value = int(hex_value, 16)
            print(decimal_value)

        except ValueError:
            print("Invalid hex number")

if __name__ == "__main__":
    main()
