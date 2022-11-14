letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in letters:
            position = letters.index(char)
            new_position = position + shift_amount
            end_text += letters[new_position]
        else:
            end_text += char     
    print(f"The {cipher_direction}d result is {end_text}")

should_continue = True
while should_continue:
    encrypt_or_decrypt = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type ypur message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text, shift, encrypt_or_decrypt)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")