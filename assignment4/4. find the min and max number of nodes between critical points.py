class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        prev = None
        temp = head

        mini, maxi = 10 ** 5, 0
        count = 1

        diff = 10 ** 5
        while temp.next.next != None:
            prev = temp
            temp = temp.next
            count += 1

            if prev.val > temp.val < temp.next.val or prev.val < temp.val > temp.next.val:

                if maxi != 0:
                    mini = min(mini, count - maxi)
                diff = min(diff, count)
                maxi = count

        if diff == 10 ** 5 or mini == 10 ** 5:
            return [-1, -1]
