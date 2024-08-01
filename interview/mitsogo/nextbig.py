a = list(map(int, list(input())))
# ind=0
# for i in range(len(a)-2,0,-1):
#     print(i)
#     if max(a[i+1:])>a[i]:
#         ind=i
#         break

ind = -1
m = 0
for i in range(len(a)-2, 0, -1):
    if a[i] < m:
        ind = i
        break
    m = max(m, a[i])

if ind >= 0:
    swap_ind = ind+1
    for i in range(ind+1, len(a)):
        if a[ind] < a[i] and a[i] < a[swap_ind]:
            swap_ind = i
    a[ind], a[swap_ind] = a[swap_ind], a[ind]
a[ind+1:].sort()
print("".join(map(str, a)))
