class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        q = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'prqs', '8':'tuv', '9':'wxyz'}
        ans = []
        if len(digits)==0:
            return []
        for iw in q[digits[0]]:
            if len(digits) >= 2:
                for iiw in q[digits[1]]:
                    if len(digits) >= 3:
                        for iiiw in q[digits[2]]:
                            if len(digits) >= 4:
                                for iiiiw in q[digits[3]]:
                                    ans.append(iw+iiw+iiiw+iiiiw)
                            else:
                                ans.append(iw+iiw+iiiw)
                    else:
                        ans.append(iw+iiw)
            else:
                ans.append(iw)
        return ans


q = Solution()
print(q.letterCombinations(digits = ""))