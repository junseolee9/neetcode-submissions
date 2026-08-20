class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}

        for ch in s:
            if ch not in counter:
                counter[ch] = 0
            counter[ch] += 1

        for ch in t:
            if ch not in counter:
                return False
            counter[ch] -= 1
            if counter[ch] == 0:
                del counter[ch]
        
        return not counter