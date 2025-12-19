package main

import "core:fmt"
import "core:math"
import "core:os"
import "core:sort"
import "core:strconv"
import "core:strings"

main :: proc() {
	data, ok := os.read_entire_file_from_filename_or_err("input.txt")
	if ok != nil {
		os.exit(1)
	}

	defer delete(data, context.allocator)

	input := string(data)
	intervals_and_queries, err := strings.split_n(input, "\n\n", 2)

	Interval :: struct {
		from: int,
		to:   int,
	}

	// intervals
	intervals := [dynamic]Interval{}
	for interval in strings.split_lines_iterator(&intervals_and_queries[0]) {
		from_and_to, err := strings.split_n(interval, "-", 2)
		from, _ := strconv.parse_int(from_and_to[0])
		to, _ := strconv.parse_int(from_and_to[1])
		append(&intervals, Interval{from, to})
	}

	sort.quick_sort_proc(intervals[:], proc(a: Interval, b: Interval) -> int {
		if (a.from < b.from) {return -1} else if (a.from > b.from) {return 1} else {return 0}
	})

	for interval in intervals {
		fmt.print(interval.from)
		fmt.print("-")
		fmt.println(interval.to)
	}

	total_fresh_ingredients := 0
	current_interval := intervals[0]
	for interval in intervals[1:] {
		fmt.print("Processing interval ")
		fmt.print(interval.from)
		fmt.print("-")
		fmt.println(interval.to)

		if current_interval.to < interval.from || interval == intervals[len(intervals) - 1] {
			if interval == intervals[len(intervals) - 1] {
				current_interval.to = math.max(interval.to, current_interval.to)
			}

			fmt.print("Adding interval: ")
			fmt.print(current_interval.from)
			fmt.print("-")
			fmt.println(current_interval.to)
			total_fresh_ingredients += current_interval.to - current_interval.from + 1
			current_interval = interval
		} else {
			current_interval.to = math.max(interval.to, current_interval.to)
		}
	}

	fmt.println(total_fresh_ingredients)
}
