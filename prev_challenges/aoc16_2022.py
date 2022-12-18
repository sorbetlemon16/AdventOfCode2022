from collections import deque 

file_data = open('puzzle_inputs/day162022.txt', 'r').readlines()

class Node:
  def __init__(self, name, rate, leads_to):
    self.name = name
    self.rate = rate
    self.leads_to = leads_to
    self.pressure_released = 0

  def __repr__(self):
    return str(self.name) + " " + str(self.rate) + " " + str(self.pressure_released)

def bfs(node_dict, max_path_length):

  path_length = 0
  pressure_released  = 0
  # root is AA  
  to_visit = deque([(node_dict["AA"], path_length, pressure_released)])
  seen = set()

  while to_visit and path_length < max_path_length:
    # use queue for BFS
    current, path_length, pressure_released = to_visit.popleft()

    path_length += 1

    seen.add(current.name)

    for node_name in current.leads_to - seen:
      node_dict[node_name].pressure_released = pressure_released + node_dict[node_name].rate
      to_visit.append(\
        (node_dict[node_name], 
         path_length, 
         pressure_released + node_dict[node_name].rate))
      
      seen.add(node_name)

  return node_dict
    
    
def part_one():
  node_list = []
  node_dict = {}
  for row in file_data:
    line = row.strip("Valve \n").split(" ")
    # print(line)
    letter = line[0]
    rate = int(line[3].strip("rate=;"))
    leads_to = set()
    for tunnel in line[8:]:
      leads_to.add(tunnel.strip(","))
    node = Node(letter, rate, leads_to)
    node_dict[node.name] = node

  print(node_dict)

  # path length will need to equal 30 
  bfs(node_dict, 16)

  print(node_dict)
    
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
