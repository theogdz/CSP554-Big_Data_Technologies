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


foodratings = spark.read.schema(structfr).csv('/user/hadoop/foodratings122559.txt')
foodplaces = spark.read.schema(structfp).csv('/user/hadoop/foodplaces122559.txt')

ex6 = foodratings.join(foodplaces, foodratings.placeid == foodplaces.placeid, 'inner')
