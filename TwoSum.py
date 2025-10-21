class Solution(object):
    def twoSum(self,nums,target): # return the indices       
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:  
                    result =[i,j]     
                    return result
                


                    
        
    
 
nums = [3,2,4]
#nums = [2,5,5,11] # Rule out same element
target = 6


result = Solution()


print(result.twoSum(nums,target))

