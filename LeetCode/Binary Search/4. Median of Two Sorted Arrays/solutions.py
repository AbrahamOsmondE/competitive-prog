class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        half = total // 2
        A = nums2
        B = nums1
        if len(nums1) > len(nums2):
            A = nums1
            B = nums2

        l, r = 0, len(B) - 1

        while True:
            mid = (r+l)//2
            midA = half - mid - 2

            A1 = A[midA] if midA >= 0 else float("-inf")
            A2 = A[midA + 1] if midA + 1 < len(A) else float("inf")
            B1 = B[mid] if mid >= 0 else float("-inf")
            B2 = B[mid + 1] if mid + 1 < len(B) else float("inf")

            if A1 <= B2 and B1 <= A2:
                if total % 2 == 0:
                    return float(max(A1,B1) + min(A2, B2)) / 2
                else:
                    return min(A2, B2)
            elif B1 > A2:
                r = mid - 1
            else:
                l = mid + 1
        

            


        