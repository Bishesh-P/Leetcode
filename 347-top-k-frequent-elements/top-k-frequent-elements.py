class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Sort by frequency
        sorted_nums = sorted(freq, key=freq.get, reverse=True)

        return sorted_nums[:k]
        