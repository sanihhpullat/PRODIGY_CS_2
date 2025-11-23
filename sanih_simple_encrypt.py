from PIL import Image
import numpy as np

# Super simple XOR encryption/decryption
def xor_image(input_path, output_path, key):
    # Open the image and make sure it's RGB
    img = Image.open(input_path).convert("RGB")

    # Convert to numpy array (so we can edit pixel values)
    arr = np.array(img, dtype=np.uint8)

    # XOR every pixel value with the key
    arr = arr ^ key

    # Save the output image
    Image.fromarray(arr).save(output_path)


if __name__ == "__main__":
    import sys

    # We need 3 arguments: input image, output image, key
    if len(sys.argv) != 4:
        print("Usage: python simple_encrypt.py input.png output.png key_number")
        print("Example: python simple_encrypt.py original.png enc.png 50")
        sys.exit(1)

    input_img = sys.argv[1]
    output_img = sys.argv[2]
    key = int(sys.argv[3]) % 256  # Key must be between 0–255

    xor_image(input_img, output_img, key)
    print("Done! Use the same key again to reverse it.")
