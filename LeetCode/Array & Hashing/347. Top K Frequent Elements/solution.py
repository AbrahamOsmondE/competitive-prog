import collections
import math

class Solution(object):
    def topKFrequent(self, nums, k):
        count = collections.Counter(nums)
        unique = list(count.keys())
        
        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]  
            
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            unique[right], unique[store_index] = unique[store_index], unique[right]  
            
            return store_index
        
        def quickselect(left, right, k_smallest) -> None:
            if left == right: 
                return
            
            pivot_index = math.random.randint(left, right)     
                            
            pivot_index = partition(left, right, pivot_index)
            
            if k_smallest == pivot_index:
                 return 

            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)

            else:
                quickselect(pivot_index + 1, right, k_smallest)
         
        n = len(unique)  
        quickselect(0, n - 1, n - k)

        return unique[n - k:]
        