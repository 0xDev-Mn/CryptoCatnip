from modules.hashing import compute_hash
from modules.blockchain import get_hash

def verify_image(image_path):
    """
    Compares the current hash of the image with the stored hash.
    Returns True if image is unchanged, False if tampered.
    """
    current_hash = compute_hash(image_path)
    stored_hash = get_hash(image_path.split('/')[-1])
    
    if stored_hash is None:
        return None  # Hash not stored yet
    return current_hash == stored_hash

