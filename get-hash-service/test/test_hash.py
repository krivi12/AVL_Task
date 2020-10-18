import hashlib


def test_hash():

    h = hashlib.new("sha256")
    h.update(str.encode("Test AVL"))
    hash_result = h.hexdigest()
    assert type(hash_result) == str
