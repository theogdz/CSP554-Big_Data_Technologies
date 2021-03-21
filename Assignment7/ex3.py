from pyspark.sql.types import *

structfr = StructType(
        [
                StructField("name", StringType(), True),
                StructField("food1",IntegerType(), True),
                StructField("food2",IntegerType(), True),
                StructField("food3",IntegerType(), True),
                StructField("food4",IntegerType(), True),
                StructField("placeid",IntegerType(), True)
        ]
)

structfp = StructType().add("placeid", IntegerType(), True).add("placename",StringType(), True)


foodratingsT = spark.read.schema(structfr).csv('/user/hadoop/foodratings122559.txt')
foodplacesT = spark.read.schema(structfp).csv('/user/hadoop/foodplaces122559.txt')
foodratings_ex3a = spark.sql("SELECT * FROM foodratingsT WHERE food2 < 25 AND food4 > 40")
foodplaces_ex3b = spark.sql("SELECT * FROM foodplacesT WHERE placeid > 3")
