class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        
        first = m-1  #the pointer will be in num1 array
        second = n-1 #the pointer will be in num2 array
        third = m+n-1
        
        while(first>=0 and second >=0):  #if the first or second reches negative value the loop will break
            if nums1[first] < nums2[second]:  #we are comparing the num1 with num2 if the condition satisfies we are changing the nums1 value 
                nums1[third] = nums2[second]
                second-=1  #decrementing the nums 2 pointer after changing the num in nums 1
                
            else:  #if the nums1 is not greater than the nums2 array we are changing the nums1 arrayvalue with nums1 of first pointer
                nums1[third] = nums1[first]
                first-=1  # #decrementing the nums 1 pointer after changing the num in nums 1
            third-=1  #we are decrementing the third pointer
            
        if(second>=0):  #if the second didnt go out of bounds we are copying the numsbers from nums 2 to nums 1 where the loop broke
            nums1[:second+1] = nums2[:second+1]