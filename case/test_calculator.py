import pytest

# from case.conftest import get_case_data
from case.conftest import get_case_data
from src.caculator import caculator
import pytest
import allure

@allure.feature("测试计算类")
class TestCaculator():
    def setup_class(self):
        self.cal = caculator()

    @allure.story("测试计算类的减法")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,exc_data',get_case_data()[1])
    def test_minus(self,a,b,exc_data):
        print("减法")
        assert self.cal.minus(a, b) == exc_data

    @allure.story("测试计算类的乘法")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,exc_data',get_case_data()[2])
    def test_multipy(self,a,b,exc_data):
        print("乘法")
        assert self.cal.multipy(a, b) == exc_data

    @allure.story("测试计算类的除法")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,exc_data',get_case_data()[3])
    def test_devide(self,a,b,exc_data):
        print("除法")
        assert self.cal.devide(a, b) == exc_data

    @allure.story("测试计算类的加法")
    @pytest.mark.run(order=1)
    @pytest.mark.usefixtures("cal_begin_end")
    @pytest.mark.parametrize('a,b,exc_data',get_case_data()[0])
    def test_add(self,a,b,exc_data):
        print("加法")
        assert self.cal.add(a,b)==exc_data
