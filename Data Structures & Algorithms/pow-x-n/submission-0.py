class Solution:
    def myPow(self, x: float, n: int) -> float:
            # x to the power n
        #power is negative, return inverse 
        if n < 0:
            return 1 / self.myPow(x, -n)
        #base case, x to the power 0 is 1
        if n == 0:
            return 1.0
        #dividing the power by 2 and calling the func recursively
        half = self.myPow(x, n // 2)
        #if the power is even
        if n % 2 == 0:
            #square the half and return
            return half * half  # like x^2 * x^2 for n = 4
        #if it's odd
        #square and multiply x with the answer and return
        return half * half * x   # like x^2 * x^2 * x for n = 5