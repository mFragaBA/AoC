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

> Slices are like references to arrays; they do not store any data, rather they describe a section, or slice, of underlying data.

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

## Part 4 (okay, let's not drag it THAT long)

If we look at the code we might be satisfied with the result, but as a CS major i've been taught to optimize no matter what (code simplicity, readability and mantainability what?). So not being satisfied enough, we want to make this bad boy fly.

Again, as a cs major I cannot stop thinking about computational complexity. I'm not gonna do a series on that, but [here's](https://medium.com/@DevChy/introduction-to-big-o-notation-time-and-space-complexity-f747ea5bca58) a link to an article that does that.

If we stare at our code (the one for part 2) for a while, we might get to the conclusion that the running time for the algorithm is $$\mathcal{O}(L * N^2)$$, with $$L$$ being the amount of lines and $$N$$ being the length of the longest report (or each line). We already have to parse the file so at least we'll have a $$\mathcal{O}(L * N)$$ running time complexity. We are going to find a solution that has that exact running complexity.

The $$L * N^2$$ appears because, for each line, we have to check each of the $$N$$ versions of the array that have an element removed (plus the one that has no removals) and for each of those check if it is sorted and has the proper spacing between elements (which adds the extra $$N$$).

Hence, we'll find a way to check all versions of the array in just $$\mathcal{O}(N)$$ instead. To simplify the explanation, let's just assume that a safe report is one that is only increasing. You can check the code afterwards for the full implementation considering the decreasing possibility and the proper gaps. We are going to build the following arrays:

- `D[i]` will contain the amount of levels before `R[i]`, the i-th report level that are consecutively **decreasing**. For example, if `R = [1, 2, 3, 2, 3]` you would have `D = [0, 1, 2, 0, 1]`. Note, that if `D[i] == i` then `D[0..i]` is increasing.
- `I[i]` which similarly will contain the amount of levels **after** `R[i]` that are consecutively **increasing**. Try thinking what would `I` look like for the previous example. Likewise, if `I[i] == N - 1 - i` (`N` being the amount of levels in the report) then that means that from that level and onwards, `R[i..]` is increasing. 

Each of those can be built with just a single iteration over the whole report:

```
R[0] = 0
I[N-1] = 0
D[i] = D[i-1] + 1 if R[i] > R[i-1], 0 otherwise
I[i] = I[i+1] + 1 if R[i] < R[i+1], 0 otherwise
```

Then, having those it is possible to answer whether the report is safe without considering the i-th level or not by doing:

```
# Note: we're not considering i == 0 nor i == N-1 here
is_safe_without_ith_level(R, D, I, i):
	return D[i-1] == i-1 && I[i+1] == (N - 1 - (i+1)) && R[i-1] < R[i+1]
```

And note that this is $$\mathcal{O}(1)$$! So it grants us the desired complexity.

### Benchmark time!

So, I re-ran the same benchmarks as before, but I noticed hyperfine provides this option:

```bash
You can try to use the `-N`/`--shell=none` option to disable the shell completely
```

This might give us a bit better results:

```bash
Benchmark 1: ./p2
  Time (mean ± σ):       4.9 ms ±   1.2 ms    [User: 3.6 ms, System: 1.1 ms]
  Range (min … max):     2.5 ms …   7.4 ms    481 runs

# Note: p3 usually had a first run with an outlier
hyperfine --warmup 3 './p3' -N
Benchmark 1: ./p3
  Time (mean ± σ):     666.5 µs ± 130.1 µs    [User: 260.3 µs, System: 251.8 µs]
  Range (min … max):   404.0 µs … 1329.7 µs    2521 runs


hyperfine --warmup 3 './p4' -N
Benchmark 1: ./p4
  Time (mean ± σ):       3.5 ms ±   0.9 ms    [User: 2.5 ms, System: 0.9 ms]
  Range (min … max):     1.8 ms …   5.4 ms    608 runs
```

wait WHAT?!?!?! I thought smaller complexity would lead to better running time! How foolish was I to believe such lies...

### A note on time complexity

Let's address one thing. Take a look at the input file for day 2. What can you see? Yes, look at each report. They are usually no longer than 8-10 levels. If you are familiar with $$/mathcal{O}$$ notation, you should know that **it hides the constant in the running time calculation**. It has some reasoning behind that. For bigger instances, the constant is usually not relevant. But for small instances as these ones, it does. 

So, making the final optimization **gave us a better theoretical complexity but at the expense of code complexity, readability, worse running time for the instances the problem has and mor**. This is usually a common mistake most devs make (myself included) and for which we have to resist the urge to optimize for theoritical complexity, or a solution that seems more "elegant", whatever way you wanna name it.
