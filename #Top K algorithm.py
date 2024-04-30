#Top K algorithm
#Given and integer array numbs and an integer k, return k most frequent elements.


def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    
    res = []
    for i in range(len(freq) - 1, 0 , -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

nums = [1, 1, 1, 2, 2, 100]
k = 6
print(topKFrequent(nums, k))



#Sliding window

#Backtracking

#Dynamic Programming

#DFS and BFS DFS IS VERY IMPORTANT

def dfs(graph, node):
    visited = []
    stack = deque()

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        print(s, end = " ")

        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)