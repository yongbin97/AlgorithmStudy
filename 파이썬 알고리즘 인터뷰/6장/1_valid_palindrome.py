class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [alpha_num.lower() for alpha_num in s if alpha_num.isalnum()]
        return s_list == s_list[::-1]


solution = Solution()
text_string = [
    "A man, a plan, a canal: Panama",
    "race a car",
    " "
]
for s in text_string:
    print(solution.isPalindrome(s))
