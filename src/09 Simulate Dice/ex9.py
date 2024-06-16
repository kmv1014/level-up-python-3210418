import random

def roll_dice(*args):
  dice_sum = []
  mc_steps = 1000000
  trial = mc_steps
  while trial > 0:
    roll_sum = 0
    for n in args:
      roll = random.randint(1,n)
      roll_sum = roll_sum + roll
    dice_sum.append(roll_sum)
    trial -=1
  no_dice = len(args)
  args_list = list(args)
  max_sum = sum(args_list)
  roll_wise_per = {}
  for i in range(no_dice,max_sum+1):
    sum_n=0
    for n in dice_sum:
      if (n==i):
        sum_n +=1
    roll_wise_per[i] = sum_n/mc_steps
  print("OUTCOME PROBABILITY")
  for rollsum in roll_wise_per.keys():
    print(f"{rollsum} {round(roll_wise_per[rollsum]*100,2)}%")

roll_dice(4,6,6)