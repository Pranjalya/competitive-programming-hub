from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        w1, w2 = Counter(word1), Counter(word2)
        if sorted(w1.values()) != sorted(w2.values()):
            return False
        set_diff = (set(w1.keys())-set(w2.keys())) | (set(w2.keys())-set(w1.keys()))
        if len(set_diff) not in [0, 1]:
            return False
        return True