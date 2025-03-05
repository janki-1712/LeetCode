class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 0

        for i in range(1,n+1):
            if i == 1:
                ans = 1
            else:
                ans = ans + 4*(i-1)

        return ans
    
        