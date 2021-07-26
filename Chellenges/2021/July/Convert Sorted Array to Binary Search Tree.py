class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sortedArrayToBST(arr):

    if len(arr)==0:
        return None
    if len(arr)==1:
        return TreeNode(arr[0])

    midst = len(arr)//2
    root = TreeNode(arr[midst])
    root.left = sortedArrayToBST(arr[:midst])
    root.right = sortedArrayToBST((arr[midst+1:]))
    return root


if __name__ == '__main__':
    print(
        sortedArrayToBST(arr=
            [-10,-3,0,5,9]
                                  ))
