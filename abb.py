import string


class Solution:
    longest_len = 0
    longest_pattern = ''
    abc = string.ascii_lowercase

    def find_longest_pattern(self, pattern):
        start = 0
        end = 1

        while True:
            if pattern in self.abc:
                print(len(pattern))
                self.longest_len = len(pattern)
                self.longest_pattern = pattern
                pattern = input[start:end]
                print(pattern)


s = Solution()
s.find_longest_pattern('xyzabc')
