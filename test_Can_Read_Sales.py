# import pytest
# from pyspark.sql import SparkSession
#
#
# @pytest.fixture(scope='session')
# def spark():
#     return SparkSession.builder \
#         .appName('sri_test_session').getOrCreate()
#
#
# @pytest.mark.sales
# def test_read_csv_into_dataframe(spark: SparkSession, tmp_path):
#     dataframe_sales = spark.read.format("csv").option("header", "true") \
#         .option("inferSchema", "true") \
#         .load("abfss://srisource@saforsriasdatalake.dfs.core.windows.net/Sales.csv")
#     # Perform assertions on the DataFrame
#     # assert dataframe_sales.count() == 2
#     assert "Item_Identifier" in dataframe_sales.columns
#     assert "Item_Outlet_Sales" in dataframe_sales.columns
# # .load("C:/Users/sridh/Downloads/Sales_short.csv")
