from PIL import Image
import numpy as np
import os

def encrypt_image(input_path, output_path, key):
    # Check if the input image file exists
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' not found. Please check the file path.")
        return
    
    # Open the image and convert it to a numpy array
    img = Image.open(input_path)
    img_array = np.array(img)
    
    # Apply XOR operation with the key on each pixel
    encrypted_array = img_array ^ key
    
    # Save the encrypted image
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as '{output_path}'")

def decrypt_image(input_path, output_path, key):
    # Decrypt using the same method (XOR operation is symmetric)
    encrypt_image(input_path, output_path, key)

# Example usage:
input_image = r'C:\Users\user\OneDrive\Studies\Prodigy InfoTech\TASK 2\Normal.jpg'
encrypted_image = r'C:\Users\user\OneDrive\Studies\Prodigy InfoTech\TASK 2\encrypted_try.png'
decrypted_image = r'C:\Users\user\OneDrive\Studies\Prodigy InfoTech\TASK 2\decrypted_try.png'

key = 50  # You can change the key for different encryption results

encrypt_image(input_image, encrypted_image, key)
decrypt_image(encrypted_image, decrypted_image, key)
