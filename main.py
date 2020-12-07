# Exercise: Given the following problem and solution, write a test program, with test cases that you come up with
# on your own to verify the solution. Gather and log success and timing info for each individual test case run both to
# the console and to a unique file.

# The solution we are sending is expected to be functional (bonus points if you find any bugs). But we will run your
# test program with some faulty examples during the interview.

# Expected output:
# Test Case #1: SUCCESS, 11ms.
# Test Case #2: FAILURE, 20ms.

# ... (Formatting unimportant, but at least equivalent information expected)
# Problem: Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all
# unique triplets in the array which gives the sum of zero. The solution set must not contain duplicate triplets.
import self as self


class Solution(object):

    def threeSum(self, nums):
        """
            :type nums: List[int]
            :rtype: List[List[int]]
            """

        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = nums[i] * -1
            s, e = i + 1, N - 1

            while s < e:
                if nums[s] + nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s + 1
                    while s < e and nums[s] == nums[s - 1]:
                        s = s + 1

                elif nums[s] + nums[e] < target:
                    s = s + 1
                else:
                    e = e - 1

        return result
