from PIL import Image
import numpy as np

KEY = 50  # Simple encryption key

def encrypt_image(input_file, output_file, key=KEY):
    img = Image.open(input_file).convert('RGB')
    data = np.array(img, dtype=np.int16)  # Use int16 to avoid overflow
    encrypted_data = (data + key) % 256
    Image.fromarray(np.uint8(encrypted_data)).save(output_file)
    print(f"Encrypted image saved as {output_file}")

def decrypt_image(input_file, output_file, key=KEY):
    img = Image.open(input_file).convert('RGB')
    data = np.array(img, dtype=np.int16)
    decrypted_data = (data - key) % 256
    Image.fromarray(np.uint8(decrypted_data)).save(output_file)
    print(f"Decrypted image saved as {output_file}")

if __name__ == "__main__":
    INPUT_FILE = "input.jpg"
    ENCRYPTED_FILE = "encrypted.jpg"
    DECRYPTED_FILE = "decrypted.jpg"

    encrypt_image(INPUT_FILE, ENCRYPTED_FILE)
    decrypt_image(ENCRYPTED_FILE, DECRYPTED_FILE)
