class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        res = []
        first, second = 0, 0
        while first < len(firstList) and second < len(secondList):
            head = max(firstList[first][0], secondList[second][0])
            tail = min(firstList[first][1], secondList[second][1])
            if head > tail:
                if firstList[first][0] < secondList[second][0]:
                    first += 1 
                elif firstList[first][0] > secondList[second][0]:
                    second += 1 
                else:
                    first += 1 
                    second += 1 
            else:
                res.append([head, tail])
                if firstList[first][1] < secondList[second][1]:
                    first += 1 
                elif firstList[first][1] > secondList[second][1]:
                    second += 1 
                else:
                    first += 1 
                    second += 1 
        return res 
