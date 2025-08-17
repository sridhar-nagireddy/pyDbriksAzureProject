# conftest.py
import pytest
# from pyspark.sql import SparkSession
#
#
# @pytest.fixture(scope='session')
# def spark():
#     return SparkSession.builder \
#         .appName('sri_test_session').getOrCreate()
#
def pytest_addoption(parser):
    print(f'is this pyTest Entry point?"')
    parser.addoption("--param1", action="store", default="defVal_param1", help="My custom parameter")
    parser.addoption("--param2", action="store", default="defVal_param2")
    parser.addoption("--filestogagelocation",action="store",default="defVal_filestoreloc")


@pytest.fixture
def my_param1(request):
    return request.config.getoption("--param1")
@pytest.fixture
def my_param2(request):
    return request.config.getoption("--param2")

pytest.fixture
def my_filestoreLoc(request):
    return request.config.getoption("--filestogagelocation")
