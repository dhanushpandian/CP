class Solution:
    def timeRequiredToBuy(self, tickets, k: int) -> int:
        res = 0
        target = tickets[k]
        for person, entry in enumerate(tickets):
            if person <= k:
                res += min(entry, target)
            else:
                if target <= entry:
                    res += min(entry, target) - 1
                else:
                    res += min(entry, target)
        
        
        return res