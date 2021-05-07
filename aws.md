# Boto3

## Boto3 Clients

### Boto3 Client for s3
```python
s3 = boto3.resource('s3',
                   region_name="us-west-2",
                   aws_access_key_id=KEY,
                   aws_secret_access_key=SECRET)
```

### Boto3 Client for ec2
```python
ec2 = boto3.resource('ec2',
                    region_name="us-west-2",
                    aws_access_key_id=KEY,
                    aws_secret_access_key=SECRET)
```

### Boto3 Client for iam
```python
iam = boto3.client('iam',
                   region_name="us-west-2",
                   aws_access_key_id=KEY,
                   aws_secret_access_key=SECRET)
```

### Boto3 Client for redshift
```python
redshift = boto3.client('redshift',
                   region_name="us-west-2",
                   aws_access_key_id=KEY,
                   aws_secret_access_key=SECRET)
```

---


## Boto3 List s3 Buckets
```python
for bucket in s3.buckets.all():
    print(bucket.name)
```

## Filter Objects from a Path in a Bucket
```python
bucket = s3.Bucket('bucket-name')
for obj in bucket.objects.filter(Prefix='prefix/A/B/C'):
    print('{0}'.format(obj.key))
```

## Retrieve JSON Object File from s3 Bucket
```python
object_ = s3.Object('bucket-name','file-path')
file_content = object_.get()["Body"].read()
dictionary = json.loads(file_content)

# example
object_ = s3.Object('udacity-dend','song_data/A/A/A/TRAAAAK128F9318786.json')
```

## Retrieve JSON-Lines Object File from s3 Bucket
```python
import io
import jsonlines

# s3.Object('bucket-name','file-path')
object_ = s3.Object('udacity-dend','log_data/2018/11/2018-11-30-events.json')

file_content = object_.get()["Body"].read()

fp = io.BytesIO(file_content)
list_of_json_files = [json_ for json_ in jsonlines.Reader(fp)]
```
