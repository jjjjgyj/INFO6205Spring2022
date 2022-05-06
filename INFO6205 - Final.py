#!/usr/bin/env python
# coding: utf-8

# Question1: String Compression: Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original 
# string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).


def str_comp(s):
    left = 0
    temp = []
    cnt = 1
    for right in range(len(s)):
        if right == 0:
            temp.append(s[right])
            temp.append(str(cnt))
            continue
        if s[left] == s[right]:
            cnt += 1
            temp.pop()
            temp.append(str(cnt))
        else:
            cnt = 1
            left = right
            temp.append(s[left])
            temp.append(str(cnt))

    res = "".join(temp)
    return res if len(res) < len(s) else s


# Question2: Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number 
# of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may 
# assume all four edges of the grid are all surrounded by water.


from collections import deque
     
def find_islands(grid):
    visited = set()
    queue = deque()
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1" and (i, j) not in visited:
                visited.add((i, j))
                queue.append((i, j))
                bfs(queue, visited, grid)
                res += 1
    return res

def bfs(queue, visited, grid):
    while queue:
        row, col = queue.popleft()
        for delta_row, delta_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = row + delta_row
            new_col = col + delta_col 
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == "1" and(new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))


# Question3: Given an array of strings strs, group the anagrams together. You can return the answer in any order. 
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using 
# all the original letters exactly once.


from collections import defaultdict

def group_anagrams(strs):
    word_map = defaultdict(set)
    for word in strs:
        chars = [0] * 26
        for c in word:
            chars[ord(c) - ord("a")] = chars[ord(c) - ord("a")] + 1 
        word_map[tuple(chars)].add(word)
    
    res = []
    for word_list in word_map.values():
        temp = []
        for word in word_list:
            temp.append(word)
        res.append(temp)
    
    return res


# Question4: Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. 
# According to the definition of LCA on Wikipedia: The lowest common ancestor is defined between two nodes p and q 
# as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).

def LCA(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)

    if left and right:
        return root
    if left:
        return right 
    if right:
        return left 
    
    return None

