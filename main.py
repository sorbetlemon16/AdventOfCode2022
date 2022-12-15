import re

file_data = open('puzzle_inputs/day152022.txt', 'r').readlines()

def part_one(y):

  x_vals = set()
  objects_at_y = set()
  for row in file_data:
    # remove non-numbers
    coordinates = re.split(r'\D+',row.strip())

    # can't get rid of space in front?
    sensor_x = int(coordinates[1])
    sensor_y = int(coordinates[2])
    beacon_x = int(coordinates[3])
    beacon_y = int(coordinates[4])
    x_dist = abs(sensor_x - beacon_x)
    y_dist = abs(sensor_y - beacon_y)

    total_dist = x_dist + y_dist

    if beacon_y == y:
      objects_at_y.add(beacon_x)
    if sensor_y == y:
      objects_at_y.add(sensor_x)

    # check if sensor overlaps
    if sensor_y - total_dist <= y <= sensor_y + total_dist:
      level_overlap = total_dist - abs(y - sensor_y)
      min_x = sensor_x - level_overlap
      max_x = sensor_x + level_overlap

      # include max_x
      for i in range(min_x, max_x + 1):
        # print(i)
        x_vals.add(i)

  return len(x_vals - objects_at_y)
    
def part_two():
   pass
    
print(part_one(2000000))
print(part_two())

# Template

# def part_one():
    
# def part_two():
#    pass
    
# print(part_one())
# print(part_two())
