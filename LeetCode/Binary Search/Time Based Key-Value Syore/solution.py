class TimeMap(object):

    def __init__(self):
        self.dicti = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.dicti[key].append([timestamp, value])
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        arr = self.dicti[key]
        if len(arr) == 0:
            return ""
        
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        ans_time = arr[left-1][0]
        return arr[left-1][1] if timestamp > ans_time else ""