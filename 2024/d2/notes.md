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


## Part 1

Output: number of safe reports

Idea for solution:

- read lines
- parse each report (used type aliasing via `Report :: [dynamic]int`)
- filter safe reports
- return number of remaining reports

to check if a report is safe, we go through its levels and check:

- if it's smaller than the next one, we already know the report is not decreasing
- if it is greater than the next one, we know it is not increasing
- if the difference between the level and the next one is either 0 or greater than 3 then it does not have the proper gaps

Then a safe report is either increasing or decreasing **AND** it has to have the proper gaps.

## Part 2

Now a safe report can be safe if:

- it's already safe
- by removing one of its elements it is safe

Not caring too much about efficiency and because I did a first implementation and deleted everything by mistake and it was already 1AM and the next day had to wake up early to work (don't laugh, you never know if that's not gonna happen to you) I tried to reuse everything I already had in place. `is_safe` already received a `Report` so I'll keep it like that. Instead, when filtering safe reports I check:

- whether the report is already safe
- whether removing an element at a time results in a safe report 

odin has slices so it was quite easy to do this by using `report[:i]` and `report[i+1:]` to construct a new `Report`. It also supports appending slices to a dynamic array so no changes in types were needed, though a solution only using slices would probably be more efficient.

## Part 3(?)

Ok, ok. I got curious if using slices would make a difference. I copied the same code with the exception of `is_safe` receving a slice instead of a dynamic array (sorry `Report`, you're now a useless type alias). And did a few measurements using [hyperfine](https://github.com/sharkdp/hyperfine):

```bash
hyperfine --warmup 3 './p2'
Benchmark 1: ./p2
  Time (mean ± σ):       6.2 ms ±   1.4 ms    [User: 4.3 ms, System: 1.9 ms]
  Range (min … max):     2.7 ms …  12.2 ms    670 runs

hyperfine --warmup 3 './p3'
Benchmark 1: ./p3
  Time (mean ± σ):       5.1 ms ±   1.2 ms    [User: 4.1 ms, System: 1.1 ms]
  Range (min … max):     2.0 ms …   7.5 ms    407 runs
```

Nice, it got a tiny bit faster! That being said, hyperfine shows us this warning:

```bash
  Warning: Command took less than 5 ms to complete. Note that the results might be inaccurate because hyperfine can not calibrate the shell startup time much more precise than this limit. You can try to use the `-N`/`--shell=none` option to disable the shell completely.
```

So we have to take this with a pinch of salt. But the results are somewhat expected since we are keeping one version of each Report instead of a different one for each element.
