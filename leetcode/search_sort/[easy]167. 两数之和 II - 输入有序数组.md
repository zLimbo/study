#### [[easy]167. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)

> 给定一个已按照升序排列的有序数组，找到两个数使得它们相加之和等于目标数。
>
> 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
>
> **说明:**
>
> - 返回的下标值（index1 和 index2）不是从零开始的。
> - 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
>
> **示例:**
>
> ```shell
> 输入: numbers = [2, 7, 11, 15], target = 9
> 输出: [1,2]
> 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
> ```
>
> 
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```cpp
// cpp
// 二分查找 O(nlogn)

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        for (int i = 0; i < n; ++i) {
            int rest = target - numbers[i];
            int lo = i + 1, hi = n;
            while (lo < hi) {
                int md = lo + (hi - lo >> 1);
                if (numbers[md] < rest) lo = md + 1;
                else if (numbers[md] > rest) hi = md;
                else return vector<int>{i+1, md+1};
            }
        }
        return vector<int>();
    }
};
```



```cpp
// cpp
// 双指针

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int lo = 0, hi = numbers.size() - 1;
        while (true) {
            int s = numbers[lo] + numbers[hi];
            if (s < target) ++lo;
            else if (s > target) --hi;
            else return vector<int>{lo + 1, hi + 1};
        }
        return vector<int>();
    }
};
```



```python
# python3
# 双指针

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        lo, hi = 0, n-1
        while True:
            s = numbers[lo] + numbers[hi]
            if s < target:
                lo += 1
            elif s > target:
                hi -= 1
            else:
                return [lo+1, hi+1]
```



```java
// java
// 双指针

class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int lo = 0, hi = numbers.length - 1;
        while (true) {
            int s = numbers[lo] + numbers[hi];
            if (s < target) ++lo;
            else if (s > target) --hi;
            else return new int[]{++lo, ++hi};
        }
    }
}
```

