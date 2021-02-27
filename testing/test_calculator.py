import sys
import pytest
import yaml

sys.path.append('..')
print(sys.path)
from pythoncode.calculator import Calculator


def get_datas():
    with open("./datas/cacl.yml", "r", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    return (datas['add']['datas'], datas['add']['ids'], datas['add']['divdatas'])


class Testcalcu:
    datas: tuple = get_datas()

    # 前置条件
    def setup_class(self):
        print("开始计算")
        self.calcu = Calculator()

    # 后置条件
    def teardown_class(self):
        print("结束计算")

    # @pytest.mark.search
    # 相加
    @pytest.mark.parametrize("a, b, result", datas[0], ids=datas[1])
    def test_add(self, a, b, result):
        # print(f"a={a},b={b},result={result}")
        assert result == self.calcu.add(a, b)

    def test_add1(self):
        datas = [[1, 1, 2], [100, 400, 300], [1, 0, 1]]
        for data in datas:
            assert data[2] == self.calcu.add(data[0], data[1])

    # @pytest.mark.login
    # todo: 完善相加功能
    # done: 相除功能
    # 相除 提交
    @pytest.mark.parametrize("a,b,result", datas[2], ids=datas[1])
    def test_div(self, a, b, result):
        assert result == self.calcu.div(a, b)
