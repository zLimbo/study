#### [[easy]剑指 Offer 09. 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)

> 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )



```cpp
// cpp
// stack, queue

class CQueue {
    /**
     * Your CQueue object will be instantiated and called as such:
     * CQueue* obj = new CQueue();
     * obj->appendTail(value);
     * int param_2 = obj->deleteHead();
     */

private:
    stack<int> s1,  s2;

public:
    CQueue() { }
    
    void appendTail(int value) {
        s1.push(value);
    }
    
    int deleteHead() {
        if (s2.empty()) {
            if (s1.empty()) return -1;
            while (!s1.empty()) {
                s2.push(s1.top()); s1.pop();
            }
        }
        int ret = s2.top(); s2.pop();
        return ret;
    }
};



```



```python
# python3
# stack, queue

class CQueue:
    # Your CQueue object will be instantiated and called as such:
    # obj = CQueue()
    # obj.appendTail(value)
    # param_2 = obj.deleteHead()
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return -1 if not self.stack2 else self.stack2.pop()


```



