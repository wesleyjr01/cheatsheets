provider "aws" {
  region = "your-region"
}

resource "aws_s3_bucket" "mwaa_bucket" {
  bucket = "your-mwaa-bucket"
  acl    = "private"
}

# Assuming the bucket already exists, you can use data source to reference it
data "aws_s3_bucket" "existing_bucket" {
  bucket = "your-mwaa-bucket"
}

resource "aws_s3_bucket_object" "dag_files" {
  for_each = fileset("${path.module}/dags", "*.py")

  bucket = data.aws_s3_bucket.existing_bucket.bucket
  key    = each.value
  source = "${path.module}/dags/${each.value}"
}
