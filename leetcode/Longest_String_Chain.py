class Solution:
    def longestStrChain(self, words):
        sorted_list = sorted(words, key=len)
        dp = [0 for i in words]
        answer = 0
        for idx,word in enumerate(sorted_list):
            word_len = len(word)
            for idx_2 in range(idx+1, len(sorted_list)):
                for i in range(len(sorted_list[idx_2])):
                    word2 = sorted_list[idx_2][:i] + sorted_list[idx_2][i+1:]
                    if word_len< len(word2):
                        break
                    if word == word2:
                        dp[idx_2] = max(dp[idx_2], dp[idx]+1)
                    answer = max(answer,dp[idx_2])

        print(dp)
        return answer+1





a = Solution()
b = a.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"])
print(b)
            

