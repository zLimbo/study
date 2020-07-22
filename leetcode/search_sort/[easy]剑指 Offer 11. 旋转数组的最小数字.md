#### [[easy]剑指 Offer 11. 旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)

> 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。
>
> **示例 1：**
>
> ```shell
> 输入：[3,4,5,1,2]
> 输出：1
> ```
>
> **示例 2：**
>
> ```bash
> 输入：[2,2,2,0,1]
> 输出：0
> ```
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// 二分查找

class Solution {
public:
    int minArray(vector<int>& numbers) {
        int lo = 0, hi = numbers.size() - 1;

        while (lo < hi) {
            int md = lo + (hi - lo >> 1);
            if (numbers[md] < numbers[hi]) hi = md;
            else if (numbers[md] > numbers[hi]) lo = md + 1;
            else --hi;
        }
        return numbers[lo];
    }
};
```



```python
# python3
# 二分查找

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        lo, hi = 0, len(numbers) - 1
        
        while lo < hi:
            md = (lo + hi) // 2
            if numbers[md] < numbers[hi]:
                hi = md
            elif numbers[md] > numbers[hi]:
                lo = md + 1
            else:
                hi -= 1

        return numbers[lo]
```



```java
// java
// 二分查找

class Solution {
    public int minArray(int[] numbers) {
        int lo = 0, hi = numbers.length - 1;

        while (lo < hi) {
            int md = lo + (hi - lo >> 1);
            if (numbers[md] < numbers[hi]) hi = md;
            else if (numbers[md] > numbers[hi]) lo = md + 1;
            else --hi;
        }

        return numbers[lo];
    }
}
```



```javascript
// javascript
// 二分查找

/**
 * @param {number[]} numbers
 * @return {number}
 */
var minArray = function(numbers) {
    let lo = 0, hi = numbers.length;

    while (lo < hi) {
        let md = lo + hi >>> 1;
        if (numbers[md] < numbers[hi]) hi = md;
        else if (numbers[md] > numbers[hi]) lo = md + 1;
        else --hi; 
    }
    return numbers[lo];
};
```

