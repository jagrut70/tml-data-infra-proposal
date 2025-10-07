from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, col, lit

spark = SparkSession.builder.appName("merge_dedup_example").getOrCreate()

bronze = spark.createDataFrame(
    [("id1","Hello world"),("id2","Hello  world")], ["doc_id","text"]
).withColumn("norm_text", col("text"))

with_hash = bronze.withColumn("content_hash", sha2(col("norm_text"), 256))

# In real Delta MERGE, you'd merge into a target table on content_hash to dedup.
with_hash.show(truncate=False)
