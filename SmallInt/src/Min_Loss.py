input()
#values = input().split()



prices = list(map(int, values))
prices_with_index = {}

min_loss = 100000

for i in range(len(prices)):
    prices_with_index[prices[i]] = i

sorted_keys = sorted(prices_with_index.keys(), reverse=True)

# print(sorted_keys,prices_with_index)

for i in range(len(sorted_keys) - 1):
    if prices_with_index[sorted_keys[i]] < prices_with_index[sorted_keys[i + 1]]:
        diff = sorted_keys[i] - sorted_keys[i + 1]
        if diff < min_loss:
            min_loss = diff

print(min_loss)          