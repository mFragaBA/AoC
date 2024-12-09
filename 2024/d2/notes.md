# Day 2 notes

Input: `[Report]`

`Report`: space separated numbers called **levels**

Example:

```
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```

A report is said to be safe if:

- the levels are all increasing or all decreasing and
- any two adjacent levels differ by at least one and at most 3

In the example, 2 reports are safe (first and last)

Output: number of safe reports
