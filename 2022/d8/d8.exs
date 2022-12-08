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

  def is_visible(world_map, i, j) do
    all_less(:up, world_map, i, j) ||
    all_less(:right, world_map, i, j) ||
    all_less(:down, world_map, i, j) ||
    all_less(:left, world_map, i, j)
  end

  defp height(world_map, i, j) do
    world_map
    |> Enum.at(i)
    |> Enum.at(j)
  end

  defp all_less(:left, world_map, i, j) do
    height_at_i_j = height(world_map, i, j)
    (0..length(hd(world_map))-1)
    |> Enum.all?(fn y -> 
      y >= j || height_at_i_j > height(world_map, i, y)
    end)
  end

  defp all_less(:right, world_map, i, j) do
    height_at_i_j = height(world_map, i, j)
    (0..length(hd(world_map))-1)
    |> Enum.all?(fn y -> 
      y <= j || height_at_i_j > height(world_map, i, y)
    end)
  end

  defp all_less(:up, world_map, i, j) do
    height_at_i_j = height(world_map, i, j)
    (0..length(world_map)-1)
    |> Enum.all?(fn x -> 
      x >= i || height_at_i_j > height(world_map, x, j) 
    end)
  end

  defp all_less(:down, world_map, i, j) do
    height_at_i_j = height(world_map, i, j)
    (0..length(world_map)-1)
    |> Enum.all?(fn x -> 
      x <= i || height_at_i_j > height(world_map, x, j) 
    end)
  end
end

parsed_input = AdventDay8InputReader.read()

parsed_input
|> VisionCalculator.all_positions()
|> Enum.count(fn {i, j} -> 
  VisionCalculator.is_visible(parsed_input, i, j)
end)
|> IO.puts()
