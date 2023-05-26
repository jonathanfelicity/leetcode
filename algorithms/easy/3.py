class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        count = 0
        prev_value = 0

        for char in s:
            value = dic.get(char)
            if value > prev_value:
                count += value - 2 * prev_value
            else:
                count += value
            prev_value = value

        return count
