
data = 0b1011101
modified_data = 0b10111010000000000000
divisor = 0b10001000000100001

remainder = modified_data % divisor

codeword = str(bin(data)[2:])+str(bin(remainder)[2:])

print(f"codeword:  {codeword}")
print(len(codeword))