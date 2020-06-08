class Solution:
    def plusOne(self, digits):
        add = 1
        
        for i in range(len(digits) - 1, -1, -1):
            digits[i], add = (digits[i] + add) % 10, (digits[i] + add)//10
            
        if add:
            digits.insert(0, add)
            
        return digits
