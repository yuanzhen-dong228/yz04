# 计算器相加
def add(a, b):
    return a + b


def div(a, b):
    try:
        a / b
    except:
        print('分母不能为零')
    return a / b


# pytest 测试用例
def test_add():
    assert 2 == add(1, 1)


def test_div():
    assert 2 == div(4, 0)
