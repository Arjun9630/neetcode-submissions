class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        output = []
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in hash_map.items():
            bucket[freq].append(num)

        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                output.append(num)

                if len(output) == k:
                    return output