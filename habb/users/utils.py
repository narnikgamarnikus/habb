import string, random

def token_generator(size=100, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))