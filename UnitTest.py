from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {
            1: {'nums': [3,1], 'output': 2},
            2: {'nums': [2,2,2], 'output': 7},
            3: {'nums': [3,2,1,5], 'output': 6}
        }
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        nums, output = self.__testCases[1].values()
        result = self.__obj.countMaxOrSubsets(nums = nums)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        nums, output = self.__testCases[2].values()
        result = self.__obj.countMaxOrSubsets(nums = nums)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case3(self):
        nums, output = self.__testCases[3].values()
        result = self.__obj.countMaxOrSubsets(nums = nums)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()