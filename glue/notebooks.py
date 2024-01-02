# 1st Isolated cell, import Delta
%%configure -f
{
    "datalake-formats": "delta"
}

# 2nd Cell Import Parameters
%idle_timeout 60
%glue_version 4.0
%worker_type G.1X
%number_of_workers 2

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import delta
  
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
