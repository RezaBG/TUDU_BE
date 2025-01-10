import jwt
from datetime import datetime

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbjEiLCJleHAiOjE3MzY1MjI0MjZ9.0vzhvFaB6qlONbllRETOFCqPNjfYjS2npA9xfPjiEMQ"
decoded_token = jwt.decode(token, options={"verify_signature": False})
expiration_time = datetime.fromtimestamp(decoded_token["exp"])

print(decoded_token)
print(f"Token expires at: {expiration_time}")
