#### [[medium]5545. 无矛盾的最佳球队](https://leetcode-cn.com/problems/best-team-with-no-conflicts/)

> ![image-20201018140040726](C:\Users\z\AppData\Roaming\Typora\typora-user-images\image-20201018140040726.png)
>
> ![image-20201018140054872](C:\Users\z\AppData\Roaming\Typora\typora-user-images\image-20201018140054872.png)

```cpp
// cpp
// dp

class Solution {
public:
    int bestTeamScore(vector<int>& scores, vector<int>& ages) {
        int n = ages.size();
        vector<vector<int>> v;
        for (int i = 0; i < n; ++i) {
            v.push_back({ages[i], scores[i]});
        }
        sort(v.begin(), v.end());
        vector<int> dp(n, 0);
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            //cout << v[i][0] << " " << v[i][1] << endl;
            for (int j = i - 1; j >= 0; --j) {
                if (v[j][1] <= v[i][1]) {
                    dp[i] = max(dp[i], dp[j]);
                }
            }
            dp[i] += v[i][1];
            ans = max(ans, dp[i]);
        }
        return ans;
    }
};
```

