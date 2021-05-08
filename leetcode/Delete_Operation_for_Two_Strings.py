
def minDistance(word1, word2):
    left = word1
    right = word2
    if len(word2) > len(word1):
        left = word2
        right = word1

    left_cnt = len(left)
    right_cnt = len(right)

    dp_cur = [0] * (right_cnt + 1)
    dp_last = [0] * (right_cnt + 1)

    for l in left:
        for r in range(right_cnt):
            dp_cur[r+1] = (dp_last[r] + 1) if l == right[r] else max(dp_cur[r], dp_last[r+1])
            print(l)
            print(dp_cur)
        dp_last, dp_cur = dp_cur, dp_last

    return left_cnt + right_cnt - 2*dp_last[right_cnt]


a = minDistance("food", "money")
print(a)