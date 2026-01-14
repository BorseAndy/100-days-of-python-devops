alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    print(f"Original text is: {original_text}")
    print(f"Shift number: {shift_amount}")
    print(f"Encrypting.......")
    for letter in original_text:
        if letter.lower() in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
            print(f"{letter} encrypted in -> {alphabet[shifted_position]}")
        else:
            ## 🚧 Aici intră spațiile, "!", "," etc.
            # Pur și simplu le adăugăm așa cum sunt, fără criptare
            cipher_text += letter
    print(f"Here is the encoded result: {cipher_text}")

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
def decrypt(original_text, shift_amount):
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
    output_text = ""
    print(f"Decrypted text is: {original_text}")
    print(f"Shift number: {shift_amount}")
    print(f"Decrypting.......")
    for letter in original_text:
        if letter.lower() in alphabet:
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
            print(f"{letter} encrypted in -> {alphabet[shifted_position]}")
        else:
            ## 🚧 Aici intră spațiile, "!", "," etc.
            # Pur și simplu le adăugăm așa cum sunt, fără criptare
            output_text += letter

    print(f"Here is the original result: {output_text}")
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
def caesar(original_direction, original_text, shift_amount):
    if original_direction == 'encode':
        encrypt(original_text= original_text, shift_amount= shift_amount)
    elif original_direction == 'decode':
        decrypt(original_text= original_text, shift_amount= shift_amount)
    else:
        print(f"There must be a typo: {original_direction}\nThe direction must be 'encode' or 'decode'")

#Call Caesar function
caesar(original_direction=direction, original_text=text, shift_amount=shift)
