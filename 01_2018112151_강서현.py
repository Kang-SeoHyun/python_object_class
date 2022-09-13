num_list = list(map(int, input().split()))

num_list = sorted(set(num_list), reverse = True)

print(num_list)