class Solution:
    def rotate(self, nums, k: int) -> None:
        l=len(nums)
        a=[0]*l
        for i in range(l):
            if i+k < l:
                a[i+k]=nums[i]
            else:
                a[(i+k)%l]=nums[i]
        for i,v in enumerate(a):
            nums[i]=v


def rotate( nums, k: int):
    if len(nums) < k:
        k = k % len(nums)
        print(k)
    last_k_elements = nums[-k:]
    print("last k elements: ",last_k_elements)
    print("k to last: ",nums[k:])
    nums[k:] = nums[:-k]
    print("new k to last: ",nums[k:])
    nums[:k] = last_k_elements
    print("front to k: ",nums[:k])
    return nums


print("1:")
a=[0,1,2,3,4,5,6]
print(a)
print(rotate(a,3))

print("2:")
nums=[1,2,3,4,5]
k=3
for i in range(k):
    nums.insert(0,nums[-1])
    print(nums)
    nums.pop()
    print("pop: ",nums)
print(nums)