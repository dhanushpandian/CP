#write an algorithm to find the minimum number of bits required to convert integer A to integer B.
#Input: 7, 10
#Output: 3
def min_bits(a, b):
    c = a ^ b
    count = 0
    while c:
        count += c & 1
        c >>= 1
    return count    

print(10,7)
print(min_bits(7, 10)) 