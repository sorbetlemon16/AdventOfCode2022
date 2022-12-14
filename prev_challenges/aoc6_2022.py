file_data = open('../puzzle_inputs/day62022.txt', 'r').read()

def part_one():
  for i in range(0, len(file_data) - 4):
    current_chars = {file_data[i], file_data[i + 1], file_data[i + 2], \
                     file_data[i + 3]}
    if len(current_chars) == 4:
      return i + 4
    
def part_two():
  # list of 26 zeros representing frequency of each character
  chars_present = [ 0 for _ in range(26) ]

  for i in range(0, len(file_data)):
    char_end_range = file_data[i]
    chars_present[ord(char_end_range) - 97] += 1

    # remove front range
    if i >= 14:
      char_start_range = file_data[i - 14]
      chars_present[ord(char_start_range) - 97] -= 1
      
    num_uniq_chars = 0
    for freq in chars_present:
      if freq > 0:
        num_uniq_chars += 1
    if num_uniq_chars == 14:
      return i + 1

    # only remove the one at the beginning if it's not there elsewhere
    
print(part_one())
print(part_two())