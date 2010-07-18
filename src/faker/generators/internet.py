import random
import re

from faker.generators import company
from faker.generators import name

def email(n=None):
    return '@'.join([user_name(n), domain_name()])

def free_email(n=None):
    return '@'.join([user_name(n), random.choice('gmail.com yahoo.com hotmail.com'.split())])

def user_name(n=None):
    if n is not None:
        sep = random.choice(['.', '_'])
        matches = re.findall(r'\w+', n)
        random.shuffle(matches)
        return sep.join(matches).lower()
    return random.choice([
        lambda: re.sub(r'\W+', '', name.first_name()).lower(),
        lambda: random.choice(['.', '_']).join(re.sub(r'\W+', '', n) for n in [name.first_name(), name.last_name()]).lower()
    ])()

def domain_name():
    return '.'.join([domain_word(), domain_suffix()])

def domain_word():
    return re.sub(r'\W+', '', company.name().split(' ')[0]).lower()

def domain_suffix():
    return random.choice('co.uk com us uk ca biz info name'.split())

def ip_address():
    return '%d.%d.%d.%d' % tuple(random.randint(0,255) for i in range(4))
