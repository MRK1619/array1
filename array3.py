#Find Duplicate
#We Know That Set Does Not Contains Duplicate Value
#So We Compare The List Length With The Set Length
#If Any Duplicate Any Value In Set It Reduce The Length

class Solution:  
    def duplicate(self, list1):  
        new_value = set(list1) #Type Cast The List Into Set. 
          
        if len(new_value) == len(list1):  
            return 'false'  
        else:  
            return 'true'  
              
nums = [1, 2, 3, 1]  
obj = Solution()  
print(obj.duplicate(nums))  