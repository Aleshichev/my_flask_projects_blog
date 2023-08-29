import base64

encoded_string = b'UGFzc3dvcmQ6'
decoded_string = base64.b64decode(encoded_string).decode('utf-8')

print(decoded_string)