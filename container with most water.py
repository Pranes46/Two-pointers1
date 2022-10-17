class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        low = 0  #setting low pointer to index 0
        high = len(height)-1  #setting high pointer to lst index
        
        max_area = 0  #max amount of water in a container
        
        while low<high: #if the low pointer crosses the high pointer the loop will break
            max_area = max(max_area, (min(height[low],height[high])*(high-low)))  #to calculate the max_area, we are finding the breath using min function and we are multiplying with the length between high and low after that we are comparing this with the previous max area value.
            
            if height[low]<height[high]:  #if the low pointer val is smaller than the high pointer we are incrementing the low pointer to
                low+=1
            else:
                high-=1  #if not we are decrementing the high pointer
                
        return max_area  #returning max_area
            
        