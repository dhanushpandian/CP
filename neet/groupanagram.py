from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)
        
        return list(anagram_groups.values())
    



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=[]
        for i in strs:
            b=[]
            b.append(i)
            for j in strs:
                if i!=j:
                    if Counter(i)==Counter(j):
                        b.append(j)
                        strs.remove(j)
            a.append(b)
        return a

