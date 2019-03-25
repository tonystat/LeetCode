# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class solution:
    def TwoSum(self, nums: list, target: int) -> list:
        store = dict()
        for id,x in enumerate(nums):
            if target - x in store:
                return [store[target-x],id]
            else:
                store[x] = id
        return [-1, -1]



a = solution().TwoSum([2,7,11,15],9)
print(a)
