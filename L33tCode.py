def rotate(nums : list, k : int)->None:
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        print(f'k={k}\n')
        nums[k:], nums[:k] = nums[:-k], nums[-k:]
        print(nums)

nums = [1,2,3,4,5,6,7,8]
rotate(nums,3)
