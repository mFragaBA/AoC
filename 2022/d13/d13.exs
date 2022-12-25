defmodule AdventDay13InputReader do
  def read() do
    read_input_file()
    |> String.trim()
    |> String.split("\n\n")
    |> Enum.map(fn pairs -> 
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

_parsed_input = AdventDay13InputReader.read()
|> Enum.with_index(1)
|> Enum.filter(fn {[first, second], _index} -> 
    # IO.inspect(first, label: "FIRST", charlists: false)
    # IO.inspect(second, label: "SECOND", charlists: false)
    (ListComparator.properly_sorted(first, second) == :yes) 
    # |> IO.inspect(label: "WELL SORTED?")
  end)
|> Enum.map(fn {_pairs, index} -> index end)
|> Enum.sum()
|> IO.inspect()
