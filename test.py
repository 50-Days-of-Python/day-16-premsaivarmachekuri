import main;

def test():
    assert main.sum_list([[21, 2, 13], [14, 51, 6], [27, 81, 9]]) == 224
def test2():
    assert main.sum_list([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]) == 120
def test3():
    assert main.sum_list([[1, 12, 30], [ 10, 21, 12], [35, 14, 15, 63, 17, 18]]) == 248
