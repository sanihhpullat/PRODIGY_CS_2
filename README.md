# Image Encryptor/Decryptor (Python)

This is a simple image encryption and decryption program made as part of my Prodigy InfoTech internship. The program uses a numeric key to encrypt or decrypt images by adding/subtracting a fixed key to each pixel. It works with PNG or JPG images, and the same key can be used to reverse the encryption.

## How to Use
1. Place your image in the project folder as `input.jpg`
2. Run the script `sanih_encryptor.py` in Python
3. The program will automatically generate:
   - `encrypted.jpg` → encrypted version
   - `decrypted.jpg` → restored original image

**Notes:**
- No input prompts are required; it runs automatically.
- The encryption key is fixed in the script as `KEY = 50`.
- Works with standard image formats like `.jpg` or `.png`.

**Example:**
Input Image: `input.jpg`  
Output Images:  
- `encrypted.jpg` (scrambled/encrypted)  
- `decrypted.jpg` (original restored)
