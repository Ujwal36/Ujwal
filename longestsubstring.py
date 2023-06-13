from xmlrpc.client import MAXINT


def lengthOfLongestSubstring(s: str) -> int:
        if len(s) == 0:
            return 0
        else:

            current = s[0]
            maxi = s[0]
            for i in range(1,len(s)):
                current = current + s[i] if s[i] not in current  else current[current.index(s[i])+1:]+ s[i]
                maxi = current if len(current) > len(maxi) else maxi
            print(maxi)
            return len(maxi)
str = "abdap"
print(lengthOfLongestSubstring(str))