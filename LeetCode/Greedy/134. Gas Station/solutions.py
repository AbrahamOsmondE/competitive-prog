class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        for i in range(len(cost)):
            gas[i] -= cost[i]
        if sum(gas) < 0:
            return -1
        
        start = 0
        curr = 0
        for i in range(len(gas)):
            curr += gas[i]
            if curr < 0:
                start = i + 1
                curr = 0
        return start
            

        