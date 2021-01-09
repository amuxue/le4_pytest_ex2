import pytest
import yaml
# from test_pytest.pythoncode.calculator import Calculator
import os

# 通过 os.path.dirname 获取当前文件所在目录的路径
yaml_file_path = os.path.dirname(__file__) + "/data.yml"
def get_case_data():
    with open(yaml_file_path,encoding='utf-8') as f:
        data=yaml.safe_load(f)
        return [data["add"],data["minus"],data["multipy"],data["devide"]]



@pytest.fixture(scope="module")
def cal_begin_end():
    print("开始计算")
    yield
    print("结束计算")