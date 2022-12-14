package main

import (
	"container/list"
	"fmt"
	"strconv"
)

type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

func connect(root *Node) *Node {
	res := [][]*Node{}
	if root == nil { //防止为空
		return root
	}
	queue := list.New()
	queue.PushBack(root)
	var tmpArr []*Node
	for queue.Len() > 0 {
		length := queue.Len() //保存当前层的长度，然后处理当前层（十分重要，防止添加下层元素影响判断层中元素的个数）
		for i := 0; i < length; i++ {
			node := queue.Remove(queue.Front()).(*Node) //出队列
			if node.Left != nil {
				queue.PushBack(node.Left)
			}
			if node.Right != nil {
				queue.PushBack(node.Right)
			}
			tmpArr = append(tmpArr, node) //将值加入本层切片中
		}
		res = append(res, tmpArr) //放入结果集
		tmpArr = []*Node{}        //清空层的数据
	}
	//遍历每层元素,指定next
	for i := 0; i < len(res); i++ {
		for j := 0; j < len(res[i])-1; j++ {
			res[i][j].Next = res[i][j+1]
		}
	}
	return root
}

//添加遍历输出结果的代码
func traverse(root *Node) []string {
	res := []string{}
	queue := list.New()
	queue.PushBack(root)
	for queue.Len() > 0 {
		node := queue.Remove(queue.Front()).(*Node)
		if node.Left != nil {
			queue.PushBack(node.Left)
		}
		if node.Right != nil {
			queue.PushBack(node.Right)
		}
		if node.Next != nil {
			res = append(res, strconv.Itoa(node.Val), "#") //将整型转换成字符串
		} else {
			res = append(res, strconv.Itoa(node.Val))
		}
	}
	return res
}

func main() {
	root := &Node{Val: 1, Left: &Node{Val: 2, Left: &Node{Val: 4}, Right: &Node{Val: 5}}, Right: &Node{Val: 3, Left: nil, Right: &Node{Val: 7}}}
	connect(root)
	fmt.Println(traverse(root)) // 输出 [1, #, 2, 3, #, 4, 5, 7, #]
}
