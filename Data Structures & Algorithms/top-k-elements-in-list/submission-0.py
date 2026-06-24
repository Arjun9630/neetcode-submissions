class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        output = []
        heap = []
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
            
        for num, count in hash_map.items():
                heapq.heappush(heap, (-count, num))
        
        for _ in range(k):
            output.append(heapq.heappop(heap)[1])
            
        return output