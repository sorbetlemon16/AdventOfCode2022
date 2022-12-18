file_data = open('puzzle_inputs/day182022.txt', 'r').readlines()

def get_block_dicts():
  block_nested_dict = {}
  block_pairs_dict = {}
  for block in file_data: 
    line = block.strip().split(",")
    x, y, z = int(line[0]), int(line[1]), int(line[2])

    if z in block_nested_dict.keys():
      # pairs dict
      block_pairs_dict[z].add((x, y))

      # nested dict
      if y in block_nested_dict[z].keys():
        block_nested_dict[z][y].add(x)
      else:
        block_nested_dict[z][y] = set([x])
    else:
      # pairs dict
      block_pairs_dict[z] = set([(x, y)])

      # nested dict
      y_dict = {y: set([x])}
      block_nested_dict[z] = y_dict
  
  return (
    dict(sorted(block_nested_dict.items())), 
    dict(sorted(block_pairs_dict.items())))

def part_one():
  for row in file_data:
    print(row, end="")
  print()

  surface_area = 0

  block_nested_dict, block_pairs_dict = get_block_dicts()

  # for each thin slice
  for z in block_nested_dict.keys():
    
    for y in block_nested_dict[z]:
      # add all sides for each x y pair
      surface_area += 6 * len(block_nested_dict[z][y])

      # subtract sides that overlap
      for x in block_nested_dict[z][y]:
        # check adjacent x
        if x + 1 in block_nested_dict[z][y]:
          surface_area -= 2
        # check adjacent y
        if y + 1 in block_nested_dict[z]:
          if x in block_nested_dict[z][y + 1]:
            surface_area -= 2

    # subtract for bottom plane that overlap with next z 
    if z + 1 in block_nested_dict.keys():
      overlapping = len(block_pairs_dict[z] & block_pairs_dict[z + 1])
      surface_area -= overlapping

    # subtract for top plane that overlap with next z 
    if z - 1 in block_nested_dict.keys():
      overlapping = len(block_pairs_dict[z] & block_pairs_dict[z - 1])
      surface_area -= overlapping
      
      print("overlapping", z, overlapping)

    print(surface_area)
    
  for z in block_nested_dict.keys():
    print(z, block_nested_dict[z])
    # print(z, block_pairs_dict[z])

  return surface_area
    
def part_two():
   pass
    
print(part_one())
print(part_two())
