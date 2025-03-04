class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        while n>0:
            if n%3 > 1:
                return False
            n//=3

        return True

        # power3=[]

        # while n>0:
        #     power3.append(n%3)
        #     n//3

        # print(power3)
        # return true
        