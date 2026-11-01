# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 105
# s consists of English letters, digits, symbols and spaces.
 

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        
        입력받은 문자열 s 에서 중복되지 않는 가장 긴 부분 문자열의 길이를 반환하는 함수
        
        1. 문자열을 입력받음
        
        2. 문자열 내에 포함되는 인덱스당 문자를 확인 >>
        
        영어의 경우 [A-Z], [a-z]  범위
        한국어의 경우 [가-핳] 범위에 해당
        
        중국어 일본어의 경우 [一-龥], [ぁ-ゔ], [ァ-ヴ] 범위에 해당
        
        나머진 유기하고 : 예외 처리 해야함 >>
        문자에 해당하더라도, 해당 범위(언어)에 해당하지 않으면 예외문구 출력 : 척화비
        """
        start = 0
        max_leng = 0  # 0으로 초기화
        
        n = len(s) # 문자열의 길이를 저장
        
        for end in range(n) : 
            for i in range(start, end) :
                if s[i] == s[end] :  # 이 때 s는 위에서 입력받은 문자열
                    start = i + 1
                    break
            max_leng = max(max_leng, end - start + 1) # 문자열이 어떤 값이 들어오더라도 1글자의 최솟값 출력
        return  max_leng
    



if __name__ == "__main__":
    solution = Solution()

    # result = solution.lengthOfLongestSubstring("abcabcbb")
    result = solution.lengthOfLongestSubstring(input("문자열을 입력하세요: "))

    print("결과:", result)