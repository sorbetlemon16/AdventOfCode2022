file_data = open('../puzzle_inputs/day42022.txt', 'r').read().split('\n')

def part_one():
  total = 0
  for line in file_data:
    first, second = line.split(',')
    first_lower_bound, first_upper_bound = first.split('-')
    second_lower_bound, second_upper_bound = second.split('-')
 
    # If first range subsumes second range
    if int(first_lower_bound) <= int(second_lower_bound) and \
         int(first_upper_bound) >= int(second_upper_bound):
      total += 1
    # If second range subsumes first range
    elif int(second_lower_bound) <= int(first_lower_bound) and \
          int(second_upper_bound) >= int(first_upper_bound):
      total += 1
  return total
    
def part_two():
  total = 0
  for line in file_data:
    first, second = line.split(',')
    first_lower_bound, first_upper_bound = first.split('-')
    second_lower_bound, second_upper_bound = second.split('-')

    # Any of these conditions mean an overlap:
    # second_lower_bound is inside the first range
    # second_upper_bound is inside the first range
    # first_lower_bound is inside the second range
    # first_upper_bound is inside the second range

    if int(first_lower_bound) <= int(second_lower_bound) <= int(first_upper_bound) \
      or int(first_lower_bound) <= int(second_upper_bound) <= int(first_upper_bound) \
      or int(second_lower_bound) <= int(first_lower_bound) <= int(second_upper_bound) \
      or int(second_lower_bound) <= int(first_upper_bound) <= int(second_upper_bound):
      total += 1
    else:
      print(first, second)

  return total
  
print(part_one())
print(part_two())

# Template

# file_data = open('day42022.txt', 'r').read().split('\n')

# def part_one():
    
# def part_two():
#    pass
    
# print(part_one())
# print(part_two())