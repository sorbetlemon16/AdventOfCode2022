file_data = open('puzzle_inputs/day72022.txt', 'r').readlines()

class Node:
  def __init__(self, name, parent=None, size=None):
    self.name = name
    self.size = size
    self.parent = parent
    self.children = []

  def __repr__(self):
    return f"name: {self.name}, children: {self.children}"

def get_child_from_name(name, children):
  for child in children:
    if name == child.name:
      return child

def find_size(node):
  if node.size:
    return node.size

  size = 0
  for child in node.children:
    child.size = int(find_size(child))
    size += child.size

  return size

def create_tree(): 

  current_dir = Node("/")

  root = current_dir

  for row in file_data:
    line = row.rstrip().split()
    if line[0] == "$":
      if line[1] == "cd":
        dir_name = line[2]

        # ignore root directory
        if dir_name != "/":
          if dir_name == "..":
            current_dir = current_dir.parent
          else:
            child = get_child_from_name(dir_name, current_dir.children)
            if child: 
              current_dir = child
            else:
              new_dir = Node(name=dir_name, parent=current_dir)
              current_dir.children.append(new_dir)
              current_dir = new_dir
    else:
      if line[0] == "dir":
        new_dir = Node(name=line[1], parent=current_dir)
        current_dir.children.append(new_dir)
      else:
        new_file = Node(name=line[1], parent=current_dir, size=int(line[0]))
        current_dir.children.append(new_file)

  root.size = find_size(root)
  return root
  
def part_one():

  root = create_tree()
  to_visit = [ root ]

  sum = 0

  while to_visit:
    current = to_visit.pop()

    # dir with size over 100000
    if current.size <= 100000 and current.children:
      sum += current.size

    for child in current.children:
      to_visit.append(child)

  return sum
      
    
def part_two():
  root = create_tree()

  dir_sizes = []

  space_needed = 30000000 - (70000000 - root.size)

  to_visit = [ root ]

  while to_visit:
    current = to_visit.pop()
  
    if current.size >= space_needed and current.children:
      dir_sizes.append(current.size)
  
    for child in current.children:
      to_visit.append(child)

  dir_sizes.sort()
  return dir_sizes[0]
  
print(part_one())
print(part_two())

# Template

# def part_one():
    
# def part_two():
#    pass
    
# print(part_one())
# print(part_two())