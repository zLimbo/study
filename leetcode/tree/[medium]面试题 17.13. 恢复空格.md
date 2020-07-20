#### [[medium]面试题 17.13. 恢复空格](https://leetcode-cn.com/problems/re-space-lcci/)

> 哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。
>
> 注意：本题相对原题稍作改动，只需返回未识别的字符数
>
>  
>
> 示例：
>
> 输入：
> dictionary = ["looked","just","like","her","brother"]
> sentence = "jesslookedjustliketimherbrother"
> 输出： 7
> 解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
> 提示：
>
> 0 <= len(sentence) <= 1000
> dictionary中总字符数不超过 150000。
> 你可以认为dictionary和sentence中只包含小写字母。
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/re-space-lcci
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// string
// 字典树(Trie) + 动态规划

struct Trie {
    Trie* next[26] = { nullptr };
    bool isEnd = false;

    void insert(string& s) {
        Trie* cur = this;

        for (int i = s.length()-1; i >= 0; --i) {
            int c = s[i] - 'a';
            if (cur->next[c] == nullptr) {
                cur->next[c] = new Trie;
            }
            cur = cur->next[c];
        }
        cur->isEnd = true;
    }
};

class Solution {
public:

    int respace(vector<string>& dictionary, string sentence) {
        Trie* trie = new Trie;
        for (string& word: dictionary) {
            trie->insert(word);
        }
        int n = sentence.length();
        vector<int> dp(n+1);
        dp[0] = 0;
        for (int i = 1; i <= n; ++i) {
            dp[i] = dp[i-1] + 1;
            Trie* cur = trie;
            for (int j = i-1; j >= 0; --j) {
                int c = sentence[j] - 'a';
                if (cur->next[c] == nullptr) {
                    break;
                }
                cur = cur->next[c];
                if (cur->isEnd) {
                    dp[i] = min(dp[i], dp[j]);
                }
                if (dp[i] == 0) {
                    break;
                }
            }
        }
        return dp[n];
    }
};
```



```cpp
// cpp
// string
// 字符串哈希

class Solution {
public:
    using LL = long long;
    static constexpr LL P = (1LL << 31) - 1;
    static constexpr LL BASE = 41;

    LL getHash(const string& s) {
        LL hashValue = 0;
        for (int i = s.length()-1; i >= 0; --i) {
            hashValue = hashValue * BASE + s[i] - 'a' + 1;
            hashValue %= P;
        }
        return hashValue;
    }

    int respace(vector<string>& dictionary, string sentence) {
        unordered_set<LL> hd;
        int maxLen = 0;
        for (const string& word: dictionary) {
            hd.insert(getHash(word));
            if (word.length() > maxLen)  maxLen = word.length();
        }
        int n = sentence.length();
        vector<int> dp(n+1); 
        dp[0] = 0;
        
        for (int i = 1; i <= n; ++i) {
            dp[i] = dp[i-1] + 1;
            LL hashValue = 0;
            for (int j = i - 1; j >= 0 && i - j <= maxLen; --j) {
                hashValue = hashValue * BASE + sentence[j] - 'a' + 1;
                hashValue %= P;
                if (hd.find(hashValue) != hd.end()) {
                    dp[i] = min(dp[i], dp[j]);
                }
            }
        }

        return dp[n];
    }
};
```



```python
# python3
# string
# 字典树

class Trie:
    def __init__(self):
        self.next = [None for _ in range(26)]
        self.isEnd = False

    def insert(self, s):
        cur = self
        for c in reversed(s):
            o = ord(c) - ord('a')
            if not cur.next[o]:
                cur.next[o] = Trie()
            cur = cur.next[o]
        cur.isEnd = True

class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        n = len(sentence)
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i] = dp[i-1] + 1
            cur = trie
            for j in range(i-1, -1, -1):
                o = ord(sentence[j]) - ord('a')
                if not cur.next[o]:
                    break
                cur = cur.next[o]
                if cur.isEnd:
                    dp[i] = min(dp[i], dp[j])
                if (dp[i] == 0):
                    break
        return dp[n]
```



```python
# python3
# string
# dp

class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        if not dictionary:
            return len(sentence)
        dic = {*dictionary}
        n = len(sentence)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i):
                if sentence[j: i] in dic:
                    dp[i] = min(dp[i], dp[j])
        return dp[-1]
```

