package main

import "core:fmt"
import "core:os"
import "core:sort"
import "core:strconv"
import "core:strings"

// Union Find
uf_create :: proc(num_elements: int) -> [dynamic]int {
	uf := [dynamic]int{}
	for i := 0; i < num_elements; i += 1 {
		append(&uf, i)
	}

	return uf
}

// didn't bother to make this fast as we only need to do this once
uf_count :: proc(uf: ^[dynamic]int) -> [dynamic]int {
	count := [dynamic]int{}
	for i := 0; i < len(uf^); i += 1 {
		append(&count, 0)
	}

	for i := 0; i < len(uf^); i += 1 {
		count[uf_find(uf, i)] += 1
	}

	return count
}

uf_union :: proc(uf: ^[dynamic]int, elem1: int, elem2: int) {
	group1 := uf_find(uf, elem1)
	group2 := uf_find(uf, elem2)
	uf^[group1] = group2
}

uf_find :: proc(uf: ^[dynamic]int, elem: int) -> int {
	parent_group := uf^[elem]
	if parent_group == elem {
		return elem
	}

	group := uf_find(uf, parent_group)
	uf^[elem] = group

	return group
}

// Kruskal
Node :: struct {
	id:      int,
	x, y, z: int,
}

Edge :: struct {
	u: Node,
	v: Node,
	c: int,
}

kruskal :: proc(edges: [dynamic]Edge, num_points: int, num_steps: int) -> [dynamic]int {
	uf := uf_create(num_points)

	remaining_connections := num_points - 1
	for i := 0; i < num_steps; i += 1 {
		u := edges[i].u
		v := edges[i].v

		// ignore edges from nodes that are already interconnected
		if uf_find(&uf, u.id) == uf_find(&uf, v.id) {
			continue
		}

		fmt.printfln(
			"Connecting boxes at (%i, %i, %i) and (%i, %i, %i) at distance, %i",
			u.x,
			u.y,
			u.z,
			v.x,
			v.y,
			v.z,
			edges[i].c,
		)

		remaining_connections -= 1
		if (remaining_connections == 0) {
			fmt.printfln("============= %i ============", u.x * v.x)
		}
		uf_union(&uf, u.id, v.id)
	}

	return uf_count(&uf)
}

euclidean_distance_squared :: proc(p1: Node, p2: Node) -> int {
	x := p2.x - p1.x
	y := p2.y - p1.y
	z := p2.z - p1.z

	return x * x + y * y + z * z
}

main :: proc() {
	data, ok := os.read_entire_file_from_filename_or_err("input.txt")
	if ok != nil {
		os.exit(1)
	}

	defer delete(data, context.allocator)

	lines := string(data)
	nodes := [dynamic]Node{}
	edges := [dynamic]Edge{}
	i := 0
	for line in strings.split_lines_iterator(&lines) {
		point_coords, _ := strings.split_n(line, ",", 3)
		x, _ := strconv.parse_int(point_coords[0])
		y, _ := strconv.parse_int(point_coords[1])
		z, _ := strconv.parse_int(point_coords[2])

		append(&nodes, Node{i, x, y, z})
		i += 1
	}

	for i := 0; i < len(nodes); i += 1 {
		for j := 0; j < len(nodes); j += 1 {
			// compare with >= to avoid duplicates
			if i >= j {continue}

			u := nodes[i]
			v := nodes[j]
			append(&edges, Edge{u, v, euclidean_distance_squared(u, v)})
		}
	}

	sort.quick_sort_proc(edges[:], proc(a: Edge, b: Edge) -> int {
		if (a.c < b.c) {return -1} else if (a.c > b.c) {return 1} else {return 0}
	})

	uf_count := kruskal(edges, len(nodes), len(edges))
}
