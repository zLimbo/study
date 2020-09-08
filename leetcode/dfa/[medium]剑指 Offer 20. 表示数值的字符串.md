#### [[medium]剑指 Offer 20. 表示数值的字符串](https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/)

> 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。



```cpp
// cpp
// dfa

enum State {
    STATE_INITIAL,
    STATE_INT_SIGN,
    STATE_INTEGER,
    STATE_POINT,
    STATE_POINT_WITHOUT_INT,
    STATE_FRACTION,
    STATE_EXP,
    STATE_EXP_SIGN,
    STATE_EXP_NUMBER,
    STATE_END,
};

enum CharType {
    CHAR_NUMBER,
    CHAR_EXP,
    CHAR_POINT,
    CHAR_SIGN,
    CHAR_SPACE,
    CHAR_ILLEGAL,
};

unordered_map<State, unordered_map<CharType, State>> transfer = {
    {
        STATE_INITIAL, {
            {CHAR_SPACE, STATE_INITIAL},
            {CHAR_NUMBER, STATE_INTEGER},
            {CHAR_POINT, STATE_POINT_WITHOUT_INT},
            {CHAR_SIGN, STATE_INT_SIGN},
        }
    }, {
        STATE_INT_SIGN, {
            {CHAR_NUMBER, STATE_INTEGER},
            {CHAR_POINT, STATE_POINT_WITHOUT_INT},
        }
    }, {
        STATE_INTEGER, {
            {CHAR_NUMBER, STATE_INTEGER},
            {CHAR_POINT, STATE_POINT},
            {CHAR_EXP, STATE_EXP},
            {CHAR_SPACE, STATE_END},
        }
    }, {
        STATE_POINT, {
            {CHAR_NUMBER, STATE_FRACTION},
            {CHAR_EXP, STATE_EXP},
            {CHAR_SPACE, STATE_END},
        }
    }, {
        STATE_POINT_WITHOUT_INT, {
            {CHAR_NUMBER, STATE_FRACTION},
        }
    }, {
        STATE_FRACTION, {
            {CHAR_NUMBER, STATE_FRACTION},
            {CHAR_EXP, STATE_EXP},
            {CHAR_SPACE, STATE_END},
        }
    }, {
        STATE_EXP, {
            {CHAR_SIGN, STATE_EXP_SIGN},
            {CHAR_NUMBER, STATE_EXP_NUMBER},
        }
    }, {
        STATE_EXP_SIGN, {
            {CHAR_NUMBER, STATE_EXP_NUMBER},
        }
    }, {
        STATE_EXP_NUMBER, {
            {CHAR_NUMBER, STATE_EXP_NUMBER},
            {CHAR_SPACE, STATE_END},
        }
    }, {
        STATE_END, {
            {CHAR_SPACE, STATE_END},
        }
    }
};

unordered_set<State> endState = {
    STATE_INTEGER,
    STATE_POINT,
    STATE_FRACTION,
    STATE_EXP_NUMBER,
    STATE_END
};

class Solution {
public:

    CharType toCharType(char ch) {
        if (ch >= '0' && ch <= '9') return CHAR_NUMBER;
        if (ch == 'e' || ch == 'E') return CHAR_EXP;
        if (ch == '.') return CHAR_POINT;
        if (ch == '+' || ch == '-') return CHAR_SIGN;
        if (ch == ' ') return CHAR_SPACE;
        return CHAR_ILLEGAL;
    }

    bool isNumber(string s) {
        State st = STATE_INITIAL;
        for (char c: s) {
            CharType ct = toCharType(c);
            if (transfer[st].find(ct) == transfer[st].end()) {
                return false;
            }
            st = transfer[st][ct];
        }
        return endState.find(st) != endState.end();
    }
};
```



```cpp
// cpp
//

class Solution {
public:

    bool judgeInteger(string& s, int left, int right) {
        if (left > right) return false;
        if (s[left] == '+' || s[left] == '-') ++left;
        if (left > right) return false;

        while (left <= right) {
            if (s[left] < '0' || s[left] > '9') {
                return false;
            }
            ++left;
        }
        return true;
    }


    bool judgeReal(string& s, int left, int right) {
        if (left > right) return false;
        if (s[left] == '+' || s[left] == '-') ++left;
        if (left > right) return false;

        int dotPos = -1;
        for (int i = left; i <= right; ++i) {
            if (s[i] == '.') {
                if (dotPos != -1) return false;
                dotPos = i;
            } else if (s[i] < '0' || s[i] > '9') return false;
        }
        return dotPos != left || dotPos != right;
    }

    bool isNumber(string s) {
        int left = 0, right = s.size() - 1;
        while (left <= right && s[left] == ' ') ++left;
        while (left <= right && s[right] == ' ') --right;
        if (left > right) return false;

        int ePos = -1;
        for (int i = left; i <= right; ++i) {
            if (s[i] == 'e' || s[i] == 'E') {
                ePos = i;
                break;
            }
        }

        if (ePos == -1) {
            if (!judgeReal(s, left, right)) {
                return false;
            }
        } else {
            if (!judgeReal(s, left, ePos - 1) || !judgeInteger(s, ePos + 1, right)) {
                return false;
            }
        }

        return true;
    }
};
```

