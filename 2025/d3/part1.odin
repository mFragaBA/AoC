package main

import "core:fmt"
import "core:os"
import "core:strings"

char_to_int :: proc(c: u8) -> int {
	return int(c) - '0'
}

find_largest_battery_in_subbank :: proc(bank: string, from_i: int, to_i: int) -> int {
	largest_i := from_i
	for i := from_i + 1; i < to_i; i += 1 {
		if bank[i] > bank[largest_i] {
			largest_i = i
		}
	}

	return largest_i
}

get_max_joltage :: proc(bank: string) -> int {
	selected_battery_joltages := [2]int{0, 0}
	largest_i := find_largest_battery_in_subbank(bank, 0, len(bank))

	second_largest_from := (largest_i + 1) if largest_i < len(bank) - 1 else 0
	second_largest_to := len(bank) if largest_i < len(bank) - 1 else largest_i
	battery_slot := 0 if largest_i < len(bank) - 1 else 1

	selected_battery_joltages[battery_slot] = char_to_int(bank[largest_i])

	second_largest_i := find_largest_battery_in_subbank(
		bank,
		second_largest_from,
		second_largest_to,
	)

	selected_battery_joltages[1 - battery_slot] = char_to_int(bank[second_largest_i])
	return 10 * selected_battery_joltages[0] + selected_battery_joltages[1]
}

main :: proc() {
	data, ok := os.read_entire_file_from_filename_or_err("input.txt")
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
