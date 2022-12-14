file_data = open('puzzle_inputs/day112022.txt', 'r').readlines()

def get_monkey_dict():
  monkeys = []

  for i in range(0, len(file_data), 7):    
    items = file_data[i + 1].strip("Starting items: \n").split(",")
    operation = file_data[i + 2][23]
    value = file_data[i + 2].split()[-1]
    divisible_by = int(file_data[i + 3].split()[-1])
    if_true = int(file_data[i + 4].split()[-1])
    if_false = int(file_data[i + 5].split()[-1])
  
    monkey_dict = {"items" : items, 
                  "operation": operation,
                  "value": value,
                  "divisible_by": divisible_by,
                  "if_true": if_true,
                  "if_false": if_false,
                  "frequency": 0}
  
    monkeys.append(monkey_dict)

  return monkeys

def model_monkey_behavior(num_rounds, worry):
  num_monkeys = round(len(file_data) / 7)
  monkey_inspection_frequency = [ 0 for x in range(num_monkeys)]
  monkey_cargo = [ [] for x in range(num_monkeys) ]
  monkeys = get_monkey_dict()

  modulo = 1
  for monkey in monkeys:
    modulo = modulo * monkey["divisible_by"]

  for t in range(num_rounds):
    for monkey in monkeys:
  
      monkey["frequency"] += len(monkey["items"])
      for item in monkey["items"]:
        value = monkey["value"]
        
        if value.isalpha():
          value = int(item)
        
        if monkey["operation"] == "*":
          value = int(int(item) * int(value) / worry)
        elif monkey["operation"] == "+":
          value = int((int(item) + int(value)) / worry)

        value = int(value) % modulo

        if value % monkey["divisible_by"] == 0:
          throw_to = monkey["if_true"]
        else:
          throw_to = monkey["if_false"]
  
        monkeys[throw_to]["items"].append(value)
      # reset to empty
      monkey["items"] = []

  return monkeys

def find_top_two(monkeys):
  all_freqs = []
  for monkey in monkeys:
    all_freqs.append(monkey["frequency"])

  all_freqs.sort()
  return all_freqs[-1] * all_freqs[-2]  
  
def part_one():
  monkeys = model_monkey_behavior(20, 3)
  return find_top_two(monkeys)

def part_two():
  monkeys = model_monkey_behavior(10000, 1)
  return find_top_two(monkeys)
    
print(part_one())
print(part_two())
