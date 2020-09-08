#### [[medium]215. 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)

> 在未排序的数组中找到第 **k** 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
>
> ```python
> 示例 1:
> 
> 输入: [3,2,1,5,6,4] 和 k = 2
> 输出: 5
> 示例 2:
> 
> 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
> 输出: 4
> ```
>
> **说明:**
>
> 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// 快速排序

class Solution {
public:

    int quick_n_max(vector<int>& nums, int left, int right, int k) {
        while (left <= right) {
            int z = rand() % (right - left + 1) + left;
            swap(nums[z], nums[right]);
            int pre = left - 1;
            for (int i = left; i < right; ++i) {
                if (nums[i] > nums[right]) {
                    swap(nums[++pre], nums[i]);
                }
            }
            swap(nums[++pre], nums[right]);
            int cnt = pre - left + 1;
            if (k == cnt) return nums[pre];
            if (cnt < k) {
                left = pre + 1;
                k -= cnt;
            } else {
                right = pre - 1;
            }
        }
        return -1;
    }


    int findKthLargest(vector<int>& nums, int k) {
        return quick_n_max(nums, 0, nums.size() - 1, k);
    }
};
```



```cpp
// cpp
// heap


template<typename T, typename Cmp=less<T>>
void heap_filter(vector<T>& v, int low, int high, int parent, Cmp cmp=Cmp()) {
    while (parent < (high - low) / 2) {
        int child = parent * 2 + 1;
        if (cmp(v[low + child], v[low + child + 1])) ++child;
        if (cmp(v[low + parent], v[low + child]))
            swap(v[low + parent], v[low + child]);
        parent = child;
    }
    if (parent == (high - low - 1) / 2 && (high - low & 1)) {
        int child = parent * 2 + 1;
        if (cmp(v[low + parent], v[low + child]))
            swap(v[low + parent], v[low + child]);
    }
}

template<typename T, typename Cmp=less<T>>
void heap_make(vector<T>& v, int low, int high, Cmp cmp=Cmp()) {
    if (high - low < 2) return;
    int parent = (high - low - 1) / 2;
    while (parent >= 0) {
        heap_filter(v, low, high, parent, cmp);
        --parent;
    }
}

template<typename T, typename Cmp=less<T>>
void heap_push(vector<T>& v, int low, int high, Cmp cmp=Cmp()) {
    int child = high - low;
    while (child > 0) {
        int parent = (child - 1) / 2;
        if (cmp(v[low + parent], v[low + child]))
            swap(v[low + parent], v[low + child]);
        child = parent;
    }
}


template<typename T, typename Cmp=less<T>>
void heap_pop(vector<T>& v, int low, int high, Cmp cmp=Cmp()) {
    swap(v[low], v[high--]);
    heap_filter(v, low, high, 0, cmp);
}


template<typename T, typename Cmp=less<T>>
bool heap_check(vector<T>& v, int low, int high, Cmp cmp=Cmp()) {
    if (high - low < 2) return true;
    for (int i = 0; i < (high - low) / 2; ++i) {
        assert(!cmp(v[low + i], v[low + 2 * i + 1]));
        assert(!cmp(v[low + i], v[low + 2 * i + 2]));
    }
    if (high - low & 1) {
        assert(!cmp(v[low + (high - low - 1) / 2], v[high]));
    }
    return true;
}


class Solution {
public:

    int findKthLargest(vector<int>& nums, int k) {

        vector<int> v;
        
        for (int x: nums) {
            if (v.size() == k) {
                if (x > v[0]) {
                    v[0] = x;
                    heap_filter(v, 0, v.size() - 1, 0, greater<int>());
                }
            } else {
                v.push_back(x);
                heap_push(v, 0, v.size() - 1, greater<int>());
            }
        }
        return v[0];
    }
};
```

