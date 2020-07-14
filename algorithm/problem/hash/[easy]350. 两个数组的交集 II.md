#### [[easy]350. 两个数组的交集 II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/)

> 给定两个数组，编写一个函数来计算它们的交集。
>
> 示例 1:
>
> 输入: nums1 = [1,2,2,1], nums2 = [2,2]
> 输出: [2,2]
> 示例 2:
>
> 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
> 输出: [4,9]
> 说明：
>
> 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
> 我们可以不考虑输出结果的顺序。
> 进阶:
>
> 如果给定的数组已经排好序呢？你将如何优化你的算法？
> 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
> 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```c
// c
// quick_sort

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

 void quickSort(int* A, int lo, int hi) {
    if (lo + 1 >= hi) return;
    int x = A[(lo + hi) >> 1];
    int L = lo, R = hi - 1;

    while (true) {
        while (A[L] < x) ++L;
        while (A[R] > x) --R;
        if (L < R) {
            int temp = A[L];
            A[L] = A[R];
            A[R] = temp;
            ++L;
            --R;
        }
        else break;
    }
    quickSort(A, lo, L);
    quickSort(A, L, hi);
}


int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize){
    quickSort(nums1, 0, nums1Size);
    quickSort(nums2, 0, nums2Size);
    int len = nums1Size < nums2Size ? nums1Size : nums2Size;
    int* ret = (int *)malloc(len * sizeof(int));
    int sz = 0;
    int i = 0, j = 0;
    while (i < nums1Size && j < nums2Size) {
        if (nums1[i] < nums2[j]) ++i;
        else if (nums1[i] > nums2[j]) ++j;
        else {
            ret[sz++] = nums1[i];
            ++i;
            ++j;
        }
    }
    *returnSize = sz;
    return ret;
}
```



```python
# python3
# hash

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 and not nums2:
            return []
        if (len(nums1) > len(nums2)):
            nums1, nums2 = nums2, nums1
        ret = []
        d = collections.Counter(nums1)
        for v in nums2:
            if d.get(v) and d[v] > 0:
                ret.append(v)
                d[v] -= 1
        return ret
```

