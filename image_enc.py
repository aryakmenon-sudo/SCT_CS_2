from PIL import Image

# Swap pixels horizontally
def swap_pixels(pixels, width, height):
    for i in range(width // 2):
        for j in range(height):
            # Swap left and right pixels
            temp = pixels[i, j]
            pixels[i, j] = pixels[width - i - 1, j]
            pixels[width - i - 1, j] = temp



# Encrypt image
def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    # Step 1: Apply mathematical operation
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[i, j] = (r, g, b)

    # Step 2: Swap pixels
    swap_pixels(pixels, width, height)

    img.save(output_path)
    print("Encrypted image saved as", output_path)


# Decrypt image
def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    # Step 1: Reverse swapping
    swap_pixels(pixels, width, height)

    # Step 2: Reverse mathematical operation
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[i, j] = (r, g, b)

    img.save(output_path)
    print("Decrypted image saved as", output_path)


# User input
choice = input("Encrypt or Decrypt (e/d): ").lower()
input_path = input("Enter input image path: ")
output_path = input("Enter output image path: ")
key = int(input("Enter key value: "))

if choice == 'e':
    encrypt_image(input_path, output_path, key)
elif choice == 'd':
    decrypt_image(input_path, output_path, key)
else:
    print("Invalid choice!")
