#### [[easy]面试题 08.03. 魔术索引](https://leetcode-cn.com/problems/magic-index-lcci/)

> 魔术索引。 在数组`A[0...n-1]`中，有所谓的魔术索引，满足条件`A[i] = i`。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回`-1`。若有多个魔术索引，返回索引值最小的一个。
>
> ```shell
> 示例1:
> 
>  输入：nums = [0, 2, 3, 4, 5]
>  输出：0
>  说明: 0下标的元素为0
> 示例2:
> 
>  输入：nums = [1, 1, 1]
>  输出：1
> ```
>
> **说明:**
>
> 1. nums长度在[1, 1000000]之间
> 2. 此题为原书中的 Follow-up，即数组中可能包含重复元素的版本
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/magic-index-lcci
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// 利用有序性质跳跃

class Solution {
public:
    int findMagicIndex(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; ) {
            if (i == nums[i]) {
                return i;
            }
            if (nums[i] > i) {
                i = nums[i];
            } else {
                ++i;
            }
        }
        return -1;
    }
};
```



```python
# python3
# 利用有序性质跳跃

class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        p, n= 0, len(nums)
        while p < n:
            if p == nums[p]:
                return p
            p = nums[p] if nums[p] > p else p + 1
        return -1
```

