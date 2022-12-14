file_data = open('puzzle_inputs/day92022.txt', 'r').readlines()

def follow(head_x, head_y, orig_tail_x, orig_tail_y): 
  tail_x = orig_tail_x
  tail_y = orig_tail_y
  
  # same column
  if head_x == tail_x:
    if head_y > tail_y + 1:
      tail_y += 1
    elif head_y + 1 < tail_y:
      tail_y -= 1
  # same row
  elif head_y == tail_y:
    if head_x > tail_x + 1:
      tail_x += 1
    elif head_x + 1 < tail_x:
      tail_x -= 1
  else:
    # if not touching - that is, the coordinate values are more than one apart
    if abs(tail_x - head_x) > 1 or abs(tail_y - head_y) > 1:
      # head is right
      if head_x - tail_x > 0:
        tail_x += 1
      # head is above
      if head_y - tail_y > 0:
        tail_y += 1
      # head is left
      if tail_x - head_x > 0:
        tail_x -= 1
      # head is below
      if tail_y - head_y > 0:
        tail_y -= 1

  return (head_x, head_y, tail_x, tail_y)
  
def move(head_x, head_y, tail_x, tail_y, direction):  
  if direction == "R":
    #head_x += 1
    return follow(head_x + 1, head_y, tail_x, tail_y)
  elif direction == "L":
    return follow(head_x - 1, head_y, tail_x, tail_y)
    #head_x -= 1
  elif direction == "U":
    return follow(head_x, head_y + 1, tail_x, tail_y)    
    #head_y += 1
  else:
    return follow(head_x, head_y - 1, tail_x, tail_y)
    #head_y -= 1

  return follow(head_x, head_y, tail_x, tail_y)

def part_one():
  tail_x = tail_y = head_x = head_y = 0
  # Create set of tuples to represent unique spaces visited
  spaces_visited = {(tail_x, tail_y)}

  for line in file_data:
    direction = line.split()[0]
    magnitude = int(line.split()[1])
    for i in range(magnitude):
      head_x, head_y, tail_x, tail_y \
        = move(head_x, head_y, tail_x, tail_y, direction)
      spaces_visited.add((tail_x, tail_y))

  return len(spaces_visited)
          
def part_two():
  # Create set of tuples to represent unique spaces visited
  tail_spaces_visited = {(0, 0)}

  # 10 knots, initialized at (0, 0)
  knots_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  knots_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

  for line in file_data:
    direction = line.split()[0]
    magnitude = int(line.split()[1])

    for i in range(magnitude):

      # head moves, next knot gets updated 
      knots_x[0], knots_y[0], knots_x[1], knots_y[1] \
        = move(knots_x[0], knots_y[0], knots_x[1], knots_y[1], direction)
      # only going up to 9 to avoid index out of bounds error
      for j in range(1, 9):
        knots_x[j], knots_y[j], knots_x[j + 1], knots_y[j + 1] \
          = follow(knots_x[j], knots_y[j], knots_x[j + 1], knots_y[j + 1])

      tail_spaces_visited.add((knots_x[9], knots_y[9]))

  print(tail_spaces_visited)  

  return len(tail_spaces_visited)
    
print(part_one())
print(part_two())

