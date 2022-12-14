file_data = open('puzzle_inputs/day82022.txt', 'r').readlines()

def create_visibility_grid():
  num_rows = len(file_data)
  num_cols = len(file_data[0].strip())
  num_visible = num_cols * 2 + 2 * (num_rows - 2)

  # initialize 2D array to all false
  is_visible = [ [ False for x in range (num_cols - 2) ] for x in range(num_rows - 2) ]

  # GET TREES VISIBLE FROM LEFT
  # indices are off by one to account for outer edges which we ignore 
  for row_index in range(1, num_rows - 1):
    # leftmost tree height in row
    max_left = file_data[row_index][0]
    for col_index in range(1, num_cols - 1):
      if (file_data[row_index][col_index] > max_left):
        max_left = file_data[row_index][col_index]
        # off by one to account for off by one in row_index and col_index
        is_visible[row_index - 1][col_index - 1] = True

  # GET TREES VISIBLE FROM RIGHT
  # indices are off by one to account for outer edges which we ignore 
  for row_index in range(1, num_rows - 1):
    # rightmost tree height in row
    max_right = file_data[row_index][num_cols - 1]
    # step is -1 to go from the opposite direction: left to right
    for col_index in range(num_cols - 2, 0, -1):
      if (file_data[row_index][col_index] > max_right):
        max_right = file_data[row_index][col_index]
        # off by one to account for off by one in row_index and col_index
        is_visible[row_index - 1][col_index - 1] = True

  # GET TREES VISIBLE FROM TOP
  # indices are off by one to account for outer edges which we ignore 
  for col_index in range(1, num_cols - 1):
    # top tree height in column
    max_top = file_data[0][col_index]
    for row_index in range(1, num_rows - 1):
      if (file_data[row_index][col_index] > max_top):
        max_top = file_data[row_index][col_index]
        # off by one to account for off by one in row_index and col_index
        is_visible[row_index - 1][col_index - 1] = True

  # GET TREES VISIBLE FROM BOTTOM
  # indices are off by one to account for outer edges which we ignore 
  # step is -1 to go from the opposite direction
  for col_index in range(1, num_cols - 1):
    # bottom tree height in column
    max_bottom = file_data[num_rows - 1][col_index]
    for row_index in range(num_rows - 2, 0, -1):
      if (file_data[row_index][col_index] > max_bottom):
        max_bottom = file_data[row_index][col_index]
        # off by one to account for off by one in row_index and col_index
        is_visible[row_index - 1][col_index - 1] = True

  return is_visible

# O(n) time and space complexity where n is the number of trees
def part_one():
  visibility_grid = create_visibility_grid()
  num_rows = len(visibility_grid)
  num_cols = len(visibility_grid[0])
  num_visible = (num_cols + 2)* 2 + 2 * num_rows
  for row in visibility_grid:
    for entry in row:
      if entry:
        num_visible += 1 

  return num_visible   

# GET SCENERY SCORES FROM LEFT
def create_left_scenic_score_grid(num_rows, num_cols):

  # initialize 2D array to all 0
  scenic_score = [ [ 0 for x in range (num_cols - 2) ] for x in range(num_rows - 2) ]

  # indices are off by one to account for outer edges which we ignore 
  for row_index in range(1, num_rows - 1):
    # leftmost tree in inner grid always 1
    scenic_score[row_index - 1][0] = 1
    for col_index in range(2, num_cols - 1):
      # initialize view length to one at the start of each row
      view_length = 1
      # go reverse for contiguous
      for scan_index in range(col_index - 1, 0, -1):
        if file_data[row_index][col_index] > file_data[row_index][scan_index]:
          view_length += 1
        else:
          break

      # off by one to account for off by one in row_index and col_index
      scenic_score[row_index - 1][col_index - 1] = view_length

  return scenic_score 

# GET SCENERY SCORES FROM RIGHT
def create_right_scenic_score_grid(num_rows, num_cols):

  # initialize 2D array to all 0
  scenic_score = [ [ 0 for x in range (num_cols - 2) ] for x in range(num_rows - 2) ]

  # indices are off by one to account for outer edges which we ignore 
  for row_index in range(1, num_rows - 1):
    # righmost tree in inner grid always 1
    scenic_score[row_index - 1][num_cols - 3] = 1
    for col_index in range(1, num_cols - 1):
      # initialize view length to one at the start of each row
      view_length = 1
      for scan_index in range(col_index + 1, num_cols - 1):
        if file_data[row_index][col_index] > file_data[row_index][scan_index]:
          view_length += 1
        else:
          break

      # off by one to account for off by one in row_index and col_index
      scenic_score[row_index - 1][col_index - 1] = view_length

  return scenic_score

# GET SCENERY SCORES FROM BOTTOM
def create_bottom_scenic_score_grid(num_rows, num_cols):

  # initialize 2D array to all 0
  scenic_score = [ [ 0 for x in range (num_cols - 2) ] for x in range(num_rows - 2) ]

  # indices are off by one to account for outer edges which we ignore 
  for col_index in range(1, num_rows - 1):
    # bottommost tree in inner grid always 1
    scenic_score[num_rows - 3][col_index - 1] = 1
    for row_index in range(num_rows - 3, 0, -1):
      # initialize view length to one at the start of each column
      view_length = 1
      for scan_index in range(row_index + 1, num_rows - 1):
        if file_data[row_index][col_index] > file_data[scan_index][col_index]:
          view_length += 1
        else:
          break

      # off by one to account for off by one in row_index and col_index
      scenic_score[row_index - 1][col_index - 1] = view_length

  return scenic_score

# GET SCENERY SCORES FROM TOP
def create_top_scenic_score_grid(num_rows, num_cols):

  # initialize 2D array to all 0
  scenic_score = [ [ 0 for x in range (num_cols - 2) ] for x in range(num_rows - 2) ]

  # indices are off by one to account for outer edges which we ignore 
  for col_index in range(1, num_rows - 1):
    # topmost tree in inner grid always 1
    scenic_score[0][col_index - 1] = 1
    for row_index in range(2, num_rows - 1):
      # initialize view length to one at the start of each column
      view_length = 1
      for scan_index in range(row_index - 1, 0, -1):
        if file_data[row_index][col_index] > file_data[scan_index][col_index]:
          view_length += 1
        else:
          break

      # off by one to account for off by one in row_index and col_index
      scenic_score[row_index - 1][col_index - 1] = view_length

  return scenic_score
  
def part_two():

  num_rows = len(file_data)
  num_cols = len(file_data[0].strip())

  left = create_left_scenic_score_grid(num_rows, num_cols)
  right = create_right_scenic_score_grid(num_rows, num_cols)
  top = create_top_scenic_score_grid(num_rows, num_cols)
  bottom = create_bottom_scenic_score_grid(num_rows, num_cols)

  print(left)
  print(right)
  print(top)
  print(bottom)

  max = 0

  for row_index in range(num_rows - 2):
    for col_index in range(num_cols - 2):
      scenic_score = left[row_index][col_index] * right[row_index][col_index] \
        * top[row_index][col_index] * bottom[row_index][col_index]
      if scenic_score > max:
        max = scenic_score

  return max
    
print(part_one())
print(part_two())


# Template

# def part_one():
    
# def part_two():
#    pass
    
# print(part_one())
# print(part_two())
