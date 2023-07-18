# scribble.py

# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if char == chr(32):
        cipher += chr(32)
        continue
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + -1       # change to +1 to encode plain text or -1 to decrypt encoded text
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)


