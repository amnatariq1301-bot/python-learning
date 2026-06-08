import random
import string
def generate_random_chars(length=3):
    """Generates a string of random lowercase letters."""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

message = input("Enter the secrer message")

"""-------------Coding-------------"""

def encode(message):
    if len(message) < 3:
        return message[::-1]

    else:
        modified_message = message[1:] + message[0]
        random_start = generate_random_chars(3)
        random_end = generate_random_chars(3)
        return random_start + modified_message + random_end

        """-----------Decoding-----------------"""
def decode(message):
    if len(message) < 3:
        return message[::-1]
    
    else:
        trimmed_word = message[3:-3]
        original_Word = trimmed_word[-1]  + trimmed_word[:-1]
        return original_Word
    
if __name__ == "__main__":
    print("Testing encoding")
    word = message
    encoded = encode(message)
    print(f"Original word: {message}")
    print(f"Encoded message: {encoded}")

    print("Testing Decoding")
    decoded = decode(encoded)
    print(f"Decoded: {decoded}")

    print("\n--- Testing Short Word (< 3 chars) ---")
    short_word = "hi"
    encoded_short = encode(short_word)
    decoded_short = decode(encoded_short)
    print(f"Original: {short_word} -> Encoded: {encoded_short} -> Decoded: {decoded_short}")

