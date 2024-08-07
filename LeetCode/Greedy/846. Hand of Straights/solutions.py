class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        count = collections.defaultdict(int)
        for i in hand:
            count[i] += 1
        if len(hand) % groupSize != 0:
            return False
        
        keys = sorted(count.keys())
        print(keys, count)
        for i in range(len(keys) - groupSize + 1):
            num = keys[i]
            if count[num] == 0:
                continue
            
            if count[num] < 0:
                return False
            curr = count[num]
            for j in range(groupSize):
                if num+j not in count:
                    return False

                count[num+j] -= curr
        
        if any([count[i] != 0 for i in keys]) != 0:
            return False
        
        return True
