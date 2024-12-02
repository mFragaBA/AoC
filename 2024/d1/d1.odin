package main

import "core:fmt"

import "core:os"
import "core:strings"
import "core:strconv"
import "core:math"
import "core:slice"

read_file_by_lines_in_whole :: proc(filepath: string) -> [dynamic]string {
	data, ok := os.read_entire_file(filepath, context.allocator)
	if !ok {
		// could not read file
		return {}
	}
	defer delete(data, context.allocator)

	res : [dynamic]string = nil
	it := string(data)
	for line in strings.split_lines_iterator(&it) {
		// process line
		stable_line := strings.clone(strings.trim(line, " \t\n\r\v\f"))
		append(&res, stable_line)
	}

	return res
}


process_lines :: proc(lines: [dynamic]string) -> ([dynamic]int, [dynamic]int) {
	first_list : [dynamic]int
	second_list : [dynamic]int
	for line in lines {
		// process line
		numbers := strings.fields(line)

		first_number_int := strconv.atoi(numbers[0])
		second_number_int := strconv.atoi(numbers[1])

		append(&first_list, first_number_int)
		append(&second_list, second_number_int)
	}

	return first_list, second_list
}

main :: proc() {
	lines : [dynamic]string = read_file_by_lines_in_whole("input.txt")
	first_list, second_list := process_lines(lines)

	slice.sort(first_list[:])
	slice.sort(second_list[:])

	total_diff : int = 0

	for i in 0..<len(first_list) {
		total_diff += math.abs(first_list[i] - second_list[i])
	}

	fmt.println(total_diff)
}
