def reorder_list(lst):
    result = []
    n = len(lst)
    i = 0
    j = n - 1
    while i <= j:
        result.append(lst[i])
        if i != j:  
            result.append(lst[j])
        i += 1
        j -= 1
    return result

original_list = [1, 2, 3, 4,5,6,7,8,9]
result = reorder_list(original_list)
print(result)
