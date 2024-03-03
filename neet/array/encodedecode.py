def encode(strs):
    return ':;'.join(strs)
def decode(strs):
    return strs.split(':;')

a=["a",":","b","c"]
b=encode(a)
print(a,"\n",b)
b=decode(b)
print(b)
