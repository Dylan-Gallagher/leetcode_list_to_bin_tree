import ast


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_bin_tree(node_list_str):
    if node_list_str == "[]":
        return None

    node_val_list = ast.literal_eval(node_list_str.replace("null", "None"))

    node_list = [None] * len(node_val_list)

    for i, node_val in enumerate(node_val_list):
        if isinstance(node_val, int):
            node_list[i] = TreeNode(node_val)
    
    for i, node in enumerate(node_list):
        if node:
            left_child_index = 2*i + 1
            right_child_index = 2*i + 2
            
            if left_child_index < len(node_list):
                node.left = node_list[left_child_index]
            if right_child_index < len(node_list):
                node.right = node_list[right_child_index]

    return node_list[0]

if __name__ == "__main__":
    # Example Usage
    root = list_to_bin_tree("[3,9,20,null,null,15,7]")

    def maxDepth(root):
        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))

        node = root
        return depth(node)

    print(maxDepth(root))
