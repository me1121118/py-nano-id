import pytest
from py_nano_id import generate_id

def test_generate_id():
    id1 = generate_id()
    id2 = generate_id()
    assert len(id1) == 21
    assert len(id2) == 21
    assert id1 != id2

def test_custom_size_and_alphabet():
    custom = generate_id(size=8, alphabet="0123456789")
    assert len(custom) == 8
    assert custom.isdigit()
