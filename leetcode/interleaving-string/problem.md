## Interleaving String

<div id="problem_statement">

Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an interleaving of `s1` and `s2`.

An interleaving of two strings `s` and `t` is a configuration where they are divided into non-empty substrings such that:

```
s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
```

The interleaving is `s1 + t1 + s2 + t2 + s3 + t3 + ...` or `t1 + s1 + t2 + s2 + t3 + s3 + ...`

Note: `a + b` is the concatenation of strings `a` and `b`.
</div>

#### Example:

**Input**: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
**Output**: true

**Input**: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
**Output**: false