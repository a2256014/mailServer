import base64

text = "김도균"
encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
print(encoded_text)

print(base64.b64decode(encoded_text).decode('utf-8'))