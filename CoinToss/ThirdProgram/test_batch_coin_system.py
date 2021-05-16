import batch_coin_toss

batch_size = 6
repeat_count = batch_size * 10000000
balanced_head_count = batch_size / 2
balanced_count = 0

for i in range(repeat_count):
    head_count = batch_coin_toss.batch_toss_coins(batch_size)
    if(head_count == balanced_head_count):
        balanced_count = balanced_count + 1


percentage_balanced_sets = balanced_count/repeat_count
print('Our balanced set count was', balanced_count, 
'out of', repeat_count, 'total batches')
print(f'We flipped a balanecd set, {100*percentage_balanced_sets: 0.2f}% of the time')