from pyspark.sql.types import *
struct1 = StructType(
        [
                StructField("name", StringType(), True),
                StructField("food1",IntegerType(), True),
                StructField("food2",IntegerType(), True),
                StructField("food3",IntegerType(), True),
                StructField("food4",IntegerType(), True),
                StructField("placeid",IntegerType(), True)
        ]
)
foodratings = spark.read.schema(struct1).csv('/user/hadoop/foodratings122559.txt')