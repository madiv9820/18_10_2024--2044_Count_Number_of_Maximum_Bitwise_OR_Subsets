# Maximum OR Value Subset Counting Approaches

- ## Recursive Approach

    - ### Intuition
        - The goal of this algorithm is to count the number of subsets in a list of integers nums that achieve the maximum bitwise OR value. The bitwise OR operation combines the binary representation of numbers, and our task is to explore all possible combinations (subsets) of nums to determine which of these combinations can yield the maximum OR value.
    - ### Approach
        1. __Calculate Maximum OR Value:__ First, we determine the maximum possible OR value that can be obtained from all elements in nums. This is done using the reduce function to apply the bitwise OR operation across all numbers.

        2. __Recursive Subset Counting:__ We then use a recursive helper function count_Subsets that counts the subsets that yield this maximum OR value:
            - The function takes the current index and the current OR value as parameters.
            - __Base Case:__ When we reach the end of the list (index == len(nums)), we check if the current_or matches the max_or. If it does, we return 1 (indicating one valid subset); otherwise, we return 0.
            - __Recursive Choices:__ For each element, we have two choices:
                - Exclude the current element and proceed to the next.
                - Include the current element in the OR calculation and proceed to the next.
            - The total count is obtained by summing the results of both choices.

        3. __Return Count:__ Finally, we initiate the counting process by calling the helper function with the starting index and an initial OR of 0.

    - ### Time and Space Complexity
        - __Time Complexity:__ ___O(2<sup>n</sup>)___

            The algorithm explores all possible subsets of nums. For each element, there are two choices (include or exclude), leading to 2<sup>n</sup> total combinations, where n is the number of elements in nums.

        - __Space Complexity:__ __O(n)__
        
            The space complexity is primarily due to the recursion stack. In the worst case, the recursion can go as deep as the length of nums, resulting in a space usage of O(n).

    - ### Code
        ```python3 []
        from typing import List
        from functools import reduce

        class Solution:
            def countMaxOrSubsets(self, nums: List[int]) -> int:
                # Calculate the maximum OR value that can be obtained from all subsets
                max_or = reduce(lambda x, y: x | y, nums)

                # Helper function to count subsets that achieve the max OR value
                def count_Subsets(index: int = 0, current_or: int = 0) -> int:
                    # Base case: if we've considered all elements
                    if index == len(nums):
                        # Return 1 if the current OR matches the max OR, otherwise return 0
                        return 1 if current_or == max_or else 0
                    
                    # Choice 1: Exclude the current number and move to the next
                    choice1 = count_Subsets(index + 1, current_or)
                    # Choice 2: Include the current number and move to the next
                    choice2 = count_Subsets(index + 1, current_or | nums[index])

                    # Return the total count from both choices
                    return choice1 + choice2
                
                # Start counting subsets from the first index and initial OR of 0
                return count_Subsets()

        # Time Complexity: O(2^n) where n is the length of nums, as we explore all subsets.
        # Space Complexity: O(n) for the recursion stack in the worst case.
        ```

- ## Memoization Approach

    - ### Intuition
        - The goal of this algorithm is to count the number of subsets in a list of integers `nums` that achieve the maximum bitwise OR value. The bitwise OR operation combines the binary representation of numbers, and our task is to explore all possible combinations (subsets) of `nums` to determine which of these combinations can yield the maximum OR value.

    - ### Approach
        1. **Calculate Maximum OR Value**: First, we determine the maximum possible OR value that can be obtained from all elements in `nums`. This is done using the `reduce` function to apply the bitwise OR operation across all numbers.

        2. **Memoized Recursive Subset Counting**: We then use a recursive helper function `count_Subsets` that counts the subsets that yield this maximum OR value:
            - The function takes the current index and the current OR value as parameters.
            - **Base Case**: When we reach the end of the list (`index == len(nums)`), we check if the `current_or` matches the `max_or`. If it does, we return 1 (indicating one valid subset); otherwise, we return 0.
            - **Memoization**: We use a cache (dictionary) to store results of previously computed states to avoid redundant calculations.
            - **Recursive Choices**: For each element, we have two choices:
                - Exclude the current element and move to the next.
                - Include the current element in the OR calculation and move to the next.
            - The total count is obtained by summing the results of both choices and storing it in the cache.

        3. **Return Count**: Finally, we initiate the counting process by calling the helper function with the starting index and an initial OR of 0.

    - ### Time and Space Complexity
        - __Time Complexity:__ ___O(n⋅m)___
            - The time complexity arises from the memoization that may compute results for each combination of index and current_or, where n is the number of elements in nums and m is the range of possible OR values.

        - __Space Complexity:__ 
            - ___O(n)___ for the recursion stack, which can go as deep as the length of nums.
            - ___O(n⋅m)___ for the cache that stores results of previously computed states based on the index and the value of current_or.

    - ### Code
        ```python3 []
        from typing import List
        from functools import reduce

        class Solution:
            def countMaxOrSubsets(self, nums: List[int]) -> int:
                # Calculate the maximum OR value that can be obtained from all subsets
                max_or = reduce(lambda x, y: x | y, nums)

                # Dictionary to cache results of previously computed states
                cache = {}

                # Helper function to count subsets that achieve the max OR value
                def count_Subsets(index: int = 0, current_or: int = 0) -> int:
                    # Base case: if we've considered all elements
                    if index == len(nums):
                        # Return 1 if the current OR matches the max OR, otherwise return 0
                        return 1 if current_or == max_or else 0
                    
                    # Check if the current state has already been computed
                    if (index, current_or) not in cache:
                        # Choice 1: Exclude the current number and move to the next
                        choice1 = count_Subsets(index + 1, current_or)
                        # Choice 2: Include the current number and move to the next
                        choice2 = count_Subsets(index + 1, current_or | nums[index])

                        # Cache the result of the current state
                        cache[(index, current_or)] = choice1 + choice2
                    
                    # Return the cached result for the current state
                    return cache[(index, current_or)]
                
                # Start counting subsets from the first index and initial OR of 0
                return count_Subsets()
        ```