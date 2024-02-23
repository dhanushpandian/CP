
def merge1(nums1, m ,nums2, n) -> None:
    i, j, k = m-1, n-1, m+n-1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

#using right shift
def shift(num):
    x = num[-1]
    for i in range(len(num) - 1, 0, -1):
        num[i] = num[i - 1]
    num[0] = x

def merge2(self, nums1, m, nums2, n) -> None:
    i, j, k = 0, 0, m
    while i < m and j < n:
        if nums1[i] > nums2[j]:
            nums1[i] = nums2[j]
            shift(nums1[:k + 1])  # Shift only the merged part of nums1
            j += 1
            k += 1
        else:
            i += 1
    # If there are remaining elements in nums2, copy them to nums1
    while j < n:
        nums1[k] = nums2[j]
        j += 1
        k += 1

#sneaky approach!
class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        a=[]
        print(nums1,nums2)
        for i in range(m):
            a.append(nums1[i])
        for i in nums2:
            a.append(i)
        a.sort()
        for i,v in enumerate(a):
            print(i,v)
            nums1[i]=v     