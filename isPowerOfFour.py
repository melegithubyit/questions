class Solution(object):
    def fib(self, n):
        if n == 0 or n==1:
            return n
        return fib(self,n - 1) + fib(self,n - 2)

trial=Solution()
print(trial.fib(3))