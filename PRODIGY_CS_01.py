def caesar_cipher(text, shift, encrypt=True):
    result = ''
    for char in text:
        if char.isalpha():
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            if char.isupper():
                result += alphabet[(alphabet.index(char.lower()) + shift) % len(alphabet)].upper()
            else:
                result += alphabet[(alphabet.index(char) + shift) % len(alphabet)]
        else:
            result += char
    if encrypt:
        return f"Encrypted message: {result}"
    else:
        return f"Decrypted message: {result}"

def main():
    while True:
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            print(caesar_cipher(message, shift, encrypt=True))
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            print(caesar_cipher(message, shift, encrypt=False))
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
