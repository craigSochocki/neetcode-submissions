class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            current_anagrams = anagrams_dict.setdefault(sorted_string, [])
            current_anagrams.append(string)
            anagrams_dict[sorted_string] = current_anagrams
        return [anagram for anagram in anagrams_dict.values()]