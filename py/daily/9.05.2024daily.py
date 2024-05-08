class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranked = sorted(score, reverse=True)  # Sort the scores in descending order
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i + 1) for i in range(3, len(score))]
        rank_dict = {score: medal for score, medal in zip(ranked, medals)}  # Create a dictionary to store ranks

        return [rank_dict[s] for s in score]  # Return the ranks for each score

# Sorting Scores:
# ranked = sorted(score, reverse=True)
# Here, sorted(score, reverse=True) sorts the score list in descending order, assigning it to the variable ranked. This sorted list will be used to determine the ranks.
# medals = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i + 1) for i in range(3, len(score))]
# In this line, we create a list medals that contains the first three elements as "Gold Medal", "Silver Medal", and "Bronze Medal", corresponding to the top three ranks. For the remaining ranks, we use a list comprehension [str(i + 1) for i in range(3, len(score))] to generate strings representing the ranks starting from 4 to the length of the score list.
# Creating Rank Dictionary:
# rank_dict = {score: medal for score, medal in zip(ranked, medals)}
# Here, we create a dictionary rank_dict where keys are scores from the ranked list (sorted scores), and values are corresponding medals or ranks from the medals list. We use the zip() function to pair each score with its corresponding medal/rank.
# Returning Ranks:
# return [rank_dict[s] for s in score]
# Finally, we return a list comprehension that maps each original score s to its corresponding rank/medal in the rank_dict. This list comprehension iterates over the original score list and looks up the rank/medal for each score in the rank_dict, effectively providing the desired output.