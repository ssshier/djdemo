import datetime
import jwt


def encode_token(data):
    payload = {
        "data": data,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7),
    }
    return jwt.encode(payload, "secret", algorithm="HS256")


def decode_token(encoded: str):
    payload = jwt.decode(encoded, "secret", algorithms=["HS256"])
    return payload["data"]
