# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Solution:
    def get_parent_hashmap(self, parent_hashmap, root):
        if root is not None:
            if root.left is not None:
                parent_hashmap[root.left] = root
            if root.right is not None:
                parent_hashmap[root.right] = root
            parent_hashmap = self.get_parent_hashmap(parent_hashmap, root.left)
            parent_hashmap = self.get_parent_hashmap(parent_hashmap, root.right)
        return parent_hashmap
        
    def get_target_node(self, root, target):
        if root is not None:
            if root.val == target:
                return root
            node_left = self.get_target_node(root.left, target)
            node_right = self.get_target_node(root.left, target)
            
            if node_left is not None:
                return node_left
            elif node_right is not None:
                return node_right
            
    def get_k_distant_nodes(self, root, hm, target, k):
        q = Queue()
        q.put((target, 0))
        visited = set([target])
        output = []
        while not q.empty():
            node, dist = q.get()
            if dist == k:
                output.append(node.val)
            neighbours = []
            if node.left:
                neighbours.append(node.left)
            if node.right:
                neighbours.append(node.right)
            if node in hm:
                neighbours.append(hm[node])
            for neighbour in neighbours:
                if neighbour not in visited:
                    q.put((neighbour, dist+1))
                    visited.add(neighbour)
        return output


    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_hashmap = {}
        parent_hashmap = self.get_parent_hashmap(parent_hashmap, root)
        return self.get_k_distant_nodes(root, parent_hashmap, target, k)
        
