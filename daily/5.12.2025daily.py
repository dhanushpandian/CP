# class Solution:
#     def countCollisions(self, d: str) -> int:
#         ans=0
#         i=0
#         d=[i for i in d]
#         l=len(d)
#         while i < l:
#             if d[i] == 'R' and i+1 < l:
#                 if  d[i+1] == 'L':
#                     ans+=2
#                     print(i,ans)
#                     d[i] = 'S'
#                     d[i+1] = 'S'
#                     i+=2
#                     continue

#                 if d[i+1] == 'S' :
#                     ans+=1
#                     print(i,ans)
#                     d[i]='S'
#                     i+=1
#                     continue
                    
#             if d[i] == 'L' and i-1 > -1:
#                 if d[i-1] == 'S':
#                     ans+=1
#                     print(i,ans)
#                     d[i]='S'
#                     i+=1
#                     continue                
#             print(i,ans)
#             i+=1
#         return ans
# class Solution:
#     def countCollisions(self, directions: str) -> int:
#         stack = []
#         collisions = 0

#         for car in directions:
#             if car == 'R':
#                 stack.append('R')

#             elif car == 'S':
#                 # Any R before S will collide
#                 while stack and stack[-1] == 'R':
#                     stack.pop()
#                     collisions += 1
#                 stack.append('S')

#             elif car == 'L':
#                 if not stack:
#                     stack.append('L')
#                 else:
#                     if stack[-1] == 'R':
#                         # R and L collide → both become S
#                         stack.pop()
#                         collisions += 2
#                         # Any more R before also collide
#                         while stack and stack[-1] == 'R':
#                             stack.pop()
#                             collisions += 1
#                         stack.append('S')
#                     elif stack[-1] == 'S':
#                         # L collides with S
#                         collisions += 1
#                         stack.append('S')
#                     else:
#                         stack.append('L')

#         return collisions
class Solution:
    def countCollisions(self, directions: str) -> int:
        # Remove cars that will never collide
        directions = directions.lstrip('L').rstrip('R')
        # Every remaining moving car collides
        return sum(c != 'S' for c in directions)