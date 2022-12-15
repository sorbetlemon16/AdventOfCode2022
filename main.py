import re

file_data = open('puzzle_inputs/day152022.txt', 'r').readlines()

def part_one():
  sensor_beacon_pairs = set()
  sensors = set()
  beacons = set()
 
  covered = set()
  for row in file_data:
    # print(row, end="")
    # remove non-numbers
    coordinates = re.split(r'\D+',row.strip())

    # can't get rid of space in front?
    _, sensor_x, sensor_y, beacon_x, beacon_y = coordinates
    sensor = (int(sensor_x), int(sensor_y))
    beacon = (int(beacon_x), int(beacon_y))
    sensors.add(sensor)
    beacons.add(beacon)
    sensor_beacon_pairs.add((sensor, beacon))

  for pair in sensor_beacon_pairs:
    sensor, beacon = pair
    sensor_x = int(sensor[0])
    sensor_y = int(sensor[1])
    beacon_x = int(beacon[0])
    beacon_y = int(beacon[1])
    x_dist = abs(sensor_x - beacon_x)
    y_dist = abs(sensor_y - beacon_y)

    total_dist = x_dist + y_dist
    # start at furthest edges, then go in
    print("pair", total_dist)
    for dist_from_center in range(total_dist, -1, -1):
      print(dist_from_center)
      # print("distance from center ", dist_from_center)
      # at furthest edge, need for most iteration - less iteration as you go 
      # inwards because dimensions decrease 

      # +1 to include value of distance_from_center 
      for i in range(dist_from_center + 1):
        # values from i represent the incremental staircasing

        # offset represents how much to bring it closer to the center
        offset = total_dist - dist_from_center

        # TOP RIGHT
        covered.add((sensor_x + total_dist - offset - i, sensor_y + i))
        # TOP LEFT 
        covered.add((sensor_x - total_dist + offset + i, sensor_y + i))
        # BOTTOM LEFT 
        covered.add((sensor_x - total_dist + offset + i, sensor_y - i))
        # BOTTOM RIGHT
        covered.add((sensor_x + total_dist - offset - i, sensor_y - i))
  
  num_covered = 0
  for coordinates in covered - sensors - beacons: 

    if coordinates[1] == 10:
      print(coordinates)
      num_covered += 1
      
  return num_covered
    
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
