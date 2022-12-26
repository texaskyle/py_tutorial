clothes = {"jacket", "shorts", "vest", "inner wear"}
utensils = {"serving spoon", "dishes", "sufuria"}
house_hold_items = clothes.union(utensils)
clothes.add("trousers")
# print(house_hold_items.difference(clothes))
print(house_hold_items.intersection(clothes))


# for x in house_hold_items:
# print(x)