from cryptography.fernet import Fernet
import rsa

selection = int(input("""1. Symmetric-Key Encryption
2. Asymmetric-Key Encryption: """))

if selection == 1:
    text = input("Input Text to Encrypt: ")

    key = Fernet.generate_key()

    fernet = Fernet(key)

    encText = fernet.encrypt(text.encode())
    print("Original Text: ", text)
    print("Encrypted Text: ", encText)
    selection = input("Want to Decrypt it? (Y/N): ")
    if selection == "Y":
        decText = fernet.decrypt(encText).decode()

        print("Decrypted Text: ", decText)
    else:
        quit()
elif selection == 2:
    publicKey, privateKey = rsa.newkeys(512)

    text = input("Input Text to Encrypt: ")

    encText = rsa.encrypt(text.encode(), publicKey)

    print("Original Text: ", text)
    print("Encrypted Text: ", encText)
    selection = input("Want to Decrypt it? (Y/N): ")
    if selection == "Y":
        decText = rsa.decrypt(encText, privateKey).decode()

        print("Decrypted Text: ", decText)
    else:
        quit()
else:
    print('Please Select 1 or 2!')

