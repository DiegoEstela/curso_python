first_list = [1, 2, 3]
second_list = [4, 5, 6]

""" extend """
first_list.extend(second_list)
print(first_list)

""" insert """
first_list.insert(0, 0)
print(first_list)

n = len(first_list)
first_list.insert(n, 7)
print(first_list)

""" reverse """
first_list.reverse()
print(first_list)

""" sort """
my_unordered_list = [3, 5, 1, 10, 4, 7, 9, 6, 2]
my_unordered_list.sort()
print(my_unordered_list)

my_unordered_list.sort(reverse=True)
print(my_unordered_list)
