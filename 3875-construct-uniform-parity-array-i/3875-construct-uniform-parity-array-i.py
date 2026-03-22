class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odds = sum(1 for x in nums1 if x % 2 == 1)
        evens = len(nums1) - odds
        all_even_possible = odds == 0 or odds >= 2
        all_odd_possible = evens == 0 or odds >= 1
        return all_even_possible or all_odd_possible