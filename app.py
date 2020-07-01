class Solution(object):
  def checkPerfectNumber(self, num):
    # Fill this in.
    self.num = num
    lst = []
    sum_lst = 0
    for i in range(1,self.num):
        if (self.num % i == 0):
            sum_lst += i
    return (sum_lst==self.num)
print(Solution().checkPerfectNumber(28))
# True
# 28 = 1 + 2 + 4 + 7 + 14
