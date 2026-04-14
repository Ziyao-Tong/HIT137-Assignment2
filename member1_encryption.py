"""
HIT137 Assignment 2 - Question 1
Member 1: Encryption only

This program:
1. Reads text from raw_text.txt
2. Encrypts the text using the assignment rules
3. Writes the result to encrypted_text.txt
"""

from pathlib import Path


def shift_letter(char: str, shift: int, base: str, direction: str) -> str:

    """
    Shift a single alphabetic character with wrap-around.
    """

    alphabet_size = 26
    start = ord(base)
    position = ord(char) - start

    if direction == "forward":
        new_position = (position + shift) % alphabet_size
    elif direction == "backward":
        new_position = (position - shift) % alphabet_size
    else:
        raise ValueError("direction must be 'forward' or 'backward'")

    return chr(start + new_position)


def encrypt_char(char: str, shift1: int, shift2: int) -> str:

    """
    Encrypt a single character using the assignment rules.

    Rules:
    - a-m: shift forward by shift1 * shift2
    - n-z: shift backward by shift1 + shift2
    - A-M: shift backward by shift1
    - N-Z: shift forward by shift2 squared
    - all other characters remain unchanged
    """

    if "a" <= char <= "m":
        return shift_letter(char, shift1 * shift2, "a", "forward")

    if "n" <= char <= "z":
        return shift_letter(char, shift1 + shift2, "a", "backward")

    if "A" <= char <= "M":
        return shift_letter(char, shift1, "A", "backward")

    if "N" <= char <= "Z":
        return shift_letter(char, shift2 ** 2, "A", "forward")

    return char


def encrypt_text(text: str, shift1: int, shift2: int) -> str:

    """
    Encrypt an entire string character by character.
    """

    encrypted_chars = []

    for char in text:
        encrypted_chars.append(encrypt_char(char, shift1, shift2))

    return "".join(encrypted_chars)


def read_file(file_path: Path) -> str:

    """
    Read and return the contents of a text file.
    """

    with file_path.open("r", encoding="utf-8") as file:
        return file.read()


def write_file(file_path: Path, content: str) -> None:

    """
    Write content to a text file.
    """

    with file_path.open("w", encoding="utf-8") as file:
        file.write(content)


def encrypt_file(input_path: Path, output_path: Path, shift1: int, shift2: int) -> None:

    """
    Read from the input file, encrypt the text, and write to the output file.
    """

    original_text = read_file(input_path)
    encrypted_text = encrypt_text(original_text, shift1, shift2)
    write_file(output_path, encrypted_text)


def get_integer_input(prompt: str) -> int:

    """
    Repeatedly ask the user for an integer until a valid value is entered.
    """

    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main() -> None:

    """
    Main program for Member 1's encryption component.
    """

    current_directory = Path(__file__).resolve().parent

    input_file = current_directory / "raw_text.txt"
    output_file = current_directory / "encrypted_text.txt"

    if not input_file.exists():
        print("Error: raw_text.txt was not found in the program directory.")
        return

    print("=== Q1 Encryption Program ===")
    shift1 = get_integer_input("Enter shift1: ")
    shift2 = get_integer_input("Enter shift2: ")

    encrypt_file(input_file, output_file, shift1, shift2)

    print("Encryption complete.")
    print("Encrypted text has been written to encrypted_text.txt")


if __name__ == "__main__":
    main()