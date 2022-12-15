file_data = open('puzzle_inputs/day72022.txt', 'r').readlines()

class Node:
  def __init__(self, name, size):
    self.name = name
    self.size = size
    self.children = []

def part_one():
  for row in file_data:
    line = row.rstrip().split()
    if line[0] == "$":
      if line[1] == "cd":
        dir_name = line[2]
        if dir_name != "/":
          new_dir = Node(dir_name, )
        
    
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