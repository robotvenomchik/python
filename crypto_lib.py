import hashlib


def encode_md5(value: str)-> str:
    value+="f"
    result = hashlib.md5(value.encode()).hexdigest()
    return result
try_hash=encode_md5("fkodjgosjgs")
print(try_hash)

print(encode_md5("1"))
print(encode_md5("2"))
print(encode_md5("ddd"))
print(encode_md5("12345"))
print(encode_md5("qwerty"))
print(encode_md5(""))
