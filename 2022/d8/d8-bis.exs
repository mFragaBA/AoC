defmodule AdventDay8InputReader do
  def read() do
    read_input_file()
    |> String.trim()
    |> String.split("\n")
    |> Enum.map(fn line -> 
      line
      |> String.graphemes
      |> Enum.map(fn c -> 
        {height, ""} = Integer.parse(c) 
        height
      end)
    end)
  end

  defp read_input_file() do
    {:ok, contents} = File.read("input.txt")
    contents
  end
end

defmodule VisionCalculator do

  def all_positions(map) do
    for x <- (0..length(map)-1), y <- (0..length(hd(map))-1) do
      {x, y}
    end
  end

  def scenic_score(world_map, i, j) do
    scenic_score(:up, world_map, i, j) *
    scenic_score(:right, world_map, i, j) *
    scenic_score(:down, world_map, i, j) *
    scenic_score(:left, world_map, i, j)
  end

  defp height(world_map, i, j) do
    world_map
    |> Enum.at(i)
    |> Enum.at(j)
  end

  defp scenic_score(:left, world_map, i, j) do
    height_at_i_j = height(world_map, i, j)
    stop_position = (j-1..0)
      |> Enum.find(0, fn y -> 
        y > 0 and height_at_i_j <= height(world_map, i, y)
      end)
    j - stop_position
  end

  defp scenic_score(:right, world_map, i, j) do
    height_at_i_j = height(world_map, i, j)
    stop_position = (j+1..length(hd(world_map))-1)
      |> Enum.find(length(hd(world_map))-1, fn y -> 
        y < length(hd(world_map)) and height_at_i_j <= height(world_map, i, y)
      end)
    stop_position - j
  end

  defp scenic_score(:up, world_map, i, j) do
    height_at_i_j = height(world_map, i, j)
    stop_position = (i-1..0)
      |> Enum.find(0, fn x -> 
        x > 0 and height_at_i_j <= height(world_map, x, j)
      end)
    i - stop_position
  end

  defp scenic_score(:down, world_map, i, j) do
    height_at_i_j = height(world_map, i, j)
    stop_position = (i+1..length(world_map)-1)
      |> Enum.find(length(world_map)-1, fn x -> 
        x < length(world_map) and height_at_i_j <= height(world_map, x, j)
      end)
    stop_position - i
  end
end

parsed_input = AdventDay8InputReader.read()

parsed_input
|> VisionCalculator.all_positions()
|> Enum.map(fn {i, j} -> 
  VisionCalculator.scenic_score(parsed_input, i, j)
end)
|> Enum.max
|> IO.puts()
