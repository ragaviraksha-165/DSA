nums=[1,2,3,66,7,8]
def longestConsecutive( nums):

        if len(nums) == 0:
            return 0

        #nums = sorted(set(nums))

        count = 1
        lengths = []

        for i in range(len(nums)-1):

            if nums[i] + 1 == nums[i+1]:
                count += 1
            else:
                lengths.append(count)
                count = 1

        lengths.append(count)

        return sum(lengths)
print(longestConsecutive(nums))
