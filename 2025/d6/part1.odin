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

	table := [dynamic][dynamic]string{}

	for line in strings.split_lines_iterator(&lines) {
		row := [dynamic]string{}
		for op in strings.fields(line) {
			append(&row, op)
		}

		append(&table, row)
	}

	total := 0
	for col := 0; col < len(table[0]); col += 1 {
		col_result := 0 if table[len(table) - 1][col] == "+" else 1
		for row := 0; row < len(table) - 1; row += 1 {
			number, _ := strconv.parse_int(table[row][col])
			if table[len(table) - 1][col] == "+" {
				col_result += number
			} else {
				col_result *= number
			}
		}

		total += col_result
	}

	fmt.println(total)
}
