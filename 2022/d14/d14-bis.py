import os
import sys
import time

"""
Submition for Advent of Code 2022 - Day 14 Part 2

## How to RUN
```bash
# to run normally, just displays the solution and that's it
python3 d14-bis.py
# to run while rendering the simulation
RENDER=ON python3 d14-bis.py
```
"""

def make_point(p):
    return [int(p[0]), int(p[1])]

SAND = 'o'
ROCK = '#'
VOID = '.'

RENDER_ON = os.getenv("RENDER") == "ON"

class StepResult:
    CONT = 0
    NEXT = 1
    END = 2

color = {
    SAND: '33',
    ROCK: '31',
    VOID: '0'
}

class World:
    def __init__(self, paths) -> None:
        # We're eyeballing the necessary dimensions
        self.minx = 200
        self.maxx = max(max([max([p[0] for p in l]) for l in paths]), 800)
        self.miny = min([min([p[1] for p in l]) for l in paths])
        self.maxy = max([max([p[1] for p in l]) for l in paths])
        # print("minx: " + str(self.minx))
        # print("maxx: " + str(self.maxx))
        # print("miny: " + str(self.miny))
        # print("maxy: " + str(self.maxy))
        self.xrange = self.maxx - self.minx

        self.floor_height = self.maxy + 2
        self.maxy = self.floor_height

        self.world_map = [[VOID for _ in range(self.xrange + 1)] for _ in range(self.maxy + 1)]
        self.add_rock_paths(paths)
        self.spawn_next = True
        self.finished = False

        # set floor
        for x in range(self.minx, self.maxx + 1):
            self.add_tile(x, self.floor_height, ROCK)



    def try_step(self):
        down = [self.current_sand[0], self.current_sand[1] + 1]
        left_down = [self.current_sand[0] - 1, self.current_sand[1] + 1]
        right_down = [self.current_sand[0] + 1, self.current_sand[1] + 1]

        if self.tile_at(down[0], down[1]) == VOID:
            self.current_sand = down
            return StepResult.CONT

        if self.tile_at(left_down[0], left_down[1]) == VOID:
            self.current_sand = left_down
            return StepResult.CONT

        if self.tile_at(right_down[0], right_down[1]) == VOID:
            self.current_sand = right_down
            return StepResult.CONT

        return StepResult.NEXT


    def step(self):
        if self.spawn_next:
            if self.tile_at(500, 0) == SAND:
                self.finished = True
            self.current_sand = [500, 0]
            self.spawn_next = False
        else:
            match self.try_step():
                case StepResult.CONT:
                    self.spawn_next = False
                case StepResult.NEXT:
                    self.add_tile(self.current_sand[0], self.current_sand[1], SAND)
                    self.spawn_next = True
                    self.finished = False
                case StepResult.END:
                    self.finished = True

    def out_of_bounds(self, x, y):
        return x < self.minx or x > self.maxx or y > self.maxy

    def did_end(self):
        return self.finished

    def tile_at(self, x, y):
        if y == self.floor_height:
            return ROCK
        xpos = x - self.minx
        return self.world_map[y][xpos]

    def add_tile(self, x, y, tile):
        xpos = x - self.minx
        self.world_map[y][xpos] = tile

    def add_rock_paths(self, paths):
        for path in paths:
            self.add_rock_path(path)

    def add_rock_path(self, path):
        for i in range(len(path) - 1):
            self.add_rock_line(path[i], path[i+1])
        
    def add_rock_line(self, start, end):
        # print(f'add rock line ({start[0]}, {start[1]}) -> ({end[0]}, {end[1]})')
        if start[0] == end[0]:
            # vertical line
            for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                self.add_tile(start[0], y, ROCK)
        else:
            # horizontal line
            for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                self.add_tile(x, start[1], ROCK)

    def draw(self):
        #os.system('clear')
        # move cursor to the top of the screen
        sys.stdout.write('\033[;H')
        sys.stdout.flush()

        # show a piece of the map instead of everything
        curr_sand_pos = self.current_sand if hasattr(self, 'current_sand') else [500, 0]
        start_x = max(curr_sand_pos[0] - 70, self.minx)
        end_x = min(start_x + 140, self.maxx)
        start_y = max(curr_sand_pos[1] - 20, 0)
        end_y = min(start_y + 30, self.maxy)

        for y in range(start_y, end_y + 1):
            for xr in range(start_x, end_x + 1):
                x = xr - self.minx
                if hasattr(self, 'current_sand') and xr == self.current_sand[0] and y == self.current_sand[1]:
                    sys.stdout.write(f'\033[1m\033[1;33m{SAND}\033[0m')
                else:
                    particle = self.world_map[y][x]
                    sys.stdout.write(f'\033[0;{color[particle]}m{particle}')
            sys.stdout.write("\n")
        sys.stdout.flush()

    def count_sand_grains(self):
        total = 0
        for y in range(len(self.world_map)):
            for x in range(len(self.world_map[0])):
                if self.world_map[y][x] == SAND:
                    total += 1

        return total

    

with open("input.txt", "r") as infile:
    paths = [[make_point(point.split(",")) for point in line.split(" -> ")] for line in infile.read().splitlines()]

# Hide cursor
sys.stdout.write("\033[?25l")
sys.stdout.flush()

world = World(paths)

if RENDER_ON:
    os.system("clear")
    world.draw()
    time.sleep(0.01)

while True:
    world.step()
    if RENDER_ON:
        world.draw()
        time.sleep(0.01)
        
    if world.did_end():
        break

print(f'total_sand_grains: {world.count_sand_grains()}')
