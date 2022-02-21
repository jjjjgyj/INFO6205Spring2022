class Solution(object):
    def numComponents(self, head, G):

        p, prev, count, G = head, False, 0, set(G)
        while p:
            if p.val in G and not prev:
                count += 1
            prev, p = p.val in G, p.next;
        
        return count
