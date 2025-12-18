package main

import "core:fmt"
import "core:os"
import "core:strings"

char_to_int :: proc(c: u8) -> int {
	return int(c) - '0'
}

get_max_joltage :: proc(bank: string) -> int {
	selected_battery_joltages := [12]int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

	// since selected_battery_joltages is full, check if we can replace
	for battery_i := 0; battery_i < len(bank); battery_i += 1 {
		replaced_amount := 0
		for j := 11;
		    j >= 0 && char_to_int(bank[battery_i]) > selected_battery_joltages[j];
		    j -= 1 {
			if battery_i + replaced_amount >= len(bank) {
				break
			}
			selected_battery_joltages[j] = char_to_int(bank[battery_i])
			replaced_amount += 1

			if j < 11 {
				selected_battery_joltages[j + 1] = 0
			}
		}
	}

	total_joltage := 0
	exponent := 1
	for i := 0; i < 12; i += 1 {
		total_joltage += exponent * selected_battery_joltages[11 - i]
		exponent *= 10
	}

	return total_joltage
}

main :: proc() {
	data, ok := os.read_entire_file_from_filename_or_err("sample.txt")
	if ok != nil {
		os.exit(1)
	}

	defer delete(data, context.allocator)

	banks := string(data)
	output_joltage := 0
	for bank in strings.split_lines_iterator(&banks) {
		joltage := get_max_joltage(bank)
		output_joltage += joltage
		fmt.println(joltage)
	}

	fmt.println(output_joltage)
}
