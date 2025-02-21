class Solution:
    def climbStairs(self, n: int) -> int:
        
        result = 0
        s1 = n
        s2 = 0

        while s1>= 0 and s2<= n//2:

            result += math.factorial(n-s2)//(math.factorial(s1)*math.factorial(n-s2-s1))
            s1 -= 2
            s2 += 1

        return result


         

