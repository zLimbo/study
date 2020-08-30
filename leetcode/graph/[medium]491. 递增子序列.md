#### [[medium]491. 递增子序列](https://leetcode-cn.com/problems/increasing-subsequences/)

> 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
>
> ```python
> 示例:
> 
> 输入: [4, 6, 7, 7]
> 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
> 
> ```
>
> **说明:**
>
> 1. 给定数组的长度不会超过15。
> 2. 数组中的整数范围是 [-100,100]。
> 3. 给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/increasing-subsequences
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// dfs

class Solution {
public:
    vector<vector<int>> ans;

    bool isFirst(vector<int>& nums, int last, int pos) {
        while (++last < pos) {
            if (nums[last] == nums[pos]) {
                return false;
            }
        }
        return true;
    }
    
    void dfs(vector<int>& nums, vector<int>& aux, int last, int pos) {
        if (pos == nums.size()) return;
        
        if ((aux.empty() || aux.back() <= nums[pos]) && isFirst(nums, last, pos)) {
            aux.push_back(nums[pos]);
            if (aux.size() >= 2) {
                ans.push_back(aux);
            }
            dfs(nums, aux, pos, pos + 1);
            aux.pop_back();
        }
        dfs(nums, aux, last, pos + 1);
    }

    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<int> aux;
        dfs(nums, aux, -1, 0);
        return ans;
    }

};
```

