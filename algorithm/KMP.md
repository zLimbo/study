#### KMP

状态转移+dp

```cpp
// cpp
// 字符串匹配
// kmp

class KMP {
private:
    vector<vector<int>> dp;
public:
    KMP(const string& pat):
        dp(vector<vector<int>>(pat.size(), vector<int>(256, 0)))
    {
        dp[0][pat[0]] = 1;
        int x = 0;
        for (int i = 1; i < pat.size(); ++i) {
            for (int c = 0; c < 256; ++c) {
                dp[i][c] = dp[x][c];
            }
            dp[i][pat[i]] = i + 1;
            x = dp[x][pat[i]];
        }
    }

    int search(const string& txt) {
        int s = 0;
        for (int i = 0; i < txt.size(); ++i) {
            s = dp[s][txt[i]];
            if (s == dp.size()) {
                return i - dp.size() + 1;
            }
        }
        return -1;
    }
};
```

一维数组

```cpp
// cpp
// 字符串匹配
// kmp

class KMP {
private:
    string pat;
    vector<int> next;
public:
    KMP(const string& pat):
        pat(pat),
        next(pat.size())
    {
        int i = 0, j = -1;
        next[0] = -1;
        while (i != pat.size()-1)
            if (j == -1 || pat[i] == pat[j]) next[++i] = ++j;
            else j = next[j];
    }

    int search(const string& txt) {
        int i = 0, j = 0;
        while (i != txt.size() && j != pat.size())
            if (j == -1 || txt[i] == pat[j]) { ++i; ++j; }
            else j = next[j];
        return j == pat.size() ? i - j : -1;
    }
};
```

