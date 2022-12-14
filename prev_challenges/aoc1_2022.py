file_data = open('../puzzle_inputs/day12022.txt', 'r').read().split('\n')

# Solution with linear runtime and constant space
def part_one():
  max_cals = 0

  # Initialize current_sum at 0
  current_sum = 0

  for row in file_data:
    # If an empty string, check if current_sum is greater than max_cals 
    # and replace value if so
    if row == "":
      if current_sum > max_cals:
        max_cals = current_sum
      # Either way, reset current_sum        
      current_sum = 0
    else:
        current_sum += int(row)
  
  return max_cals


# Solution with linear runtime and constant space
def part_two():
  # Create 3 variables: first, second, third -- initialize at zero
  first, second, third = [0, 0, 0]
  current_sum = 0
  
  for row in file_data:
      # If an empty string, check if current_sum is greater than max_cals 
      # and replace value if so
      if row == "":
        # If current_sum > first, then third = second, second = first, first = current_sum
        if current_sum > first:
          third = second
          second = first
          first = current_sum
        # Else, if current_sum > second, then third = second, second = current_sum
        elif current_sum > second: 
          third = second
          second = current_sum
        # Else, if current_sum > third, third = current_sum
        elif current_sum > third:
          third = current_sum
        # Either way, reset current_sum
        current_sum = 0
      else:
        current_sum += int(row)

  return first + second + third

print(part_one())
print(part_two())