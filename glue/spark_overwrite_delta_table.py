import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from awsglue.context import GlueContext
from awsglue.job import Job
import delta

  
sc = (
        SparkSession.builder.config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
        # Config to allow Spark to read/write dates from parquet correctly after version Spark 3.0, details in SPARK-31404
        .config("spark.sql.legacy.parquet.datetimeRebaseModeInRead", "CORRECTED")
        .config("spark.sql.legacy.parquet.datetimeRebaseModeInWrite", "CORRECTED")
        .config("spark.sql.legacy.parquet.int96RebaseModeInRead", "CORRECTED")
        .config("spark.sql.legacy.parquet.int96RebaseModeInWrite", "CORRECTED")
        .config("spark.sql.avro.datetimeRebaseModeInWrite", "CORRECTED")
        .config("spark.sql.avro.datetimeRebaseModeInRead", "CORRECTED")
        .config("spark.databricks.delta.fixSchema.GlueCatalog", "true")
        .getOrCreate()
    )
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
# Read Delta Table as Dynamic Frame
old_delta_table_path = "s3://dl-staging-full-data-lake-test/postgres/staging_db_postgres_newschema/addr/"
database="staging_db_postgres_newschema"
dyf = glueContext.create_data_frame.from_catalog(
    database=database,
    table_name="addr",
    additional_options={
        "path": old_delta_table_path
    }
)

dyf.printSchema()
dyf.show(5)
# Convert Dynamic frame to PySpark DF
df = dyf.toDF(*dyf.columns)

df.show(5)
# Write PySpark df as new delta table - BROKEN
new_table_name = "new_addr_three"
database="staging_db_postgres_newschema"
df.coalesce(1).write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable(f"{database}.{new_table_name}")
    # .options(**additional_options) \
job.commit()
