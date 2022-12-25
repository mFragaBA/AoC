defmodule AdventDay13InputReader do
  def read() do
    read_input_file()
    |> String.trim()
    |> String.split("\n\n")
    |> Enum.flat_map(fn pairs -> 
      pairs
      |> String.split("\n")
      |> Enum.map(fn liststr -> 
        {result, _} = Code.eval_string(liststr) 
        result
      end)
    end)
  end 

  defp read_input_file() do
    {:ok, contents} = File.read("input.txt")
    contents
  end
end

defmodule ListComparator do
  def properly_sorted([], []), do: :continue
  def properly_sorted([], second), do: :yes
  def properly_sorted(first, []), do: :no
  def properly_sorted([a | first], [b | second]) when is_number(a) and is_number(b) do
    cond do
      a < b -> :yes
      a == b -> properly_sorted(first, second)
      a > b -> :no
    end
  end
  def properly_sorted([a | first], [b | second]) when is_number(a) do
    properly_sorted([[a] | first], [b | second])
  end
  def properly_sorted([a | first], [b | second]) when is_number(b) do
    properly_sorted([a | first], [[b] | second])
  end
  def properly_sorted([a | first], [b | second]) do
    sorted? = properly_sorted(a, b)
    if sorted? == :continue do
      properly_sorted(first, second)
    else 
      sorted?
    end
  end
end

sorted_messages = (AdventDay13InputReader.read() ++ [[[2]], [[6]]])
|> Enum.sort(fn x, y -> 
    (ListComparator.properly_sorted(x, y) == :yes) 
  end)

index_1 = Enum.find_index(sorted_messages, fn x -> x == [[2]] end)
index_2 = Enum.find_index(sorted_messages, fn x -> x == [[6]] end)

IO.inspect((index_1+1) * (index_2+1))
