# Day 1 notes

The problem statement can be reduced as: you input is a file with the following format:

```
x1   y1
x2   y2
x3   y3
x4   y4
x5   y5
...
```

(Note: there are **3 spaces** in between numbers)

The idea is to read that file, and consider lists `X = [x1, x2, ...]` and `Y = [y1, y2, ...]`. For the first part of the problem we want to find the result of adding up all the differences:

```math
\sum_{i=1}^n |x_i' - y_i'|
```

where $x_i'$ and $y_i'$ belong to the sorted lists `X' = sorted(X)` and `Y' = sorted(Y)` 

The problem itself is quite simple and can be divided in steps:

- read input file
- parse each line to build `X` and `Y`
- sort `X` and `Y`
- iterate over every position and calculate the corresponding difference adding up all of them

As for the second part of day one, you are supposed to calculate for each number in `X`, the amount of occurrences of that number in `Y` and sum up the number multiplied by the amount of occurrences. Any data structure that supports counting can be used for this, I resorted to the good ol dictionary (called `map` in Odin).

## Some notes on odin

Now, regarding odin... I wouldn't necessarily call it a language that you can hop on for the first time and be productive really. At least to me the sintax felt a bit alien. **BUT**, they have a great [documentation page to get started](https://odin-lang.org/docs/overview/), I barely had to look elsewhere for the answers I needed.

I don't want to go into every line, but one thing that caused me a bit of a headache was memory management. Odin has [no automatic memory management](https://odin-lang.org/docs/overview/#making-and-deleting-slices-and-dynamic-arrays) so you need to be careful about freeing memory once you have used it.

There was a problem I was having related to memory. I was getting a wrong answer compared to the example. And added some prints and noticed that I was reading the array properly but at some point it would get filled with junk:

```
LINES BEFORE ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]
LINES AFTER ["\xc4\xcf\x14\xfe\xb2", "\xde\x19  3", "2   5", "1   3", "3   9", "3   3"]
```

So, if you take a look at the code, the function `read_file_by_lines_in_whole` there is a `defer delete` call. `defer` delays the execution of the code until it goes out of scope. I was also using `trim` and my brain thought it would return a new copy of the trimmed string, should've read the documentation:

> res: The trimmed string as a slice of the original

and before I only had:

```
trimmed_line := strings.trim(line, " \t\n\r\v\f")
```

Thus, the array of lines I was returning contained slices with references of the read data, but that memory got freed after returning from the function call. The solution thankfully was to clone the string:

```
stable_line := strings.clone(strings.trim(line, " \t\n\r\v\f"))
```

# References

- [Odin By Example](https://gingerbill.gitbooks.io/odin-by-example/content/)
- [Odin Overview](https://odin-lang.org/docs/overview/)
