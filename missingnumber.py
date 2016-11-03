data_list = [-5, -23, 5, 0, 23, -6, 23, 67]

new_list = []

minimum = data_list[0]

for x in data_list:
  if x < minimum and x>=0:
    minimum = x
    new_list.append(minimum)
    print new_list