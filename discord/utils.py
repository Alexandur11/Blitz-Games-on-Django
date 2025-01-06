# from dotenv import load_dotenv
# import os
# load_dotenv()
# import hashlib
# import hmac
#
#
# def verify_signature(signature, timestamp, body):
#     try:
#         key = bytes.fromhex(os.getenv('DISCORD_PUBLIC_KEY'))
#         message = timestamp.encode() + body.encode()
#         sig_bytes = bytes.fromhex(signature)
#         return hmac.new(key, message, hashlib.sha256).digest() == sig_bytes
#     except Exception as e:
#         print(f"Signature verification failed: {e}")
#         return False
