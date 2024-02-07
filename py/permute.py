from itertools import permutations

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def permute(a, l, r):
    if l == r:
        print(''.join(a))
    else:
        for i in range(l, r + 1):
            swap(a, l, i)
            permute(a, l + 1, r)
            swap(a, l, i)  # backtrack


def generate_permutations(input_str):
    perm_list = list(permutations(input_str))
    for perm in perm_list:
        print(''.join(perm))




if __name__ == "__main__":
    str_val = "ABC"
    n = len(str_val)
    permute(list(str_val), 0, n - 1)
    generate_permutations("DASH")
