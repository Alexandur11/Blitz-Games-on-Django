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


def compare_rating_guess(guess,the_truth):
    rating = rating_handler(guess)
    if not rating:
        raise Exception('Enter a valid rating')
    return True if rating == the_truth else False


def compare_musical_guess(guess,song_data):
    return True if guess in song_data['artist'] or guess in song_data['song'] else  False


def rating_handler(guess):
    float_break_points = {',','.'}
    if len(guess) == 3 and guess[1] not in float_break_points:
        return
    else:
        return float(guess) if guess[1] == '.' else float(guess.replace(',','.'))
