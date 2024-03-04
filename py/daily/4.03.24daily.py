class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        buy = 0
        sell = len(tokens) - 1
        score = 0
        max_score = 0
        while buy <= sell:
            if power >= tokens[buy]:
                score += 1
                power -= tokens[buy]
                buy += 1
            elif score > 0:
                score -= 1
                power += tokens[sell]
                sell -= 1
            else:
                break
            max_score = max(max_score, score)
        return max_score
