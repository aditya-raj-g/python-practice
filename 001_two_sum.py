class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
  # Ek khali dictionary banayenge numbers ko yaad rakhne ke liye
        num_map = {} 
        
        for i, num in enumerate(nums):
            # Hum check karenge ki target banane ke liye kitna aur chahiye
            chahiye = target - num 
            
            # Agar wo number humari dictionary mein pehle se hai, toh answer mil gaya!
            if chahiye in num_map:
                return [num_map[chahiye], i]
            
            # Warna is number ko dictionary mein index ke sath save kar lenge
            num_map[num] = i      
