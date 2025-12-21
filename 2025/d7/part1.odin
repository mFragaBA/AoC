package main

import "core:fmt"
import "core:os"
import "core:strconv"
import "core:strings"

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

	total_splits := 0
	start_position := strings.index(manifold[0], "S")
	current_tachyon_rays := make(map[int]bool)
	current_tachyon_rays[start_position] = true

	for step := 1; step < len(manifold); step += 1 {
		next_step_tachyon_rays := make(map[int]bool)
		for tachyon_ray in current_tachyon_rays {
			if manifold[step][tachyon_ray] == '^' {
				total_splits += 1
				if tachyon_ray - 1 >= 0 {
					next_step_tachyon_rays[tachyon_ray - 1] = true
				}
				if tachyon_ray + 1 < len(manifold[0]) {
					next_step_tachyon_rays[tachyon_ray + 1] = true
				}
			} else {
				next_step_tachyon_rays[tachyon_ray] = true
			}
		}

		current_tachyon_rays = next_step_tachyon_rays
	}

	fmt.println(total_splits)
}
