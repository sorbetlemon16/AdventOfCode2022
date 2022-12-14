file_data = open('../puzzle_inputs/day22022.txt', 'r').read().split('\n')

# Solution with linear runtime and constant space
def part_one():
  total_score = 0
  for row in file_data:
    opp_choice, your_choice = row.split()
    score_dict = {'X': 1, 'Y': 2, 'Z': 3}
    round_score = score_dict[your_choice]

    # A: rock, B: paper, C: scissors for opp
    # X: rock, Y: paper, Z: scissors for you
    your_win_dict = {'X': 'C', 'Y': 'A', 'Z': 'B'}
    your_draw_dict = {'X': 'A', 'Y': 'B', 'Z': 'C'}

    if your_win_dict[your_choice] == opp_choice:
      round_score += 6
    elif your_draw_dict[your_choice] == opp_choice:
      round_score += 3
    
    total_score += round_score
  return total_score
    

# Solution with linear runtime and constant space
def part_two():
  total_score = 0
  for row in file_data:
    opp_choice, outcome = row.split()
    outcome_score = {'X': 0, 'Y': 3, 'Z': 6}
    round_score = outcome_score[outcome]

    # A: rock, B: paper, C: scissors for opp
    # dictionary displaying what play_score (rock: 1, paper: 2, scissors: 3) 
    # you get to get the winning condition given the opponent's play
    win_dict = {'A': 2, 'B': 3, 'C': 1}
    draw_dict = {'A': 1, 'B': 2, 'C': 3}
    lose_dict = {'A': 3, 'B': 1, 'C': 2}

    
    if round_score == 6:
      round_score += win_dict[opp_choice]
    elif round_score == 3:
      round_score += draw_dict[opp_choice]
    else:
      round_score += lose_dict[opp_choice]
    
    total_score += round_score
  return total_score

print(part_one())
print(part_two())