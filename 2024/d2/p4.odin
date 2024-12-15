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

Report :: [dynamic]int

process_lines :: proc(lines: [dynamic]string) -> [dynamic]Report {
	reports : [dynamic]Report
	for line in lines {
		// process report
		report : Report
		levels := strings.fields(line)

		for level in levels {
			level_int := strconv.atoi(level)
			append(&report, level_int)
		}

		append(&reports, report)
	}

	return reports
}

// L = Left array (increasing to the left, decreasing to the left)
// R = Right array (decreasing to the right, increasing to the right)
is_safe_after_removing_ith :: proc(report: Report, L: [dynamic]int, R: [dynamic]int, i: int, increasing : bool) -> bool {
	// We use i == -1 as in no removal
	if i == -1 {
		return R[0] == len(report) - 1
	}

	if i == 0 {
		return R[i + 1] == len(report) - 2
	}

	if i == len(report) - 1 {
		return L[i - 1] == len(report) - 2
	}

	diff : int = abs(report[i-1] - report[i+1])
	still_sorted : bool = L[i-1] == i-1 && 
				R[i+1] == (len(report) - 1 - (i + 1)) && 
				(increasing ? report[i-1] < report[i+1] : report[i-1] > report[i+1])
	proper_diff : bool = diff > 0 && diff < 4

	return still_sorted && proper_diff
}

filter_safe_reports :: proc(reports : [dynamic]Report) -> [dynamic]Report {
	safe_reports : [dynamic]Report

	for report in reports {
		// Decreasing to the left, increasing to the right (with the proper diff)
		D : [dynamic]int = make([dynamic]int, len(report), len(report))
		I : [dynamic]int = make([dynamic]int, len(report), len(report))

		// Increasing to the left, decreasing to the right (with the proper diff)
		I2 : [dynamic]int = make([dynamic]int, len(report), len(report))
		D2 : [dynamic]int = make([dynamic]int, len(report), len(report))

		// Initialize arrays
		D[0] = 0
		I[len(report)-1] = 0;

		I2[0] = 0;
		D2[len(report)-1] = 0

		for i in 1..<len(report) {
			if report[i] > report[i-1] {
				D[i] = D[i-1] + 1
				I2[i] = 0
			} else {
				D[i] = 0
				I2[i] = I2[i-1] + 1
			}

			diff : int = abs(report[i-1] - report[i])
			proper_diff : bool = diff > 0 && diff < 4
			if (!proper_diff) {
				D[i] = 0
				I2[i] = 0
			}
			
		}

		for i := len(report) - 2; i >= 0; i -= 1 {
			if report[i+1] > report[i] {
				I[i] = I[i+1] + 1
				D2[i] = 0
			} else {
				I[i] = 0
				D2[i] = D2[i+1] + 1
			}

			diff : int = abs(report[i] - report[i+1])
			proper_diff : bool = diff > 0 && diff < 4
			if (!proper_diff) {
				I[i] = 0
				D2[i] = 0
			}
		}

		// Do check
		any_safe : bool = false
		for i in -1..<len(report) {
			if is_safe_after_removing_ith(report, D, I, i, true) || is_safe_after_removing_ith(report, I2, D2, i, false) {
				any_safe = true
			}
		}

		if any_safe {
			append(&safe_reports, report)
		}
	}

	return safe_reports
}

main :: proc() {
	lines : [dynamic]string = read_file_by_lines_in_whole("input.txt")
	reports := process_lines(lines)
	safe_reports := filter_safe_reports(reports)

	fmt.println(len(safe_reports))
}
