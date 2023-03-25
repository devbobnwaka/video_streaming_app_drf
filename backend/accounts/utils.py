import random
import string


def get_unique_id():
    allowed_chars = ''.join((string.ascii_letters, string.digits))
    unique_id = ''.join(random.choice(allowed_chars) for _ in range(32))
    return unique_id

if __name__ == "__main__":
    get_unique_id()