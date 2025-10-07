import json, argparse, time
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp, lit

parser = argparse.ArgumentParser()
parser.add_argument("--config", required=True, help="path to JSON config")
args = parser.parse_args()

with open(args.config, "r") as f:
    cfg = json.load(f)

spark = SparkSession.builder.appName("stream_to_delta_demo").getOrCreate()

# NOTE: For local demo, we mock a small static DataFrame instead of Kafka
df = spark.createDataFrame(
    [("https://example.com/", "text/html", "<html>Hello</html>")],
    ["url", "content_type", "html"]
).withColumn("ingest_ts", current_timestamp())

outpath = cfg["storage"]["delta_base"] + "/bronze_raw_web"
(df
 .withColumn("source", lit("mock"))
 .write.mode("overwrite")
 .format("delta")
 .save(outpath)
)

print(f"Wrote mock bronze table to {outpath}")
time.sleep(1)
