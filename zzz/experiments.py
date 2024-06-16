def count_symbols(text):

  symbol_counts = {}
  for char in text:
    if char not in symbol_counts:
      symbol_counts[char] = 0
    symbol_counts[char] += 1
  return symbol_counts

# Example usage (replace 'w3schools' with your desired string)
user_input = "w3schools"
symbol_counts = count_symbols(user_input)

print(symbol_counts)