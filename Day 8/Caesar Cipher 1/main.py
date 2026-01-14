alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(text, shift):
    original_text = text
    shift_amount =shift
    print(f"Original text is: {original_text}")
    print(f"Shift number: {shift_amount}")
    print(f"Encrypting.......")
    text_encrypted = ""
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
    for letter in original_text:
        if letter.lower() in alphabet:
            old_index = alphabet.index(letter.lower())
            letter_encrypted = alphabet[(old_index + shift) %26] # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
            text_encrypted += letter_encrypted
            print(f"{letter} encrypted in -> {letter_encrypted}")
        else:
            ## 🚧 Aici intră spațiile, "!", "," etc.
            # Pur și simplu le adăugăm așa cum sunt, fără criptare
            text_encrypted += letter
    print(f"The encrypted text is: {text_encrypted}")

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

encrypt(text, shift)

