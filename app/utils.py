import hashlib

def mask_pii(value):
    return hashlib.sha256(value.encode()).hexdigest()
