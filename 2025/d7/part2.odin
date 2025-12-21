package main

import "core:fmt"
import "core:os"
import "core:strings"

GridPos :: struct {
	row: int,
	col: int,
}

timelines_reaching :: proc(
	_timelines: ^map[GridPos]int,
	manifold: [dynamic]string,
	pos: GridPos,
) -> int {
	row := pos.row
	col := pos.col
	// invalid pos
	if col < 0 || col >= len(manifold[0]) {return 0}
	if row < 0 || row >= len(manifold) {return 0}

	if row == 0 {
		res := 1 if manifold[row][col] == 'S' else 0
		// fmt.printfln("timelines reaching GridPos{{ row: %i, col: %i }} = %i", row, col, res)
		return res
	}

	if pos in _timelines^ {
		// fmt.printfln(
		// 	"timelines reaching GridPos{{ row: %i, col: %i }} = %i",
		// 	row,
		// 	col,
		// 	_timelines^[pos],
		// )
		return _timelines^[pos]
	}

	timelines := 0

	// didn't come from a split (and doesn' t have one above)
	// ..|..
	// ..|..
	if manifold[row - 1][col] != '^' {
		timelines = timelines_reaching(_timelines, manifold, GridPos{row - 1, col})
	}

	// came from a right split
	// .|...
	// .^|..
	if col > 0 && manifold[row][col - 1] == '^' {
		timelines += timelines_reaching(_timelines, manifold, GridPos{row - 1, col - 1})
	}

	// came from a left split
	// ..|..
	// .|^..
	if col < len(manifold[0]) - 1 && manifold[row][col + 1] == '^' {
		timelines += timelines_reaching(_timelines, manifold, GridPos{row - 1, col + 1})
	}

	// fmt.printfln("timelines reaching GridPos{{ row: %i, col: %i }} = %i", row, col, timelines)

	_timelines^[pos] = timelines

	return timelines
}

main :: proc() {
	data, ok := os.read_entire_file_from_filename_or_err("input.txt")
	if ok != nil {
		os.exit(1)
	}

	defer delete(data, context.allocator)

	lines := string(data)
	manifold := [dynamic]string{}

	for line in strings.split_lines_iterator(&lines) {
		append(&manifold, line)
	}

	_timelines_reaching := make(map[GridPos]int)

	total_timelines := 0
	for end_pos := 0; end_pos < len(manifold[0]); end_pos += 1 {
		total_timelines += timelines_reaching(
			&_timelines_reaching,
			manifold,
			GridPos{len(manifold) - 1, end_pos},
		)
	}

	fmt.println(total_timelines)
}
