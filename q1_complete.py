from pathlib import Path
import member1_encryption


def decrypt_char(char: str, shift1: int, shift2: int) -> str:
    """
    Decrypt one character by testing all possible letters
    of the same case and finding which one matches.
    """

    if "a" <= char <= "z":
        for candidate in "abcdefghijklmnopqrstuvwxyz":
            if member1_encryption.encrypt_char(candidate, shift1, shift2) == char:
                return candidate
        return char

    if "A" <= char <= "Z":
        for candidate in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if member1_encryption.encrypt_char(candidate, shift1, shift2) == char:
                return candidate
        return char

    return char


def decrypt_text(text: str, shift1: int, shift2: int) -> str:
    """
    Decrypt a full string character by character.
    """

    decrypted_chars = []

    for char in text:
        decrypted_chars.append(decrypt_char(char, shift1, shift2))

    return "".join(decrypted_chars)


def decrypt_file(input_path: Path, output_path: Path, shift1: int, shift2: int) -> None:
    """
    Read encrypted text from file, decrypt it, and write to output file.
    """

    encrypted_text = member1_encryption.read_file(input_path)
    decrypted_text = decrypt_text(encrypted_text, shift1, shift2)
    member1_encryption.write_file(output_path, decrypted_text)


def verify_decryption(original_path: Path, decrypted_path: Path) -> bool:
    """
    Compare raw_text.txt and decrypted_text.txt.
    Return True if they are exactly the same.
    """

    original_text = member1_encryption.read_file(original_path)
    decrypted_text = member1_encryption.read_file(decrypted_path)

    return original_text == decrypted_text


def main() -> None:
    """
    Complete Q1 program:
    1. Ask for shift1 and shift2
    2. Encrypt raw_text.txt
    3. Decrypt encrypted_text.txt
    4. Verify the result
    """

    current_directory = Path(__file__).resolve().parent

    raw_file = current_directory / "raw_text.txt"
    encrypted_file = current_directory / "encrypted_text.txt"
    decrypted_file = current_directory / "decrypted_text.txt"

    if not raw_file.exists():
        print("Error: raw_text.txt was not found in the program directory.")
        return

    print("=== Q1 Complete Program ===")
    shift1 = member1_encryption.get_integer_input("Enter shift1: ")
    shift2 = member1_encryption.get_integer_input("Enter shift2: ")

    # Step 1: Encrypt
    member1_encryption.encrypt_file(raw_file, encrypted_file, shift1, shift2)
    print("Encryption complete.")
    print("Encrypted text has been written to encrypted_text.txt")

    # Step 2: Decrypt
    decrypt_file(encrypted_file, decrypted_file, shift1, shift2)
    print("Decryption complete.")
    print("Decrypted text has been written to decrypted_text.txt")

    # Step 3: Verify
    if verify_decryption(raw_file, decrypted_file):
        print("Verification successful: decrypted text matches the original.")
    else:
        print("Verification failed: decrypted text does not match the original.")


if __name__ == "__main__":
    main()
