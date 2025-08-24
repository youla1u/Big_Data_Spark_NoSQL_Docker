"""SimpleProg.py"""
from pyspark.sql import SparkSession

myFile = "data/tpSparkPython.html"
spark = SparkSession.builder.appName("SimpleProg").getOrCreate()
myData = spark.read.text(myFile).cache()

nbsql = myData.filter(myData.value.contains("sql")).count()
nbspark = myData.filter(myData.value.contains("spark")).count()

print("Lignes avec spark : %i, lignes avec sql : %i" % (nbspark, nbsql))

spark.stop()