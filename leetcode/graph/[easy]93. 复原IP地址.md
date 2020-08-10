#### [[easy]93. 复原IP地址](https://leetcode-cn.com/problems/restore-ip-addresses/)

> 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
>
> 有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 `'.' `分隔。
>
> **示例:**
>
> ```shell
> 输入: "25525511135"
> 输出: ["255.255.11.135", "255.255.111.35"]
> ```



```cpp
// cpp
// dfs

class Solution {
private:
    static constexpr int SEG_COUNT = 4;

private:
    vector<string> ips;
    vector<int> segments;

public:

    void dfs(string& s, int segId, int segStart) {
        if (segId == SEG_COUNT) {
            if (segStart == s.size()) {
                string ip(to_string(segments[0]));
                for (int i = 1; i < SEG_COUNT; ++i) {
                    ip += "." + to_string(segments[i]);
                }
                ips.push_back(move(ip));
            }
            return;
        }
        if (segStart == s.size()) return;

        if (s[segStart] == '0') {
            segments[segId] = 0;
            dfs(s, segId + 1, segStart + 1);
            return;
        }

        int num = 0;
        for (int i = segStart; i < s.size(); ++i) {
            num = num * 10 + s[i] - '0';
            if (num <= 0xFF) {
                segments[segId] = num;
                dfs(s, segId + 1, i + 1);
            } else {
                return;
            }
        }
    }
    
    vector<string> restoreIpAddresses(string s) {
        segments.resize(SEG_COUNT);
        dfs(s, 0, 0);
        return ips;
    }
};
```

