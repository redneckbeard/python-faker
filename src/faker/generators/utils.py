import random
import re
import string

numerify_re = re.compile('#')
letterify_re = re.compile(r'\?')

def numerify(number_string):
    return numerify_re.sub(lambda m: str(random.randint(0, 9)), number_string)

def letterify(letter_string):
    return numerify_re.sub(lambda m: random.choice(string.ascii_letters), number_string)

def bothify(s):
    return letterify(numerify(s))

