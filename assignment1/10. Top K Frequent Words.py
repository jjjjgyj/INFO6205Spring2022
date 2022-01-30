class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_count = Counter(words)
        words_count_list = [(freq, word) for word, freq in words_count.items()]
        words_count_list.sort(key = lambda x:(-x[0], x[1]))
        res = []
        for freq, word in words_count_list:
            res.append(word)
            k -= 1
            if k == 0:
                return res
        
        
