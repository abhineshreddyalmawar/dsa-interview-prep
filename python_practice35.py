# python_practice35.py  --  Nov 5, 2026 (Thursday, week 1 of the new routine: 4 new problems a week)
# Problem: Best Time to Buy and Sell Stock (new problem; the start of sliding window; taught from the idea up,
#          then written by me)
# Results: morning Accepted 42/42, 27 ms (beats 100.00%), memory 7.9 MB (beats 23.22%).
#          evening redo from a blank editor, no comments: Accepted 42/42, 26 ms (beats 100.00%),
#          memory 7.9 MB (beats 23.23%).

from typing import List

# ---------------------------------------------------------------
# The six questions
#   1. Name:    Best Time to Buy and Sell Stock
#   2. Does:    buy on one day and sell on a LATER day to make the most profit (0 if no profit is possible)
#   3. Input:   a list of prices of one stock, one price per day (the position is the day)
#   4. Output:  one number: the best profit, e.g. [7, 1, 5, 3, 6, 4] -> 5 (buy at 1, sell at 6)
#   5. Steps every time: say it in one sentence; name input and output with a tiny example;
#      ask "what do I need to remember?"; pick the tool; stage comments, then code;
#      trace the smallest input; say time and space.
#   6. Algorithm (the five jobs):
#        1. PREPARE    -> left = 0 (buy day), right = 1 (sell day), best = 0   three single numbers
#        2. GO THROUGH -> while right < len(prices)
#        3. DECIDE     -> is prices[right] higher than prices[left]?
#        4. UPDATE     -> higher: profit = prices[right] - prices[left]; if profit > best: best = profit
#                         (left stays: it is still the cheapest buy day so far)
#                         not higher: left = right (a cheaper day that comes later is a better buy day)
#        5. MOVE       -> right = right + 1, every round, lined up with the if/else
#        6. RETURN     -> return best, after the loop
#
# Key question: what must I remember? Where my two fingers are (the buy day and the sell day) and the
# best profit so far: three single numbers.
#   "buy before sell / best pair / one pass" -> two pointers plus a best number; the stretch between
#   left and right is a window that slides forward (the start of sliding window).
# ---------------------------------------------------------------


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        best = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                if profit > best:
                    best = profit
            else:
                left = right
            right = right + 1
        return best


# Trace for [7, 1, 5, 3, 6, 4] (positions 0 to 5; positions and values kept apart):
#   left 0 (7), right 1 (1): 1 is lower than 7, no profit  -> left = 1, right = 2
#   left 1 (1), right 2 (5): profit 4, best 4              -> left stays, right = 3
#   left 1 (1), right 3 (3): profit 2, best stays 4        -> right = 4
#   left 1 (1), right 4 (6): profit 5, best 5              -> right = 5
#   left 1 (1), right 5 (4): profit 3, best stays 5        -> right = 6
#   6 < 6 is False, so the loop stops -> return 5
#   Smallest input [5]: right = 1, 1 < 1 is False, the loop never runs -> return best = 0
#   No-profit input [10, 8, 7, 5, 2]: every right price is lower, left keeps jumping to right -> 0
#
# Slips fixed today:
#   1. Thought buying at 1 and selling at 7 was possible: the 7 sits on day 0, BEFORE day 1; the sell day
#      must come AFTER the buy day (the day is later; the price is what is lower).
#   2. Said the cost of checking every pair was O(n): a loop inside a loop is O(n squared).
#   3. Mixed up time and space: the finger walking the list once is time (O(n)); storing left, right,
#      best and profit is space (O(1)).
#   4. In the table, moved BOTH fingers after finding a profit: when there is a profit, left stays (it is
#      still the cheapest buy day) and only right moves.
#   5. Wrote left = left + 1 in the else: left jumps to the RIGHT finger's day (left = right).
#   6. Missing best = 0 in the first version; missing colons; "right - right+1" instead of
#      right = right + 1.
#   7. Trace comments: wrote left=1,6 (a position that does not exist) instead of left=1,5, and 6>4
#      instead of 6>5: keep positions and values apart, and compare with the CURRENT best.
#   8. [5] trace: compared 5 with 6 (from the other example); a one-price list has len 1, so 1 < 1 is
#      False, the loop never runs and best = 0 is returned.
#   9. The "because" described WHAT the code does (a pair); it must say WHY it works.
#
# Complexity: time O(n): the right finger walks the list once; left never walks, it only jumps to where
#               right already is, so no day is visited twice.
#             space O(1): left, right, best and profit are single numbers.
#
# I used X because Y:
# "I used two pointers plus a best number because when the right price is lower, it is a cheaper buy day
#  that comes later, so every future sell day does better with it than with the old buy day. That means I
#  never need to check the other pairs, and one pass is enough."
#
# Interview sentence:
# "I keep a buy pointer and a sell pointer and a best profit. If the sell price is higher than the buy
#  price I update the best profit; if it is lower, I move the buy pointer to the sell pointer, because a
#  cheaper day that comes later is a better day to buy. Time is O(n) and space is O(1)."

if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))   # 5
    print(Solution().maxProfit([7, 6, 4, 3, 1]))      # 0
    print(Solution().maxProfit([5]))                  # 0
    print(Solution().maxProfit([10, 1, 5, 6, 7, 1]))  # 6

# Next: Fri Nov 6: light revision day (no class; Diwali break): the "I used X because Y" sentences and the
# pivot table. Sat Nov 7: Saturday check plus full revision of the 11 course topics.
