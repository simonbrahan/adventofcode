import sys
sys.path.append('../day10')
import knothash

def padded_binary(hex_str):
    return str(bin(int(hex_str, 16)))[2:].rjust(128, '0')


key = 'oundnydw'

on_count = 0
for i in range(128):
    hash = knothash.hash(key + '-' + str(i))
    on_count += len([bit for bit in padded_binary(hash) if bit is '1'])

print on_count
