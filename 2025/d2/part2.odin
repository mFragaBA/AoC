package main

import "core:fmt"
import "core:os"
import "core:strconv"
import "core:strings"

is_sequence_splitable_in_equal_chunks :: proc(seq: string, chunk_size: int) -> bool {
	num_chunks := len(seq) / chunk_size

	for chunk_offset := 0; chunk_offset < chunk_size; chunk_offset += 1 {
		expected_digit := seq[chunk_offset]
		for num_chunk := 0; num_chunk < num_chunks; num_chunk += 1 {
			if expected_digit != seq[num_chunk * chunk_size + chunk_offset] {
				return false
			}
		}
	}

	return true
}

is_invalid_sequence :: proc(seq: string) -> bool {
	for split_size := 1; split_size <= len(seq) / 2; split_size += 1 {
		if len(seq) % split_size != 0 {
			continue
		}

		if is_sequence_splitable_in_equal_chunks(seq, split_size) {
			return true
		}
	}

	return false
}

main :: proc() {
	data, ok := os.read_entire_file_from_filename_or_err("input.txt")
	if ok != nil {
		os.exit(1)
	}

	defer delete(data, context.allocator)

	invalid_ids_sum := 0
	intervals := string(data)
	for interval in strings.split_iterator(&intervals, ",") {
		trimmed_interval := strings.trim(interval, "\t\r\n")
		split_interval, err := strings.split_n(trimmed_interval, "-", 2)

		if err != nil {
			fmt.eprintln("error spliting interval")
			os.exit(1)
		}

		// fmt.println(split_interval[0], split_interval[1])

		from_interval, _ := strconv.parse_int(split_interval[0])
		to_interval, _ := strconv.parse_int(split_interval[1])

		// fmt.printfln(
		// 	"%s | %s | Interval %v - %v",
		// 	interval,
		// 	split_interval,
		// 	from_interval,
		// 	to_interval,
		// )

		for i := from_interval; i <= to_interval; i += 1 {
			i_str := fmt.tprintf("%v", i)
			if is_invalid_sequence(i_str) {
				fmt.printfln("%s is invalid sequence", i_str)
				invalid_ids_sum += i
			}
		}
	}

	fmt.println(invalid_ids_sum)
}
