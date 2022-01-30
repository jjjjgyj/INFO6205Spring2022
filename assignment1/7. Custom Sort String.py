class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_map = Counter(s)
        res = ""
        for char in order:
            if char in char_map:
                for i in range(char_map[char]):
                    res += char
                del char_map[char]
        
        if not char_map:
            return res 
        else:
            for char, cnt in char_map.items():
                for i in range(cnt):
                    res += char
            return res
        
