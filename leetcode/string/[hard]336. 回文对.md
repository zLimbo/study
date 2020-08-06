#### [[hard]336. 回文对](https://leetcode-cn.com/problems/palindrome-pairs/)

> 给定一组**唯一**的单词， 找出所有***不同\*** 的索引对`(i, j)`，使得列表中的两个单词， `words[i] + words[j]` ，可拼接成回文串。
>
> ```shell
> 示例 1:
> 
> 输入: ["abcd","dcba","lls","s","sssll"]
> 输出: [[0,1],[1,0],[3,2],[2,4]] 
> 解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
> 示例 2:
> 
> 输入: ["bat","tab","cat"]
> 输出: [[0,1],[1,0]] 
> 解释: 可拼接成的回文串为 ["battab","tabbat"]
> ```
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/palindrome-pairs
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// 枚举前缀+枚举后缀 + TrieTree

class Solution {
public:
    struct Node {
        int ch[26];
        int flag;

        Node() {
            flag = -1;
            memset(ch, 0, sizeof(ch));
        }
    };

    vector<Node> trie;

    void insert(string& s, int flag) {
        int cur = 0;
        for (int i = s.size() - 1; i >= 0; --i) {
            int x = s[i] - 'a';
            if (!trie[cur].ch[x]) {
                trie.emplace_back();
                trie[cur].ch[x] = trie.size( ) - 1;
            }
            cur = trie[cur].ch[x];
        }
        trie[cur].flag = flag;
    }

    int find(string& s, int low, int high) {
        int cur = 0;
        for ( ; low <= high; ++low) {
            int x = s[low] - 'a';
            cur = trie[cur].ch[x];
            if (!cur) return -1;
        }
        return trie[cur].flag;
    }

    bool isPalindrome(string& s, int low, int high) {
        while (low < high) {
            if (s[low] != s[high]) return false;
            ++low; --high;
        }
        return true;
    }

    vector<vector<int>> palindromePairs(vector<string>& words) {
        int n = words.size();
        trie.emplace_back();
        for (int i = 0; i < n; ++i) {
            insert(words[i], i);
        }

        vector<vector<int>> ans;

        for (int flag = 0; flag < n; ++flag) {
            string& s = words[flag];
            int m = s.size();
            for (int i = 0; i <= m; ++i) {
                if (isPalindrome(s, i, m - 1)) {
                    int right_flag = find(s, 0, i - 1);
                    if (right_flag != -1 && right_flag != flag) {
                        ans.push_back({flag, right_flag});
                    }
                }
                if (i && isPalindrome(s, 0, i - 1)) {
                    int left_flag = find(s, i, m - 1);
                    if (left_flag != -1 && left_flag != flag) {
                        ans.push_back({left_flag, flag});
                    }
                }
            }
        }
        return ans;
    }
};
```



```python
# python3
# 枚举前缀+枚举后缀 + TrieTree

class Trie:
    def __init__(self):
        self.ch = [None] * 26
        self.flag = -1

    def insert(self, s, flag):
        cur = self
        for c in s:
            x = ord(c) - 97
            if not cur.ch[x]:
                cur.ch[x] = Trie()
            cur = cur.ch[x]
        cur.flag = flag

    def find(self, s, low, high):
        cur = self
        while high >= low:
            x = ord(s[high]) - 97
            if not cur.ch[x]:
                return -1
            cur = cur.ch[x]
            high -= 1
        return cur.flag

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        def isPalindrome(s, low, high):
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True
        
        trie = Trie()
        n = len(words)
        for flag, word in enumerate(words):
            trie.insert(word, flag)
        
        ans = []
        for flag, word in enumerate(words):
            m = len(word)
            for i in range(m+1):
                if isPalindrome(word, i, m-1):
                    right_flag = trie.find(word, 0, i-1)
                    if right_flag != -1 and right_flag != flag:
                        ans.append([flag, right_flag])
                if i and isPalindrome(word, 0, i-1):
                    left_flag = trie.find(word, i, m-1)
                    if left_flag != -1 and left_flag != flag:
                        ans.append([left_flag, flag])
        return ans
```



```python
# python3
# 枚举前缀+枚举后缀 + hash

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        def isPalindrome(s, low, high):
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True
        
        ans = []
        dic = { word[::-1]: flag for flag, word in enumerate(words) }
        for flag, word in enumerate(words):
            m = len(word)
            for i in range(m + 1):
                if isPalindrome(word, i, m-1):
                    right_flag = dic.get(word[:i])
                    if right_flag != None and right_flag != flag:
                        ans.append([flag, right_flag])
                if i and isPalindrome(word, 0, i-1):
                    left_flag = dic.get(word[i:])
                    if left_flag != None and left_flag != flag:
                        ans.append([left_flag, flag])
        return ans
```



```cpp
// cpp
// 枚举前缀+枚举后缀 + hash

class Solution {
public:
    unordered_map<string, int> mp;

    inline bool isPalindrome(string& s, int low, int high) {
        while (low < high)
            if (s[low++] != s[high--]) return false;
        return true;
    }

    inline int find(string& s, int low, int high) {
        auto it = mp.find(s.substr(low, high - low));
        return it == mp.end() ? -1 : it->second;
    }

    vector<vector<int>> palindromePairs(vector<string>& words) {
        
        int n = words.size();
        for (int i = 0; i < n; ++i) {
            string word = words[i];
            reverse(word.begin(), word.end());
            mp.emplace(word, i);
        }

        vector<vector<int>> ans;
        for (int flag = 0; flag < n; ++flag) {
            string& word = words[flag];
            int m = word.size();
            for (int i = 0; i <= m; ++i) {
                if (isPalindrome(word, i, m-1)) {
                    int right_flag = find(word, 0, i);
                    if (right_flag != -1 && right_flag != flag) {
                        ans.push_back({flag, right_flag});
                    }
                }
                if (i && isPalindrome(word, 0, i - 1)) {
                    int left_flag = find(word, i, m);
                    if (left_flag != -1 && left_flag != flag) {
                        ans.push_back({left_flag, flag});
                    }
                }
            }
        }
        return ans;
    }
};
```



```cpp
// cpp
// 枚举前缀+枚举后缀 + hash + string_view

class Solution {
public:
    unordered_map<string_view, int> mp;
    vector<string> wordsRev;

    inline bool isPalindrome(const string_view& sv, int low, int high) {
        while (low < high)
            if (sv[low++] != sv[high--]) return false;
        return true;
    }

    inline int find(const string_view& sv, int low, int high) {
        auto it = mp.find(sv.substr(low, high - low));
        return it == mp.end() ? -1 : it->second;
    }

    vector<vector<int>> palindromePairs(vector<string>& words) {
        
        int n = words.size();
        for (const string& word: words) {
            wordsRev.push_back(word);
            reverse(wordsRev.back().begin(), wordsRev.back().end());
        }
        for (int i = 0; i < n; ++i) {
            mp.emplace(wordsRev[i], i);
        }

        vector<vector<int>> ans;
        for (int flag = 0; flag < n; ++flag) {
            string_view sv(words[flag]);
            int m = sv.size();
            for (int i = 0; i <= m; ++i) {
                if (isPalindrome(sv, i, m-1)) {
                    int right_flag = find(sv, 0, i);
                    if (right_flag != -1 && right_flag != flag) {
                        ans.push_back({flag, right_flag});
                    }
                }
                if (i && isPalindrome(sv, 0, i - 1)) {
                    int left_flag = find(sv, i, m);
                    if (left_flag != -1 && left_flag != flag) {
                        ans.push_back({left_flag, flag});
                    }
                }
            }
        }
        return ans;
    }
};
```

