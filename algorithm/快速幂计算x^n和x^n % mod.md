#### 快速幂计算x^n和x^n % mod

```C++
// cpp
// 快速幂
long long quick_pow(long long x, long long n) {
    if (n == 0) return 1;
    long long ret = 1;
    while (n) {
        if (n & 1) ret *= x;
        x *= x;
        n >>= 1;
    }
    return ret;
}

// 快速幂+mod计算
long long quick_pow_mod(long long x, long long n, long long mod) {
    if (n == 0) return 1;
    long long ret = 1;
    while (n) {
        if (n & 1) ret = (ret * x) % mod;
        x = (x * x) % mod;
        n >>= 1;
    }
    return ret;
}
```