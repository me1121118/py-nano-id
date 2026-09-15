import secrets

DEFAULT_ALPHABET = "_-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generate_id(size: int = 21, alphabet: str = DEFAULT_ALPHABET) -> str:
    """Generate cryptographically secure random string ID of specified size."""
    if size < 1:
        raise ValueError("size must be >= 1")
    return "".join(secrets.choice(alphabet) for _ in range(size))
