import re

def process_hex_numbers(input_string):
    hex_numbers = re.findall(r'[A-Fa-f0-9]+', input_string)

    decimal_sum = 0
    binary_sum = 0
    octal_sum = 0

    for hex_num in hex_numbers:
        decimal_value = int(hex_num, 16)
        binary_value = bin(decimal_value)
        octal_value = oct(decimal_value)

        decimal_sum += decimal_value
        binary_sum += decimal_value
        octal_sum += decimal_value

        print(f"{hex_num} (equals {decimal_value})")
        print(f"  Binary: {binary_value[2:]}")
        print(f"  Octal: {octal_value[2:]}")

    print("Summary:")
    print(f"  Decimal: {decimal_sum}")
    print(f"  Binary: {bin(binary_sum)[2:]}")
    print(f"  Octal: {oct(octal_sum)[2:]}")


def main():
    while True:
        input_string = input("Enter a string, enter 'exit' to quit: ")

        if input_string.lower() == 'exit':
            break

        process_hex_numbers(input_string)
        print()

if __name__ == "__main__":
    main()
