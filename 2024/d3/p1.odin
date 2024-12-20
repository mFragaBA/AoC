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

Mul :: struct {
	x: int,
	y: int,
}

read_mul :: proc(program: string, start: int) -> (Maybe(Mul), int) {
	if start > len(program) - 4 {
		return nil, -1
	}

	if program[start] != 'm' || program[start+1] != 'u' || program[start+2] != 'l' || program[start+3] != '(' {
		return nil, -1
	}


	number_start : int = start + 4
	current_idx : int = number_start
	for current_idx < len(program) {
		if program[current_idx] == ',' {
			break
		}

		current_idx += 1
	}

	if current_idx >= len(program) {
		return nil, -1
	}

	first_num, ok := strconv.parse_int(program[number_start:current_idx])
	if !ok {
		return nil, -1
	}

	number_start = current_idx + 1
	current_idx = number_start
	for current_idx < len(program) {
		if program[current_idx] == ')' {
			break
		}

		current_idx += 1
	}

	if current_idx >= len(program) {
		return nil, -1
	}

	second_num, second_ok := strconv.parse_int(program[number_start:current_idx])
	if !second_ok {
		return nil, -1
	}

	mul : Mul = Mul{first_num, second_num}

	return mul, current_idx
}

process_lines :: proc(lines: [dynamic]string) -> [dynamic]Mul {
	muls : [dynamic]Mul
	for line in lines {
		i : int = 0

		for i < len(line) {
			maybe_mul, end := read_mul(line, i)
			
			mul, ok := maybe_mul.?

			if ok {
				append(&muls, mul)
				i = end + 1
			} else {
				i += 1
			}
		}
	}

	return muls
}

main :: proc() {
	lines : [dynamic]string = read_file_by_lines_in_whole("input.txt")
	muls := process_lines(lines)

	fmt.println(muls)

	final_result : int = 0
	for mul in muls {
		final_result += mul.x * mul.y
	}

	fmt.println(final_result)
}
