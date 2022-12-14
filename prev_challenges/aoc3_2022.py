file_data = open('../puzzle_inputs/day32022.txt', 'r').read().split('\n')

# Solution with O(n) runtime and O(n) space complexity where n is the number 
# of characters in the file
def part_one():
  sum = 0
  for row in file_data:
    half_index = int(len(row) / 2)
    first_comp = set(row[:half_index])
    second_comp = set(row[half_index:])
    for letter in first_comp:
      # in operator is constant for sets
      # this solution also works if there are multiple common characters
      if letter in second_comp:
        priority = ord(letter) - 38 if letter.isupper() else ord(letter) - 96
        sum += priority
  return sum
    
# Solution with O(n) runtime and O(n) space complexity where n is the number 
# of characters in the file  
def part_two():
  letter_freq = {}
  sum = 0
  for row_index in range(len(file_data)):
    # When index is a multiple of 3, reset dictionary
    if row_index % 3 == 0:
      letter_freq = {}

    # Look through each unique letter in each row (convert to set to prevent duplicates)
    for letter in set(file_data[row_index]):
      # If letter is not yet a key, create key-value pair with value 0
      if letter not in letter_freq:
        letter_freq[letter] = 0

      # Increase frequency
      letter_freq[letter] += 1

      # This means the letter appears in all 3 
      if letter_freq[letter] == 3:
        priority = ord(letter) - 38 if letter.isupper() else ord(letter) - 96
        sum += priority
  return sum
    
print(part_one())
print(part_two())