import hashlib

def compute_hash(image_path):
    """
    Compute SHA-256 hash of the image file.
    Returns hash as a hex string.
    """
    with open(image_path, "rb") as f:
        file_bytes = f.read()
        return hashlib.sha256(file_bytes).hexdigest()

