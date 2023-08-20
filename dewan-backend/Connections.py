import mysql.connector
import boto3


class Connections:

        def __init__(self) -> None:
            #db_creds
            self.host = "sql6.freesqldatabase.com"
            self.user = "sql6640892"
            self.password = "STmI1qLAjm"
            self.database = "sql6640892"

            #minio_creds
            self.minio_endpoint = "http://127.0.0.1:9000"
            self.access_key = "UyYPUEK6Cn5HIk7riAbi"
            self.secret_key = "TP8PCfqe4ulX75Xcw2hqv2opiEwEg1eQVf10DSgK"
            self.bucket_name = "softwares"
            self.object_name = "python.exe"

      
      
        def db_connection(self):
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
                )
            
            if connection.is_connected():
                  print("Connected to the database")
                  return connection
            
            
        def minio_connection(self):

                minio_client = boto3.client(
                "s3",
                endpoint_url=self.minio_endpoint,
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key  
                )

                return minio_client
        

        def save_into_minio(self,minio_client,exe_content):
              minio_client.put_object(Bucket=self.bucket_name, Key=self.object_name, Body=exe_content)

        def get_from_minio(self,minio_client):
              return minio_client.get_object(Bucket=self.bucket_name, Key=self.object_name)
        
        def get_presigned_url(self,minio_client):
              return minio_client.generate_presigned_url(
                        "get_object",
                        Params={"Bucket": self.bucket_name, "Key": self.object_name}
                        )
        
    
        
