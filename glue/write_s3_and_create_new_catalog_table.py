# Read Glue Table from Raw Layer, write to s3 and create a new Glue Catalog Table with that
# Generated from Glue Studio


### Data Catalog option: Create a table in the Data Catalog and on subsequent runs, keep existing schema and add new partitions
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1704803068853 = glueContext.create_dynamic_frame.from_catalog(
    database="raw_db_postgres_newschema",
    table_name="books",
    transformation_ctx="AWSGlueDataCatalog_node1704803068853",
)

# Script generated for node Amazon S3
AmazonS3_node1704803083363 = glueContext.getSink(
    path="s3://dl-staging-full-data-lake-test/postgres/staging_db_postgres_newschema/new_table/",
    connection_type="s3",
    updateBehavior="LOG",
    partitionKeys=[],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1704803083363",
)
AmazonS3_node1704803083363.setCatalogInfo(
    catalogDatabase="staging_db_postgres_newschema", catalogTableName="new_table"
)
AmazonS3_node1704803083363.setFormat("glueparquet")
AmazonS3_node1704803083363.writeFrame(AWSGlueDataCatalog_node1704803068853)
job.commit()





### Data Catalog option: Create a table in the Data Catalog and on subsequent runs, update the schema and add new partitions
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1704803068853 = glueContext.create_dynamic_frame.from_catalog(
    database="raw_db_postgres_newschema",
    table_name="books",
    transformation_ctx="AWSGlueDataCatalog_node1704803068853",
)

# Script generated for node Amazon S3
AmazonS3_node1704803083363 = glueContext.getSink(
    path="s3://dl-staging-full-data-lake-test/postgres/staging_db_postgres_newschema/new_table/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1704803083363",
)
AmazonS3_node1704803083363.setCatalogInfo(
    catalogDatabase="staging_db_postgres_newschema", catalogTableName="new_table"
)
AmazonS3_node1704803083363.setFormat("glueparquet")
AmazonS3_node1704803083363.writeFrame(AWSGlueDataCatalog_node1704803068853)
job.commit()
