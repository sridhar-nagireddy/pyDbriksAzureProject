import argparse


def test_usingArgParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filestogagelocation", type=str, help="A parameter from Databricks")
    args = parser.parse_args()
    param_value = args.filestogagelocation
    assert param_value == "stogrageaccountName"
    print('f passed from databricks is '+{param_value})
    assert 3 == 4
