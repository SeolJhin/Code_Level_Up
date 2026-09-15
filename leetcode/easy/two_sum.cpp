// <!-- https://leetcode.com/problems/two-sum/
// Two Sum
// C++


// You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

 

// Example 1:

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
// Example 2:

// Input: nums = [3,2,4], target = 6
// Output: [1,2]
// Example 3:

// Input: nums = [3,3], target = 6
// Output: [0,1]
 

// Constraints:

// 2 <= nums.length <= 104
// -109 <= nums[i] <= 109
// -109 <= target <= 109
// Only one valid answer exists.
 

// Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?



// - 사이트: leetCode
// - 문제: 2개의 숫자를 더하고, 리스트에 어느 요소인지도 같이 출력
// - 난이도: easy
// - 유형: 
// - 시간복잡도:  less than O(n2)
// - 공간복잡도: -
// - 복습 필요: Yes -->


// ==========================


#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        
        std::vector<int> nums;
        std:: cout << "숫자들 입력";


        int target;
        std:: cout << "원하는 숫자";

        for (int i = 0; i < nums.size(); i++) {
            
            int num1, num2;

            num1 = nums[i];
            
            for (int j = 0; j < nums.size(); j++){

                num2 = nums[j];

                if (num1 + num2 == target) {
                    return {i, j};
                }

                return {target, num1, num2};

            }

        }

        
    }
};