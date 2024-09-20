import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from awsglue.context import GlueContext
from awsglue.job import Job

%%configure -f
{
    "datalake-formats": "iceberg",
    "--conf": "spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions --conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog --conf spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog --conf spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO --conf spark.sql.catalog.glue_catalog.warehouse=s3://<bucket_name>/notebook/iceberg_tests/",
    '--enable-glue-datacatalog': True
}

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
dyf = glueContext.create_dynamic_frame.from_catalog(database='<source_db>', table_name='<source_table>')
dyf.printSchema()
df = dyf.toDF()
df.show(3)
iceberg_db = "iceberg_test"
iceberg_table = "notebook_iceberg_ml_pred_table_sql"

tmp_spark_table = "tmp_predictions"
df.createOrReplaceTempView("tmp_predictions")

# WORKED
query = f"""
CREATE TABLE glue_catalog.{iceberg_db}.{iceberg_table}
USING iceberg
PARTITIONED BY (ingested_date)
TBLPROPERTIES ("format-version"="2")
AS SELECT is_core, document_id, ingested_date FROM {tmp_spark_table}
"""
spark.sql(query)
job.commit()
