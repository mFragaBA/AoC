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

		started_at_zero := position == 0
		offset := 1 if rotation == "R" else -1

		for distance > 0 {
			position += offset
			distance -= 1

			position = (position + 100) % 100

			if position == 0 {
				amount_of_times_at_zero += 1
			}
		}

		fmt.println(position, amount_of_times_at_zero)
	}

	fmt.println(amount_of_times_at_zero)
}
