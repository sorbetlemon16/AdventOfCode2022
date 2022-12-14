file_data = open('../puzzle_inputs/day12021.txt', 'r').read().split('\n')

data = []
for num in file_data:
  data.append(int(num))
  
def day_one_p1():
  num_incr = 0
  for i in range(len(data) - 1):
    
    if int(data[i + 1]) > int(data[i]):
      num_incr += 1 
  
  return num_incr

def day_one_p2():
  window_incr = 0
  for i in range(len(data) - 3):

    # current_window_sum = data[i] +  data[i + 1] + data[i + 2]
    # next_window_sum = data[i + 1] + data[i + 2] + data[i + 3]
    # if next_window_sum > current_window_sum: 
    #   window_incr += 1 

    # simpler but harder to read way: 
    if data[i + 3] > data[i]: 
      window_incr += 1 

  return window_incr

day_one_p1()
