from collections import deque 

file_data = open('puzzle_inputs/day122022.txt', 'r').readlines()

class Node:
  def __init__(self, coordinates, elevation, reachable):
    self.coordinates = coordinates
    self.elevation = elevation
    self.reachable = reachable

  def __repr__(self):
    return str(self.elevation) + str(self.reachable)

def get_coordinates_at_square(find):
  coord_pairs = []
  for row_index in range(len(file_data)):
    for col_index in range(len(file_data[row_index])):
      if file_data[row_index][col_index] == find:
        coord_pairs.append((row_index, col_index))
  return coord_pairs

def get_elevation(row, col):
  if file_data[row][col] == "S":
    return 0
  if file_data[row][col] == "E":
    return 26
  return ord(file_data[row][col]) - 97

def get_node_grid():
  # initialize 2D array
  node_grid = [ [ None for x in range(len(file_data[0].strip())) ] for x in range(len(file_data)) ]
  for row_index in range(len(file_data)):
    for col_index in range(len(file_data[row_index].strip())):
      elevation = get_elevation(row_index, col_index)
      coordinates = (row_index, col_index)
      reachable = get_reachable_coordinates(coordinates, elevation)
      node_grid[row_index][col_index] = Node(coordinates, elevation, reachable)
  
  return node_grid

# returns booleans for reachable in up, down, left, right
def get_reachable_coordinates(coordinates, elevation):
  row, col = coordinates
  reachable = set()
  
  # check can move up 
  if row - 1 >= 0:
    if elevation + 1 >= get_elevation(row - 1, col):
      reachable.add((row - 1, col))
  # check can move left 
  if col - 1 >= 0:
    if elevation + 1 >= get_elevation(row, col - 1):
      reachable.add((row, col - 1))
  # check can move right
  if col + 1 < len(file_data[0].strip()):
    if elevation + 1 >= get_elevation(row, col + 1):      
      reachable.add((row, col + 1))
  # check can move down
  if row + 1 < len(file_data):
    if elevation + 1 >= get_elevation(row + 1, col):
      reachable.add((row + 1, col))

  return reachable
  
def shortest_possible_path(nodes, starting_coordinates):

  start_row, start_col = starting_coordinates

  # to_visit consists of tuples with a node and distance from start 
  to_visit = deque([(nodes[start_row][start_col], 0)])
  seen_coordinates = set()

  while to_visit:
    # use queue for BFS to get shortest path
    current_node, current_distance = to_visit.popleft()

    # this means we found the end
    if current_node.elevation == 26:
      return current_distance

    seen_coordinates.add(current_node.coordinates)

    current_distance += 1

    for node_coordinates in current_node.reachable - seen_coordinates:
      x, y = node_coordinates
      to_visit.append((nodes[x][y], current_distance))
      # THIS IS WHAT GOT ME
      seen_coordinates.add(node_coordinates)

  return None

def part_one():
  nodes = get_node_grid()
  starting_coordinates = get_coordinates_at_square("S")[0]

  return shortest_possible_path(nodes, starting_coordinates)
    
def part_two():
  nodes = get_node_grid()
  coord_pair_list = get_coordinates_at_square("a")
  min_distance = 352

  for coord_pair in coord_pair_list:
    shortest_path_distance = shortest_possible_path(nodes, coord_pair)
    if shortest_path_distance and shortest_path_distance < min_distance: 
      min_distance = shortest_path_distance

  return min_distance
    
print(part_one())
print(part_two())