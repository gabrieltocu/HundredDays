
from art import logo

print(logo)

# alphabet letter list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']


# Function
def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            new_position = alphabet.index(letter) + shift_amount
            new_position = new_position % len(alphabet)
            cipher_text += alphabet[new_position]
    print(f"This is the {encode_or_decode}d result: {cipher_text}\n")

again = True
while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)
    again = input("Would you like to play again? (y/n)\n").lower()
    if again == "n":
        again = False
        print("Thank you for playing!")


