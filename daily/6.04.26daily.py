# class Solution:
#     def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
#         pos=[0,0]
#         prev='n'
#         s=set((i[0],i[1]) for i in obstacles)
#         def mov(l):
#             if prev == 'n':
#                 t=[pos[0],pos[1]+l]
#                 for i in range(pos[1],t[1]+1,1):
#                     if (t[0],i) in s:
#                         return [t[0],i-1]
#             elif prev =='s':
#                 t=[pos[0],pos[1]-l]
#                 for i in range(pos[1],t[1]-1,-1):
#                     if (t[0],i) in s:
#                         return [t[0],i+1]
#             elif prev=='e':
#                 t=[pos[0]+l,pos[1]]
#                 for i in range(pos[0],t[0]+1,1):
#                     if (i,t[1]) in s:
#                         return [i-1,t[1]]
#             else:
#                 #  prev=='w':
#                 t=[pos[0]-l,pos[1]]
#                 for i in range(pos[0],t[0]-1,-1):
#                     if (i,t[1]) in s:
#                         return [i+1,t[1]]
#             return t
#         max_dist=0
#         for i in commands:
#             if i>0:
#                 pos=mov(i)
#                 max_dist = max(max_dist, pos[0] * pos[0] + pos[1] * pos[1])

#             else:
#                 if i==-2:
#                     if prev=='n':
#                         prev='w'
#                     elif prev=='w':
#                         prev='s'
#                     elif prev=='s':
#                         prev='e'
#                     else:
#                         prev='n'
#                 else:  # i == -1, turn right
#                     if prev=='n':
#                         prev='e'
#                     elif prev=='w':
#                         prev='n'
#                     elif prev=='s':
#                         prev='w'
#                     else:
#                         prev='s'
#             # print(i,prev,pos)\
#         # ans=((pos[0]**0.5) + (pos[1]**0.5))**0.5
#         return max_dist
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        pos=[0,0]
        prev='n'
        s=set((i[0],i[1]) for i in obstacles)

        def mov(l):
            if prev == 'n':
                t=[pos[0],pos[1]+l]
                for i in range(pos[1]+1,t[1]+1):
                    if (t[0],i) in s:
                        return [t[0],i-1]
            elif prev =='s':
                t=[pos[0],pos[1]-l]
                for i in range(pos[1]-1,t[1]-1,-1):
                    if (t[0],i) in s:
                        return [t[0],i+1]
            elif prev=='e':
                t=[pos[0]+l,pos[1]]
                for i in range(pos[0]+1,t[0]+1):
                    if (i,t[1]) in s:
                        return [i-1,t[1]]
            else:  # prev=='w'
                t=[pos[0]-l,pos[1]]
                for i in range(pos[0]-1,t[0]-1,-1):
                    if (i,t[1]) in s:
                        return [i+1,t[1]]
            return t

        max_dist=0
        for i in commands:
            if i>0:
                pos=mov(i)
                max_dist = max(max_dist, pos[0]*pos[0] + pos[1]*pos[1])
            else:
                if i==-2:  # turn left
                    if prev=='n':
                        prev='w'
                    elif prev=='w':
                        prev='s'
                    elif prev=='s':
                        prev='e'
                    else:
                        prev='n'
                else:  # i==-1, turn right
                    if prev=='n':
                        prev='e'
                    elif prev=='e':
                        prev='s'
                    elif prev=='s':
                        prev='w'
                    else:  # prev=='w'
                        prev='n'

        return max_dist
        

                