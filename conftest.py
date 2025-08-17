# conftest.py
import pytest


def pytest_addoption(parser):
    parser.addoption("--my-param", action="store", default="default_value", help="My custom parameter")
    parser.addoption("--another-arg", action="store", help="Another argument")


@pytest.fixture
def my_param(request):
    return request.config.getoption("--my-param")


@pytest.fixture
def another_arg(request):
    return request.config.getoption("--another-arg")


