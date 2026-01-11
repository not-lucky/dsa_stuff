from collections import defaultdict
from itertools import permutations


class Solution:
    def isAnagram_brute(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for p in permutations(s):
            if "".join(p) == t:
                return True

        return False

    def isAnagram_map(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mps = defaultdict(int)
        mpt = defaultdict(int)
        for i in range(len(s)):
            mps[s[i]] += 1
            mpt[t[i]] += 1

        return mps == mpt

    def isAnagram_optimal(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        diff = [0] * 26

        for i in range(len(s)):
            diff[ord(s[i]) - 97] -= 1
            diff[ord(t[i]) - 97] += 1

        return all(v == 0 for v in diff)
