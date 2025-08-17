
import pytest
import os
import sys

print(f'Hi, PyCharm - Running tests')  # Press Ctrl+F8 to toggle the breakpoint.

#Run all tests in the repository root folder.
dir=os.path.dirname(os.path.realpath('__file__'))
os.chdir(dir)

# Skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

pytest_args  = [".",  # indicates the directory which needs to be ran
                "-rp",
                "no:cacheprovider",
                "-v",
                # "--html=reports/sri_report.html", # report generation
                # "--html=reports/sri_self_contained_report.html --self-contained-html"
                ]
ret_code=pytest.main(pytest_args)

assert ret_code==0, "Pytest failed"