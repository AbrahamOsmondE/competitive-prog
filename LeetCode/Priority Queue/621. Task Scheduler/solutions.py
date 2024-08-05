class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = [0] * 26
        for char in tasks:
            freq[ord(char) - ord('A')] += 1
        
        pq = [-f for f in freq if f > 0]
        heapq.heapify(pq)

        time = 0
        while pq:
            task_count = 0
            store = []
            cycle = n + 1
            while cycle > 0 and pq:
                curr = -heapq.heappop(pq)
                if curr > 1:
                    store.append(-(curr - 1))
                task_count += 1
                cycle -= 1
            
            for x in store:
                heapq.heappush(pq, x)
            
            time += task_count if not pq else n + 1
        return time

        