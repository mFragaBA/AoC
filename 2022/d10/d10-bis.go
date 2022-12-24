package main

import (
	"fmt"
	"os"
	"strings"
  "strconv"
)

// Type Definitions

type Instruction int64

const (
  Noop Instruction = iota
  Addx
)

func (i Instruction) String() string {
  switch i {
  case Noop:
    return "noop"
  case Addx:
    return "addx"
  }

  return "unknown"
}

func buildInstruction(s string) Instruction {
  switch s {
    case "noop":
      return Noop
    default:
      return Addx
  }
}

// Helper Functions

func printInstruction(i Instruction) {
  fmt.Println("instruction: ", i)
}

func parseInstruction(line string) (Instruction, []string) {
  items := strings.Split(line, " ")
  instruction := buildInstruction(items[0])
  return instruction, items[1:]
}

func step(cycle int64, x int64) int64 {
  pixel := "."
  if (cycle % 40) == x || (cycle % 40) == x + 1 || (cycle % 40) == x + 2 {
    pixel = "#"
  }

  fmt.Print(pixel)
  if cycle % 40 == 0 {
    fmt.Print("\n")
  }

  return cycle + 1
}

func main() {
  input, _ := os.ReadFile("input.txt")
  // fmt.Print(string(input))
  var cycle int64 = 1
  var x int64 = 1
  for _, line := range strings.Split(strings.Trim(string(input), "\n"), "\n") {
    // fmt.Printf("%v\n", string(line))
    instr, args := parseInstruction(line)
    // printInstruction(instr)
    // fmt.Println(args)
    switch instr {
    case Noop:
        cycle = step(cycle, x)
    case Addx: {
      for i:= 0; i < 2; i++ {
        cycle = step(cycle, x)
      }
      y, _ := strconv.Atoi(args[0])
      x += int64(y)
    }
    }
  }
}
