class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A==1 or A==0:
            return A
        start=0
        end=A
        while start<=end:
            mid=start+(end-start)/2
            if mid<=A/mid:
                start = mid + 1;
                ans=mid
            else:
                end = mid - 1; 
        return ans
