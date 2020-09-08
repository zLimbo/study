#### [[medium]347. 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/)

> 给定一个非空的整数数组，返回其中出现频率前 ***k\*** 高的元素。
>
> ```python
> 示例 1:
> 
> 输入: nums = [1,1,1,2,2,3], k = 2
> 输出: [1,2]
> 示例 2:
> 
> 输入: nums = [1], k = 1
> 输出: [1]
> ```
>
> **提示：**
>
> - 你可以假设给定的 *k* 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
> - 你的算法的时间复杂度**必须**优于 O(*n* log *n*) , *n* 是数组的大小。
> - 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
> - 你可以按任意顺序返回答案。
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/top-k-frequent-elements
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// hash + 最小堆

class Solution {
public:

    static bool cmp(const pair<int, int>& lhs, const pair<int, int>& rhs) {
        return lhs.second > rhs.second;
    }

    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> um;
        for (int x: nums) ++um[x];

        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(&cmp)> pq(cmp);

        for (auto &[num, cnt]: um) {
            if (pq.size() == k) {
                if (pq.top().second < cnt) {
                    pq.pop();
                    pq.emplace(num, cnt);
                }
            } else {
                pq.emplace(num, cnt);
            }
        }

        vector<int> ans;
        while (k--) {
            ans.push_back(pq.top().first);
            pq.pop();
        }
        return ans;
    }
};
```



```cpp
// cpp
// 快速排序

class Solution {
public:

    void quick_n_max(vector<pair<int, int>>& v, int left, int right, int k) {
        while (left <= right) {
            int t = rand() % (right - left + 1) + left;
            swap(v[right], v[t]);
            int last = left - 1;
            for (int i = left; i < right; ++i) {
                if (v[i].second > v[right].second) {
                    swap(v[++last], v[i]);
                }
            }
            swap(v[++last], v[right]);
            int cnt = last - left + 1;
            if (cnt == k) return;
            if (cnt < k) {
                left = last + 1;
                k -= cnt;
            } else {
                right = last - 1;
            }
        }
    }

    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> um;
        for (int x: nums) ++um[x];

        vector<pair<int, int>> v(um.begin(), um.end());
        quick_n_max(v, 0, v.size() - 1, k);
        vector<int> ans;
        for (int i = 0; i < k; ++i) ans.push_back(v[i].first);

        return ans;
    }
};
```



```cpp
// cpp
// 堆


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

    static bool cmp(const pair<int, int>& lhs, const pair<int, int>& rhs) {
        return lhs.second > rhs.second;
    }

    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> um;
        for (int x: nums) ++um[x];

        vector<pair<int, int>> v;
        vector<int> ans;
        for (auto &p: um) {
            if (v.size() == k) {
                if (p.second > v.front().second) {
                    v.front() = p;
                    heap_filter(v, 0, v.size() - 1, 0, cmp);
                }
            } else {
                v.emplace_back(p);
                heap_push(v, 0, v.size() - 1, cmp);
            }
        }
        for (auto &p: v) ans.push_back(p.first);

        return ans;
    }
};
```

