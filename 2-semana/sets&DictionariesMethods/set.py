""" copy """
set1 = {1, 2, 3, 4}
set2 = set1.copy()
print(set2)

""" isdisjoint """
is_dis_joint = set1.isdisjoint({4, 5, 6})
print(is_dis_joint)

""" issubset """
print(set1.issubset(set2))

""" issuperset """
print(set1.issuperset(set2))

""" union """
print(set1.union({4, 5, 6}))

""" difference """
print(set1.difference({4, 5, 6}))

""" difference_update """
set1.difference_update({4, 5, 6})
print(set1)

""" intersection """
set3 = set1.intersection({2, 3, 4, 5, 6})
print(set3)
