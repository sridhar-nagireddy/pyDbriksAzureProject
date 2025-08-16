import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope='session')
def spark():
    return SparkSession.builder \
        .appName('sri_test_session').getOrCreate()


@pytest.mark.sales
def test_read_csv_into_dataframe(spark: SparkSession, tmp_path):
    spark.conf.set("fs.azure.account.auth.type.saforsriasdatalake.dfs.core.windows.net", "OAuth")
    spark.conf.set("fs.azure.account.oauth.provider.type.saforsriasdatalake.dfs.core.windows.net",
                   "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
    spark.conf.set("fs.azure.account.oauth2.client.id.saforsriasdatalake.dfs.core.windows.net",
                   "70a191e3-11b2-4fb0-8744-4287c900dc0f")
    spark.conf.set("fs.azure.account.oauth2.client.secret.saforsriasdatalake.dfs.core.windows.net",
                   "3ry8Q~doCOvWOWWaiypA8tneEh1TImfJ1QBLmcTu")
    spark.conf.set("fs.azure.account.oauth2.client.endpoint.saforsriasdatalake.dfs.core.windows.net",
                   "https://login.microsoftonline.com/b3e00778-196a-4f63-8fcc-6d2eebbbcf14/oauth2/token")

    dataframe_sales = spark.read.format("csv").option("header", "true") \
        .option("inferSchema", "true") \
        .load("abfss://srisource@saforsriasdatalake.dfs.core.windows.net/Sales.csv")
    # Perform assertions on the DataFrame
    assert dataframe_sales.count() == 2
    assert "Item_Identifier" in dataframe_sales.columns
    assert "Item_Outlet_Sales" in dataframe_sales.columns
    assert "value" in dataframe_sales.columns
# .load("C:/Users/sridh/Downloads/Sales_short.csv")
