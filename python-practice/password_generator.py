import random
import string

characters = string.ascii_letters + string.digits

password = "".join(random.choice(characters) for _ in range(10))

print(password)
