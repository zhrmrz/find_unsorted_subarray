class Sol:
    def find_unsorted_subarray(self,nums):
        lst=0
        fst=0
        sorted_nums=sorted(nums)
        for i in range(len(nums)//2):
            if sorted_nums[i]!=nums[i]:
                fst=i
                break
        for i in reversed(range(len(nums)//2+1,len(nums))):
            if sorted_nums[i]!=nums[i]:
                lst=i
                break

        return lst-fst+1
