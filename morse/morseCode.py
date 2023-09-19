from collections import Counter
import os


class InvalidMorseCodeError(Exception):
    pass


def is_valid_morse_code(code):
    # Define valid Morse code characters
    valid_characters = set('.- ')

    # Check if all characters in the code are valid
    return not all(ch in valid_characters for ch in code)


def decode_morse_code(code):
    # Morse code dictionary
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
        '...--': '3', '....-': '4', '.....': '5', '-....': '6',
        '--...': '7', '---..': '8', '----.': '9', '/': ' ',
    }

    # Split the code into individual letters
    letters = code.split(' ')

    # Decode each letter and join them to form a sentence
    decoded_sentence = ''.join(morse_dict.get(letter, '') for letter in letters)

    return decoded_sentence


def process_file(file_name):
    try:
        # Read the contents of the file
        with open(file_name, 'r') as file:
            contents = file.read()

        # Check if the Morse code is valid
        if not is_valid_morse_code(contents):
            raise InvalidMorseCodeError("Error in Morse Code")

        # Decode the Morse code
        decoded_text = decode_morse_code(contents)
        print("Decoded sentence:", decoded_text)

        # Count the occurrences of each character
        character_counts = Counter(decoded_text)

        # Print the character counts
        print("Character Counts:")
        for character, count in character_counts.most_common():
            print(f"{character} - {count}")

    except FileNotFoundError:
        print("File not found:", file_name)
    except InvalidMorseCodeError as e:
        print(str(e))


def main():
    # Get the directory path where the script is executed
    directory = os.path.dirname(os.path.abspath(__file__))

    # Get the list of files in the directory
    files = os.listdir(directory)

    # Process each file in the directory
    for file_name in files:
        if file_name.endswith(".txt"):
            print("Processing file:", file_name)
            process_file(file_name)


if __name__ == "__main__":
    main()
