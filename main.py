import ast

file_data = open('puzzle_inputs/day132022.txt', 'r').readlines()

def compare_lists(left, right):

  if len(left) > len(right):
    return False
    
  for i in range(len(left)):
    if isinstance(left[i], int) and isinstance(right[i], int):
      if int(right[i]) < int(left[i]):
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
  not_in_order = []
  sum = 0
  for i in range(0, len(file_data), 3):
    left = ast.literal_eval(file_data[i])
    right = ast.literal_eval(file_data[i + 1])
    if compare_lists(left, right):
      sum += i / 3 + 1

  return sum

def part_two():
   pass
    
print(part_one())
print(part_two())

# Template

# def part_one():
    
# def part_two():
#    pass
    
# print(part_one())
# print(part_two())

# for i in range(len(left)):
#     # print("left_i", left[i])
#     # print("right_i", right[i])
#     if left[i].isalnum() and right[i].isalnum():
#       # print("ahoy")
#       if int(right[i]) < int(left[i]):
#         return False
#     # checks that both are lists
#     elif not left[i].isalnum() and not right[i].isalnum():
#       # print("HERE")
#       return compare_lists(str_to_pseudolist(left[i]), str_to_pseudolist(right[i]))
#     # right is a list
#     elif left[i].isalnum() and not right[i].isalnum():
#       return int(left[i]) < int(right[i][1])
#     # right is a list
#     elif not left[i].isalnum() and right[i].isalnum():
#       return int(left[i][1]) < int(right[i])

#   return True
