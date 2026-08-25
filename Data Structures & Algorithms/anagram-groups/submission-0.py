class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            sorted_words = str(sorted(word))

            if sorted_words not in anagrams:
                anagrams[sorted_words] = []
            anagrams[sorted_words].append(word)

        return list(anagrams.values())