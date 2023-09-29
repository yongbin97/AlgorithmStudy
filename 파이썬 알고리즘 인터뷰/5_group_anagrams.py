from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for word in strs:
            word_split = sorted(word)
            sorted_word = "".join(word_split)

            if sorted_word in result_dict.keys():
                result_dict[sorted_word].append(word)
            else:
                result_dict[sorted_word] = [word]

        return list(result_dict.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

solution = Solution()
print(solution.groupAnagrams(strs))