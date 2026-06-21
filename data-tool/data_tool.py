import base64

def encode_data(data):
    return base64.b64encode(data.encode()).decode()

def decode_data(data):
    return base64.b64decode(data.encode()).decode()

print("--- Data Obfuscation Tool ---")
text = input("Enter text to encode: ")
encoded = encode_data(text)
print(f"Encoded: {encoded}")
print(f"Decoded: {decode_data(encoded)}")
