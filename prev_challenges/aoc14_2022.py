import os
import time

file_data = open('puzzle_inputs/day142022.txt', 'r').readlines()

def get_rock_grid(is_floor):
  x_vals = []
  y_vals = []
  for row in file_data: 
    rock_coords = row.strip().split(" -> ")
    for i in range(len(rock_coords)):
      x1, y1 = int(rock_coords[i].split(",")[0]), int(rock_coords[i].split(",")[1])
      x_vals.append(x1)
      y_vals.append(y1)

  length = max(x_vals) - min(x_vals) + 1 if not is_floor else 1002
  height = max(y_vals) + 1
  print("dimensions", length, height)

  x_shift = min(x_vals) if not is_floor else 0
  
  grid = [ [ "." for x in range(length + 1) ] for x in range(height + 1) ]

  # print_grid(grid)

  if is_floor:
    file_data.append(f"0,{max(y_vals)} -> 1000,{max(y_vals)}")

  for row in file_data: 
    rock_coords = row.strip().split(" -> ")

    # look at each pair of rock coordinates to get a line
    for i in range(len(rock_coords) - 1):
      x1, y1 = int(rock_coords[i].split(",")[0]), int(rock_coords[i].split(",")[1])
      x2, y2 = int(rock_coords[i + 1].split(",")[0]), int(rock_coords[i + 1].split(",")[1])
      is_horizontal = True if y1 == y2 else False

      # y stays the same
      if is_horizontal:
        start_x = min([x1, x2])
        for x_index in range(start_x, start_x + abs(x1 - x2) + 1):
          grid[y1][x_index - x_shift] = "#"
      else: 
        start_y = min([y1, y2])
        for y_index in range(start_y, start_y + abs(y1 - y2) + 1):
          grid[y_index][x1 - x_shift] = "#"

  return (grid, min(x_vals), max(x_vals), min(y_vals), max(y_vals), x_shift)

def print_grid(grid):
  time.sleep(0.2)
  os.system('clear') 
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      print(grid[r][c], end="")
    print()
  print()

def simulate_sand(has_floor):
  rock_grid, min_x, max_x, min_y, max_y, x_shift = get_rock_grid(has_floor)

  sand_num = 0

  while True:
    # particle of sand emerges
    sand_x = 500
    sand_y = 0
    settled = False

    # uncomment for animation of final placement of sand
    # print_grid(rock_grid)
    
    while not settled:
      # uncomment for animation of falling sand
      print_grid(rock_grid)
      if has_floor:
        if rock_grid[0][500 - x_shift] != ".":
          return sand_num
      else: 
        # sand out of bounds into the abyss
        if not (min_x < sand_x < max_x and sand_y < max_y):
          return sand_num
      # if below is air, sand drifts down 1
      if rock_grid[sand_y + 1][sand_x - x_shift] == ".":
        rock_grid[sand_y][sand_x - x_shift] = "."        
        sand_y += 1
        rock_grid[sand_y][sand_x - x_shift] = "o"
      # immediately below is occupied, check below left
      elif rock_grid[sand_y + 1][sand_x - x_shift - 1] == ".":
        rock_grid[sand_y][sand_x - x_shift] = "."        
        sand_y += 1
        sand_x -= 1
        rock_grid[sand_y][sand_x - x_shift] = "o"
      # below left occupied, check below right
      elif rock_grid[sand_y + 1][sand_x - x_shift + 1] == ".":
        rock_grid[sand_y][sand_x - x_shift] = "."        
        sand_y += 1
        sand_x += 1
        rock_grid[sand_y][sand_x - x_shift] = "o"
      else:
        settled = True

    sand_num += 1

  return sand_num
    
def part_one():
  return simulate_sand(False)
  
def part_two():
  return simulate_sand(True)
    
print(part_one())
print()
# print(part_two())

# Template

# def part_one():
    
# def part_two():
#    pass
    
# print(part_one())
# print(part_two())
