import base64
import hashlib


class Encoder:
    def __call__(self, url):
        hash_object = hashlib.sha256(url.encode())
        hash_digest = hash_object.digest()
        return base64.urlsafe_b64encode(hash_digest[:8]).decode()
