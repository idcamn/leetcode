class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices = list()
        for i, w in enumerate(words):
            if x in w:
                indices.append(i)
        return indices