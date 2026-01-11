from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams_technically_faster(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for s in strs:
            mp[tuple(sorted(s))].append(s)
        return list(mp.values())

    def groupAnagrams_optimal(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - 97] += 1
            mp[tuple(count)].append(s)
        return list(mp.values())
