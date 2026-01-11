def move_zeros(lst):
    new_lst = [x for x in lst if x != 0]
    for i in range(lst.count(0)):
        new_lst.append(0)
    return new_lst


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))




