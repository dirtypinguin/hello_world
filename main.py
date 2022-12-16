import random
import string

def gen_str(length):
  return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(length)])


print(gen_str(12300))
