import json
import functools

file_data = open('puzzle_inputs/day132022.txt', 'r').readlines()

def compare_lists(left, right):

  # right ran out items
  if len(right) == 0:
    return False
  # left ran out of items 
  if len(left) == 0:
    return True

  for i in range(len(left)):
    
    if isinstance(left[i], int) and isinstance(right[i], int):
      if int(right[i]) < int(left[i]):
        return False
      # right is greater, do not need to continue
      elif int(right[i]) > int(left[i]):
        return True
      # so far equal values but right ran out of values
      elif i == len(right) - 1 and len(right) < len(left):
        return False
    # checks that both are lists
    elif isinstance(left[i], list) and isinstance(right[i], list):
      return compare_lists(left[i], right[i])
    # right is a list
    elif isinstance(left[i], int) and isinstance(right[i], list):
      return compare_lists([left[i]], right[i])
    # left is a list
    elif isinstance(left[i], list) and isinstance(right[i], int):
      return compare_lists(left[i], [right[i]])

  return True
    
def part_one():
  sum = 0
  for i in range(0, len(file_data), 3):
    left = json.loads(file_data[i])
    right = json.loads(file_data[i + 1])
    if compare_lists(left, right):
      sum += i / 3 + 1

  return sum

def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare

def part_two():
  all_packets = []
  for i in range(0, len(file_data), 3):
    left = json.loads(file_data[i])
    right = json.loads(file_data[i + 1])
    all_packets.append(left)
    all_packets.append(right)

  all_packets.sort(key=functools.cmp_to_key(make_comparator(compare_lists)))

  return (all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1)

    
print(part_one())
print(part_two())

