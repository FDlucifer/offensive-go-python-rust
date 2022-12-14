package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSubtree(s *TreeNode, t *TreeNode) bool {
	if s == nil {
		return false
	}
	return check(s, t) || isSubtree(s.Left, t) || isSubtree(s.Right, t)
}

func check(a, b *TreeNode) bool {
	if a == nil && b == nil {
		return true
	}
	if a == nil || b == nil {
		return false
	}
	if a.Val == b.Val {
		return check(a.Left, b.Left) && check(a.Right, b.Right)
	}
	return false
}

func main() {
	root := &TreeNode{Val: 3, Left: &TreeNode{Val: 4, Left: &TreeNode{Val: 1}, Right: &TreeNode{Val: 2}}, Right: &TreeNode{Val: 5}}
	subRoot := &TreeNode{Val: 4, Left: &TreeNode{Val: 1}, Right: &TreeNode{Val: 2}}
	fmt.Println(isSubtree(root, subRoot)) // 输出: true
}
