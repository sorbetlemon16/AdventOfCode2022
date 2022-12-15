from collections import deque 

file_data = open('puzzle_inputs/day122022.txt', 'r').readlines()

class Node:
  def __init__(self, coordinates, elevation, reachable):
    self.coordinates = coordinates
    self.elevation = elevation
    self.reachable = reachable

  def __repr__(self):
    return str(self.elevation) + str(self.reachable)

def get_starting_coordinates():

  for row_index in range(len(file_data)):
    for col_index in range(len(file_data[row_index])):
      if file_data[row_index][col_index] == "S":
        return (row_index, col_index)

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

  print(node_grid)
  
  # for row_index in range(len(node_grid)):
  #   for col_index in range(len(node_grid[row_index])):
  #     # update reachable to be nodes
  #     node_grid[row_index][col_index].reachable = get_nodes_from_coordinates(\
  #       node_grid[row_index][col_index].reachable, 
  #       node_grid)
  # print(node_grid)

  return node_grid

# def get_reachable_nodes(coordinate_list, node_grid):
#   reachable_nodes = set()
#   for coordinates in coordinate_list: 
#     row, col = coordinates
#     reachable_nodes.add(node_grid[row][col])
#   return reachable_nodes
    
# def get_nodes_from_coordinates(coordinate_list, node_grid):
#   nodes = set()
#   for coordinates in coordinate_list: 
#     row, col = coordinates
#     nodes.add(node_grid[row][col])
#   return nodes

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

def part_one():
  nodes = get_node_grid()

  start_row, start_col = get_starting_coordinates()

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

    # add reachable neighbors
    for node_coordinates in current_node.reachable - seen_coordinates:
      x, y = node_coordinates
      to_visit.append((nodes[x][y], current_distance))
      # if node not in seen:
      #   to_visit.append((node, current_distance))

  return "No possible path"
    
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
