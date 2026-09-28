from app.security import hash_password, verify_password, create_token, decode_token

def test_password_hashing():
    hashed = hash_password("strong-password")
    assert hashed != "strong-password"
    assert verify_password("strong-password", hashed)

def test_token_roundtrip():
    token = create_token(42)
    assert decode_token(token) == 42
