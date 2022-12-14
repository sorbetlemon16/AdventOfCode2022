file_data = open('../puzzle_inputs/day52022.txt', 'r').read().split('\n')

def part_one():

  # Originally considered using a 2-D list (list of lists), but would need to
  # calculate number of columns ahead of time, went with a dictionary for 
  # simplicity and readability
  stacks = {}

  # Create stack dictionary
  for i in range(len(file_data)):
    line = file_data[i]
    if line[1] == "1":
        rearr_start_index = i + 2
        break
    # Values at indices 1 + 4x
    for index in range(len(line)):
      if (index - 1) % 4 == 0:
        if line[index] != " ":
          # column number starts at 1
          stack_index = int((index - 1) / 4) + 1
          if stack_index not in stacks:
            stacks[stack_index] = []
          stacks[stack_index].append(line[index])

  # Reverse order of lists so that popping will take constant time
  for key in stacks.keys():
    stacks[key] = list(reversed(stacks[key]))

  # Rearrangement procedure for part one
  # for i in range(rearr_start_index, len(file_data)):
  #   _, num_move, _, move_from, _, move_to = file_data[i].split()
  #   for i in range(int(num_move)):
  #     stacks[int(move_to)].append(stacks[int(move_from)].pop())

  print(stacks)
  # Rearrangement procedure for part two
  for i in range(rearr_start_index, len(file_data)):
    rearr_indices = file_data[i].split()
    num_move = int(rearr_indices[1])
    move_from = int(rearr_indices[3])
    move_to = int(rearr_indices[5])

    # get slice from stack to move from 
    slice_to_add = stacks[int(move_from)][len(stacks[int(move_from)]) - int(num_move):]

    # update stack to remove slice
    stacks[move_from] = stacks[move_from][:len(stacks[int(move_from)]) - int(num_move)]    

    # add slice to new stack
    stacks[int(move_to)].extend(slice_to_add)
  
  end_chars = []  
  for key in sorted(stacks.keys()):
    end_chars.append(stacks[key].pop())

  return "".join(end_chars)
       
print(part_one())

# Template

# def part_one():
    
# def part_two():
#    pass
    
# print(part_one())
# print(part_two())

