#list_ = [-5, 2, 8, -1, 0, 10]
#dodatnie = list(filter(lambda x: x > 0, list_))
dodatnie_w_kwadrate = list(map(lambda y: y**2, filter(lambda x: x > 0, [-5, 2, 8, -1, 0, 10])))

#print(dodatnie)
print(dodatnie_w_kwadrate)