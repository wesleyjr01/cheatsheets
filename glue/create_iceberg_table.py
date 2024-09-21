from pyspark.sql.session import SparkSession
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import *


# Env Vars
iceberg_db = "<iceberg_db>"
iceberg_table = "<iceberg_table>"
destination_s3_path = "s3://<bucketname>/iceberg"
partition_by = "ingested_date"
source_db = "<source_db>"
source_table = "<source_table>"

# Spark Session
spark = (
    SparkSession.builder.config(
        "spark.sql.extensions",
        "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
    )
    .config("spark.sql.catalog.glue_catalog", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.glue_catalog.warehouse", destination_s3_path)
    .config(
        "spark.sql.catalog.glue_catalog.catalog-impl",
        "org.apache.iceberg.aws.glue.GlueCatalog",
    )
    .config(
        "spark.sql.catalog.glue_catalog.io-impl", "org.apache.iceberg.aws.s3.S3FileIO"
    )
    .getOrCreate()
)
# Add KMS Information to Write to S3 KMS Encrypted Buckets
spark._jsc.hadoopConfiguration().set("fs.s3.enableServerSideEncryption", "true")

# Glue Context
glueContext = GlueContext(spark)
job = Job(glueContext)
# job.init(args["job_name"], args)


# Import Source data
dyf = glueContext.create_dynamic_frame.from_catalog(
    database=source_db, table_name=source_table
)
df = dyf.toDF()


# Create Iceberg Table
tmp_spark_table = "tmp_table"
df.createOrReplaceTempView("tmp_table")
query = f"""
CREATE TABLE glue_catalog.{iceberg_db}.{iceberg_table}
USING iceberg
PARTITIONED BY ({partition_by})
TBLPROPERTIES ("format-version"="2")
AS SELECT * FROM {tmp_spark_table}
"""
spark.sql(query)
job.commit()

