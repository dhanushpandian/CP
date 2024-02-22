# Intuition
# Imagine you have a car, and you have some distance to travel (the length of the array). This car has some amount of gasoline, and as long as it has gasoline, it can keep traveling on this road (the array). Every time we move up one element in the array, we subtract one unit of gasoline. However, every time we find an amount of gasoline that is greater than our current amount, we "gas up" our car by replacing our current amount of gasoline with this new amount. We keep repeating this process until we either run out of gasoline (and return false), or we reach the end with just enough gasoline (or more to spare), in which case we return true.
# Note: We can let our gas tank get to zero as long as we are able to gas up at that immediate location (element in the array) that our car is currently at.

def jump(nums: list)->bool:
    j=0
    for i in nums:
        if j<0:
            return False
        if j<i:
            j=i
        j-=1
    return True

# a=[1,1,1,1]
a=[2,3,1,1,4]
# a=[3,2,1,0,4]
print(jump(a))
