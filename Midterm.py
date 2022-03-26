# Question 1 
# Input: nums = [0,1,3,50,75], lower = 0, upper = 99
# Output: ["2","4->49","51->74","76->99"]

def missing (nums, lower, upper):
    res = []
    nums = set(nums)
    start, end = -float("inf"), -float("inf")
    
    for num in range(lower, upper + 1):
        if num not in nums and start < 0:
            start = num

        if start >= 0: 
            string = ""
            if num in nums:
                if num - 1 == start: 
                    string = str(start)
                else: 
                    string = str(start) + str("->") + str(num - 1) 
                res.append(string)
                start, end = -float("inf"), -float("inf")

            if num == upper:
                string = str(start) + str("->") + str(num)     
                res.append(string)
                start, end = -float("inf"), -float("inf")      
    return res 

  
# Question 2
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]

def add_integers(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1 
    
    l1_num, l2_num = "", ""
    
    while l1:
        l1_num += str(l1.val) 
        l1 = l1.next
        
    while l2:
        l2_num += str(l2.val) 
        l2 = l2.next
        
    l1_num = int(l1_num)
    l2_num = int(l2_num)
    res_num = str(l1_num + l2_num)
    
    dummy = ListNode(None)
    curr = dummy
    for str_val in res_num:
        node = ListNode(int(str_val))
        curr.next = node
        curr = curr.next
    
    return dummy.next


# Question 3
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

def getTree(preOrder, inOrder):
    preIndex = [0]
    return buildTree(preOrder, inOrder, preIndex, 0, len(preOrder) - 1)

def findIndex(arr, start, end, val):
    for i in range(start, end + 1):
        if arr[i] == val:
            return i
    return -1

def buildTree(preOrder, inOrder, preIndex, start, end):
    if start > end or preIndex.data >= len(preOrder):
        return None
    
    node = TreeNode(preOrder[preIndex.data])
    preIndex.data += 1 
    
    inOrderIndex = findIndex(inOrder, start, end, node.data)
    if inOrderIndex == -1:
        node.left = None
        node.right = None
    else: 
        node.left = buildTree(preOrder, inOrder, preIndex, start, inOrderIndex - 1)
        node.right = buildTree(preOrder, inOrder, preIndex, inOrderIndex + 1, end)
    
    return node
            

# Question 4
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]

def merge_intervals(intervals):
    intervals.sort(key = lambda x:x[0])
    res = []
    for i in range(len(intervals)):
        if i == 0:
            res.append(intervals[0])
        if intervals[i][0] <= res[-1][1]:
            res[-1][1] = intervals[i][1]
        else:
            res.append(intervals[i])

    return res 
