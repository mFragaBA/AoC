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

is_safe :: proc(report: Report) -> bool {
	increasing : bool = true
	decreasing : bool = true
	has_proper_gaps : bool = true

	for i in 0..<(len(report)-1) {
		// check it's increasing or decreasing
		if report[i] < report[i+1] {
			decreasing = false
		}

		if report[i] > report[i+1] {
			increasing = false
		}

		// check difference between values
		diff : int = abs(report[i] - report[i+1])
		if diff < 1 || diff > 3 {
			has_proper_gaps = false
		}
	}

	return (increasing || decreasing) && has_proper_gaps
}

is_safe_two :: proc(report_one: []int, report_two: []int) -> bool {
	increasing : bool = true
	decreasing : bool = true
	has_proper_gaps : bool = true

	for i in 0..<(len(report_one)-1) {
		// check it's increasing or decreasing
		if report_one[i] < report_one[i+1] {
			decreasing = false
		}

		if report_one[i] > report_one[i+1] {
			increasing = false
		}

		// check difference between values
		diff : int = abs(report_one[i] - report_one[i+1])
		if diff < 1 || diff > 3 {
			has_proper_gaps = false
		}
	}

	for i in 0..<(len(report_two)-1) {
		// check it's increasing or decreasing
		if report_two[i] < report_two[i+1] {
			decreasing = false
		}

		if report_two[i] > report_two[i+1] {
			increasing = false
		}

		// check difference between values
		diff : int = abs(report_two[i] - report_two[i+1])
		if diff < 1 || diff > 3 {
			has_proper_gaps = false
		}
	}

	if len(report_one) > 0 && len(report_two) > 0 {
		// check it's increasing or decreasing
		if report_one[len(report_one)-1] < report_two[0] {
			decreasing = false
		}

		if report_one[len(report_one)-1] > report_two[0] {
			increasing = false
		}

		// check difference between values
		diff : int = abs(report_one[len(report_one)-1] - report_two[0])
		if diff < 1 || diff > 3 {
			has_proper_gaps = false
		}
	}

	return (increasing || decreasing) && has_proper_gaps
}

filter_safe_reports :: proc(reports : [dynamic]Report) -> [dynamic]Report {
	safe_reports : [dynamic]Report

	for report in reports {
		any_safe : bool = false
		for i in 0..<len(report) {
			report_without_elem : Report
			append(&report_without_elem, ..report[:i])
			append(&report_without_elem, ..report[i+1:])
			if is_safe(report_without_elem) {
				any_safe = true
			}
		}

		if any_safe || is_safe(report) {
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
