from minio import Minio
import boto3

# MinIO configuration
minio_endpoint = "http://127.0.0.1:9000"
access_key = "UyYPUEK6Cn5HIk7riAbi"
secret_key = "TP8PCfqe4ulX75Xcw2hqv2opiEwEg1eQVf10DSgK"
bucket_name = "softwares"
file_path = "C:\python-3.11.4-amd64.exe"  # Path to the .exe file on your local system

# Create a MinIO client
minio_client = boto3.client(
    "s3",
    endpoint_url=minio_endpoint,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)
response = minio_client.list_buckets()

try:
    # Upload the .exe file to the bucket
    minio_client.upload_file(file_path,bucket_name,"example.exe")

    print(f"File {file_path} uploaded successfully.")

except:
    print(f"Error")

