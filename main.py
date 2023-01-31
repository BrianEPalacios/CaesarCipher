alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
print(alphabet)





text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

new_text = list(text)
results = list(map(lambda x: x if x == ' ' or x.isnumeric() else alphabet[((alphabet.index(x)+shift)%26)], new_text))
encrypted_text = ''.join(results)
print(encrypted_text)

text = input("Please input your encrypted message:\n").lower()
shift = int(input("Type the shift number:\n"))
new_text = list(encrypted_text)
results = list(map(lambda x: x if x == ' ' or x.isnumeric() else alphabet[((alphabet.index(x)-shift%26))], new_text))
decrypted_text = ''.join(results)
print(decrypted_text)