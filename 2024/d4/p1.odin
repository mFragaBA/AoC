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

Pos :: struct {
	x : int,
	y : int,
}

// returns all X positions
process_lines :: proc(lines: [dynamic]string) -> [dynamic]Pos {
	x_positions : [dynamic]Pos
	for i in 0..<len(lines) {
		for j in 0..<len(lines[i]) {
			if lines[i][j] == 'X' {
				append(&x_positions, Pos{ i, j })
			}
		}
	}

	return x_positions
}

in_bounds :: proc(board: [dynamic]string, pos: Pos) -> bool {
	return pos.x >= 0 && pos.x < len(board) && pos.y >= 0 && pos.y < len(board[pos.x])
}

// already know at x_position there is an X
count_xmas_through :: proc(board: [dynamic]string, x_position: Pos, x_offset: int, y_offset: int) -> int {
	next_pos := Pos{ x_position.x + x_offset, x_position.y + y_offset}
	if !in_bounds(board, next_pos) {
		return 0
	}

	if board[next_pos.x][next_pos.y] != 'M' {
		return 0
	}

	next_pos.x += x_offset
	next_pos.y += y_offset
	if !in_bounds(board, next_pos) {
		return 0
	}

	if board[next_pos.x][next_pos.y] != 'A' {
		return 0
	}

	next_pos.x += x_offset
	next_pos.y += y_offset
	if !in_bounds(board, next_pos) {
		return 0
	}

	if board[next_pos.x][next_pos.y] != 'S' {
		return 0
	}

	return 1
}

count_xmas :: proc(board: [dynamic]string, x_position: Pos) -> int {
	return count_xmas_through(board, x_position, -1, -1) +
		count_xmas_through(board, x_position, -1, 0) +
		count_xmas_through(board, x_position, -1, 1) +
		count_xmas_through(board, x_position, 0, -1) +
		count_xmas_through(board, x_position, 0, 1) +
		count_xmas_through(board, x_position, 1, -1) +
		count_xmas_through(board, x_position, 1, 0) +
		count_xmas_through(board, x_position, 1, 1)
}

main :: proc() {
	lines : [dynamic]string = read_file_by_lines_in_whole("input.txt")
	x_positions := process_lines(lines)

	xmas_positions : [dynamic]Pos
	total_xmas : int = 0

	for x_position in x_positions {
		xmas_count := count_xmas(lines, x_position)
		if xmas_count > 0 {
			append(&xmas_positions, x_position)
		}

		total_xmas += xmas_count
	}

	fmt.println(xmas_positions)
	fmt.println(total_xmas)
}
