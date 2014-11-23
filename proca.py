#!/usr/bin/python3

import sys

# Truncation to arbitrary width unsigned integer
def u(width, value):
    result = int(value) & (2 ** width - 1)
    if result != value:
        print("u" + str(width) + "(" + str(value) + ") => " + str(result))
    return result
def u8(value):
    return u(8, value)
def u16(value):
    return u(16, value)
def u32(value):
    return u(32, value)
def u64(value):
    return u(64, value)

# Truncation to arbitrary width signed integer
def i(width, value):
    result = int(value) & (2 ** (width - 1) - 1)
    if (int(value) & (1 << (width - 1))):
        result = -((result ^ (2 ** (width - 1) - 1)) + 1)
    if result != value:
        print("i" + str(width) + "(" + str(value) + ") => " + str(result))
    return result
def i8(value):
    return i(8, value)
def i16(value):
    return i(16, value)
def i32(value):
    return i(32, value)
def i64(value):
    return i(64, value)

# Calculate result
result = eval(" ".join(sys.argv[1:]))

# Print result as decimal
print(result, end=" ")
if result != int(result):
   print(int(result), end=" ")

# Truncate and print as hex/bin using suitable width
width = 8
if ((int(result) > 2**32-1) or (int(result) < -2**(32-1))):
    width = 64
elif ((int(result) > 2**16-1) or (int(result) < -2**(16-1))):
    width = 32
elif ((int(result) > 2**8-1) or (int(result) < -2**(8-1))):
    width = 16
result = int(result) & (2 ** width - 1)
print(hex(result), bin(result))
