defmodule Solution do
  @spec is_palindrome(s :: String.t()) :: boolean
  def is_palindrome(s) do
    string_normal =
      s
      |> String.downcase()
      |> String.replace(~r/[^a-z0-9]/, "")
      |> IO.inspect()

    string_ao_contrario = String.reverse(string_normal)

    string_normal == string_ao_contrario
  end
end
