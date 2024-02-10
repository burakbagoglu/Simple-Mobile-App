import hashlib

def sifrele(metin):
    # Metni SHA-256 algoritması kullanarak özetle
    sha256_hash = hashlib.sha256(metin.encode()).hexdigest()
    return sha256_hash
