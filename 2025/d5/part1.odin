package main

import "core:fmt"
import "core:os"
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

	// queries
	total_fresh_ingredients := 0
	for query_str in strings.split_lines_iterator(&intervals_and_queries[1]) {
		query, _ := strconv.parse_int(query_str)
		for interval in intervals {
			if (interval.from <= query && query <= interval.to) {
				total_fresh_ingredients += 1
				break
			}
		}
	}

	fmt.println(total_fresh_ingredients)
}
