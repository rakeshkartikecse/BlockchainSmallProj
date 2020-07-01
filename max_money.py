
#python program to calculate how much total bitcoin will be issued

start_block_reward=50
reward_interval=210000
def max_money():
   current_reward=50*10**8 #50 btc=50000000 Satoshi
   total=0
   while current_reward>0:
        total=total+reward_interval *current_reward
        current_reward /=2
   return total
print("Total BTC to ever be created:", max_money(), "Satoshi")
