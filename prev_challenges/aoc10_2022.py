file_data = open('puzzle_inputs/day102022.txt', 'r').readlines()

def get_x_values():
  x_values = [1]
  x_value = 1
  for i in range(len(file_data)):
    line = file_data[i].rstrip()
    if line != "noop":
      delta = int(line.split()[1])
      # add an extra for the extra time
      x_values.append(x_value)
      x_value += delta
    x_values.append(x_value)
  return x_values

def part_one():
  x_values = get_x_values()

  sum = 0
  for i in range(len(x_values)):
    if (i + 1) % 40 == 20:
      sum += (i + 1) * x_values[i]

  return sum
  
def part_two():
  x_values = get_x_values()

  for i in range(len(x_values)):
    if x_values[i] - 1 <= i % 40 <= x_values[i] + 1:
      print(".", end ="")
    else:
      print("#", end ="")
    
    if i % 40 == 0:
      print()

  print()
    
print(part_one())
part_two()