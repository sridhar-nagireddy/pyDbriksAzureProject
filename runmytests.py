
import pytest
import os
import sys

print(f'Hi, PyCharm - Running tests')  # Press Ctrl+F8 to toggle the breakpoint.




#Run all tests in the repository root folder.
dir=os.path.dirname(os.path.realpath('__file__'))
os.chdir(dir)

# Skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

ret_code=pytest.main([".", "-p", "no:cacheprovider","-v"])

assert ret_code==0, "Pytest failed"