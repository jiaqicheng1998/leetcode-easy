# Given two binary strings a and b, return their sum as a binary string.
def addBinary(a, b):
    num_a = int(a, 2)
    num_b = int(b, 2)
    return bin(num_a+num_b)[2:]

addBinary("1010", "1011")