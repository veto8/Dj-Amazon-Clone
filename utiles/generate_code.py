import random

def genrate_code(lenght=8):
    nums = '0123456789'
    code = ''.join(random.choice(nums) for _ in range(lenght) )
    return code 