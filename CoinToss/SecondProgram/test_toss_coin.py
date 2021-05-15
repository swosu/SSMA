import tossSingleCoin

heads_count = 0
total_flips = 1000

for i in range(total_flips):
    print(i, end='')
    heads = tossSingleCoin.toss_coin()
    if heads:
        heads_count = heads_count + 1

print('Our heads count was', heads_count, 'out of', total_flips, 'total flips')
