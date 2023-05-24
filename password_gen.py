import random
import string
source = string.ascii_letters + string.digits
result_str = ''.join((random.choice(source) for i in range(8)))
print(result_str)