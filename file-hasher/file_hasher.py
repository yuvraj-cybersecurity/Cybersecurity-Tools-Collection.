import hashlib

def get_file_checksum(file_path):
    hash_obj = hashlib.sha256()
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

if __name__ == "__main__":
    print("--- File Integrity Verifier ---")
    file_path = input("Enter path to file: ")
    
    try:
        checksum = get_file_checksum(file_path)
        print(f"SHA-256 Hash: {checksum}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as error:
        print(f"Process failed: {error}")
