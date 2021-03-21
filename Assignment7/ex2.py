from pyspark.sql.types import *

struct2 = StructType().add("placeid", IntegerType(), True).add("placename",StringType(), True)
foodplaces = spark.read.schema(struct2).csv('/user/hadoop/foodplaces122559.txt')
