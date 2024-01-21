from typing import List
from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Calculate the length of the shortest transformation sequence from 
        beginWord to endWord such that:
        - Only one letter can be changed at a time.
        - Each transformed word must exist in the given wordList.
        
        :param beginWord: A string representing the starting word.
        :param endWord: A string representing the target word.
        :param wordList: A list of strings representing the available words.
        :return: An integer representing the length of the shortest 
                 transformation sequence.
        """
        # Constants and data structures
        MOD = 10 ** 11 + 7
        wordList.append(beginWord)
        sToIndx = defaultdict(set)
        indxToNei = defaultdict(set)

        n, m = len(wordList), len(wordList[0])
        hashes = [0] * n

        # Calculate hashes
        for i in range(n):
            for j in range(m):
                hashes[i] = (26 * hashes[i] + (ord(wordList[i][j]) - ord('a') + 1)) % MOD

        # Populate dictionaries
        base = 1
        for j in range(m - 1, -1, -1):
            for i in range(n):
                new_h = (hashes[i] - base * (ord(wordList[i][j]) - ord('a') + 1)) % MOD
                sToIndx[wordList[i]].add(new_h)
                indxToNei[new_h].add(wordList[i])
            base = 26 * base % MOD

        # BFS to find the shortest transformation sequence
        q = [beginWord]
        res = 0
        visited = set()
        visited.add(beginWord)
        while q:
            for _ in range(len(q)):
                cur = q.pop(0)
                if cur == endWord:
                    return res + 1
                for neiI in sToIndx[cur]:
                    for nei in indxToNei[neiI]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res += 1

        return 0


# Tests
if __name__ == '__main__':
    instance = Solution()
    result = instance.ladderLength(
        beginWord="hit", 
        endWord="cog", 
        wordList=["hot", "dot", "dog", "lot", "log"]
    )
    print(result)
