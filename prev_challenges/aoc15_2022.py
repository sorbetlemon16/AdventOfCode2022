import re

file_data = open('puzzle_inputs/day152022.txt', 'r').readlines()

def get_sensor_beacon_dist():
  data = set()
  for row in file_data:
    # remove non-numbers
    coordinates = re.sub(r'[^1234567890=-]', "", row.strip()).split("=")

    # can't get rid of space in front?
    sensor_x = int(coordinates[1])
    sensor_y = int(coordinates[2])
    beacon_x = int(coordinates[3])
    beacon_y = int(coordinates[4])
    x_dist = abs(sensor_x - beacon_x)
    y_dist = abs(sensor_y - beacon_y)

    total_dist = x_dist + y_dist
    data.add(((sensor_x, sensor_y), (beacon_x, beacon_y), total_dist))

  return data

def occupied_spots_at_row(y):
  x_vals = set()
  objects_at_y = set()
  data = get_sensor_beacon_dist()
  for row in data:
    sensor, beacon, total_dist = row
    sensor_x, sensor_y = sensor
    beacon_x, beacon_y = beacon
    
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
        x_vals.add(i)

  return x_vals - objects_at_y

def part_one():
  return len(occupied_spots_at_row(2000000))

def distance_between(x1, y1, x2, y2):
  return abs(x1 - x2) + abs(y1 - y2)

def find_unreachable(dimension):
  data = get_sensor_beacon_dist()

  x = y = 0
  while y < dimension:
    y += 1
    x = 0
    while x < dimension:
      reachable = False
      # print(y)
      for row in data:
        sensor, beacon, total_dist = row
        sensor_x, sensor_y = sensor
        beacon_x, beacon_y = beacon
        
        x_dist = abs(sensor_x - beacon_x)
        y_dist = abs(sensor_y - beacon_y)

        total_dist = x_dist + y_dist

        distance = distance_between(x, y, sensor_x, sensor_y)
        if distance <= total_dist:
          reachable = True
          corner_dist = total_dist - abs(sensor_y - y)
          # shift right  max amount possible
          x = sensor_x + corner_dist if sensor_x + corner_dist > x + 1 else x + 1
          break
          
      if not reachable:
        return (x, y)

    
def part_two():
  x, y = find_unreachable(4000000)
  print(x, y)
  return x * 4000000 + y
    
print(part_one())
print(part_two())
