package main

import "core:fmt"
import "core:os"
import "core:slice"
import "core:strconv"
import "core:strings"

// Finds last column of an operation
find_operation_end :: proc(operand_row: string, start_from: int) -> int {
	for j := start_from + 1; j < len(operand_row); j += 1 {
		if operand_row[j] == '+' || operand_row[j] == '*' {
			return j - 2
		}
	}

	return len(operand_row) - 1
}

pad_with_empty_spaces :: proc(string_to_pad: string, size_to_pad_into: int) -> string {
	builder := strings.builder_make()
	strings.write_string(&builder, string_to_pad)
	for strings.builder_len(builder) < size_to_pad_into {
		strings.write_rune(&builder, ' ')
	}
	return strings.to_string(builder)
}

main :: proc() {
	data, ok := os.read_entire_file_from_filename_or_err("input.txt")
	if ok != nil {
		os.exit(1)
	}

	defer delete(data, context.allocator)

	lines := string(data)

	table := [dynamic]string{}

	for line in strings.split_lines_iterator(&lines) {
		append(&table, line)
	}

	digits := table[:len(table) - 1]
	operations := table[len(table) - 1]

	longest_row := len(digits[0])
	for row in digits {
		longest_row = max(longest_row, len(row))
	}

	// pad all rows with empty spaces (My text editor likes trimming extra spaces at the end of lines)
	for i := 0; i < len(digits); i += 1 {
		digits[i] = pad_with_empty_spaces(digits[i], longest_row)
	}

	// pad operations with empty spaces
	operations = pad_with_empty_spaces(operations, longest_row)

	total := 0
	for col := 0; col < len(table[0]); col += 1 {
		if operations[col] == ' ' {continue}
		fmt.println("=========")
		operation_end := find_operation_end(operations, col)
		operation_result := 0 if operations[col] == '+' else 1

		for j := col; j <= operation_end; j += 1 {
			exponent := 1
			number := 0
			for row := len(digits) - 1; row >= 0; row -= 1 {
				if digits[row][j] == ' ' {continue}
				digit := digits[row][j] - '0'

				number += int(digit) * exponent
				exponent *= 10
			}

			fmt.println(number)

			if operations[col] == '+' {
				operation_result += number
			} else {
				operation_result *= number
			}
		}

		total += operation_result
	}

	fmt.println(total)
}
