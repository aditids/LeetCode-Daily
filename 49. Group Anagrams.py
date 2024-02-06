# 49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            count = [0]*26
            for i in s:
                count[ord(i)-ord("a")] += 1
            anagrams[str(count)].append(s)
        print(anagrams)
        return anagrams.values()
    # Time complexity - O(m*n) -> m = length of each string and n = length of strs