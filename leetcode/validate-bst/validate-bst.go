package validatebst

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func checkBST(root, left, right *TreeNode) bool {
	if root == nil {
		return true
	}
	if left != nil && left.Val >= root.Val {
		return false
	}
	if right != nil && right.Val <= root.Val {
		return false
	}
	return (checkBST(root.Left, left, root) && checkBST(root.Right, root, right))
}

func isValidBST(root *TreeNode) bool {
	return checkBST(root, nil, nil)
}
