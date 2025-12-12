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

	lines := string(data)
	position := 50
	amount_of_times_at_zero := 0
	fmt.println(position)
	for line in strings.split_lines_iterator(&lines) {
		rotation, distance, ok := line[0:1], strconv.parse_int((line[1:]))

		if rotation == "R" {
			position = (position + distance) % 100
		} else {
			position = (position + 100 - distance) % 100
		}

		if position == 0 {
			amount_of_times_at_zero += 1
		}

		fmt.println(position)
	}

	fmt.println(amount_of_times_at_zero)
}
