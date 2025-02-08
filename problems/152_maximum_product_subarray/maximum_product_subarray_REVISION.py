from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize the result with the maximum value from the input list.
        # This works because the product of a subarray can be a single element.
        res = max(nums)

        # These variables will hold the minimum and maximum product ending at the current index.
        # Both are initialized to 1 since it's the multiplicative identity.
        minProduct = 1
        maxProduct = 1

        # Iterate over each number in the list.
        for num in nums:
            # When encountering zero, it resets any product sequence.
            # Reset minProduct and maxProduct to 1 because the next subarray starts fresh.
            if num == 0:
                minProduct = 1
                maxProduct = 1
                continue

            # Since the current number can be negative, the minimum product so far might become
            # the maximum when multiplied by this negative number and vice versa.
            # Temporarily store the current minProduct value.
            temp = minProduct

            # Update minProduct: It could be the current number itself,
            # or the product of the current number with the previous min or max product.
            minProduct = min(num, num * minProduct, num * maxProduct)

            # Update maxProduct: Similar logic applies to find the maximum subarray product ending here.
            maxProduct = max(num, num * temp, num * maxProduct)

            # Update the overall result with the maximum product encountered so far.
            res = max(maxProduct, res)

        return res


# Instance creation and sample usage of the function.
solution = Solution()
print(solution.maxProduct([2, 3, -2, 4]))  # Expected output: 6 (product of [2,3])
