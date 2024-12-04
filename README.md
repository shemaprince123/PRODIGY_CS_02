
# Image Encryption/Decryption Using XOR

This project demonstrates a simple encryption and decryption technique for images using the XOR operation. The image is converted to a numpy array, and the XOR operation is applied to each pixel using a specified key. Since XOR is a symmetric operation, the same method can be used for both encryption and decryption.

---

## Features

- **Encryption and Decryption**: Secure images by applying XOR encryption and easily decrypt them using the same key.
- **File Handling**: Supports multiple image formats, including JPEG and PNG.
- **Symmetric Key**: The same encryption key is used for both encryption and decryption.
- **Educational**: A simple and straightforward implementation to explore basic image manipulation and cryptographic techniques.

---

## Requirements

This project requires Python 3.x along with the following libraries:

- `Pillow` (for image processing)
- `numpy` (for array manipulation)

To install the necessary dependencies, run:

```bash
pip install pillow numpy
```

---

## How to Use

### 1. **Encrypt an Image**

- Set `input_image` to the path of the image you want to encrypt.
- Set `encrypted_image` to the desired output path for the encrypted image.
- Define the `key` (an integer) to use for encryption.

### 2. **Decrypt the Image**

- Set `input_image` to the path of the encrypted image.
- Set `decrypted_image` to the desired output path for the decrypted image.
- Use the same `key` that was used for encryption to decrypt the image.

### Example Usage

```python
input_image = r'C:\path\to\your\image.jpg'
encrypted_image = r'C:\path\to\save\encrypted_image.png'
decrypted_image = r'C:\path\to\save\decrypted_image.png'

key = 50  # Use any integer key for encryption and decryption

encrypt_image(input_image, encrypted_image, key)
decrypt_image(encrypted_image, decrypted_image, key)
```

---

### Example Output

1. **Encrypted Image**: The image will be saved as `encrypted_image.png`.
2. **Decrypted Image**: The image will be decrypted and saved as `decrypted_image.png`.

---

## How the Code Works

1. **Image Loading**: The input image is loaded using the `Pillow` library and converted into a numpy array for pixel manipulation.
2. **XOR Operation**: Each pixel value is XOR-ed with the provided key. Since XOR is symmetric, the same operation can be used for both encryption and decryption.
3. **Saving the Image**: After the XOR operation, the numpy array is converted back into an image and saved in the specified path.

---

## Notes

- The XOR encryption method used in this project is a simple cipher and should not be used for securing sensitive information in real-world applications.
- The `key` should be an integer. Feel free to experiment with different key values for varying encryption results.
- This method supports image formats like JPEG, PNG, and more.

---

## License

This project is open-source and free to use and modify for educational or personal purposes.

---

### Image Samples

**Original Image**:  
![Normal](https://github.com/user-attachments/assets/e2e7f12f-32b7-4eaa-a663-7f8124db4ce8)

**Encrypted Image**:  
![Encrypted](https://github.com/user-attachments/assets/8b51c5e4-5009-40f4-aef0-c608fc76f9d6)
![encrypted_try](https://github.com/user-attachments/assets/d935fb90-7762-4cad-a94c-114f8b9572c9)


**Decrypted Image**:  
![Decrypted](https://github.com/user-attachments/assets/c65e3336-1593-41f0-9a7d-369d2d4cfdc4)

---

Thank you for using the Image Encryption/Decryption tool!

---
