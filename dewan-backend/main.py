from fastapi import FastAPI
import platform
import requests
import subprocess
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from minio import Minio
import boto3
import mysql.connector

app = FastAPI()

origins = [
    "http://localhost:3000",  # Example frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MinIO configuration
minio_endpoint = "http://127.0.0.1:9000"
access_key = "UyYPUEK6Cn5HIk7riAbi"
secret_key = "TP8PCfqe4ulX75Xcw2hqv2opiEwEg1eQVf10DSgK"
bucket_name = "softwares"
object_name = "python.exe"  # Path to the .exe file on your local system



host = "sql6.freesqldatabase.com"
user = "sql6640892"
password = "STmI1qLAjm"
database = "sql6640892"


connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
)
if connection.is_connected():
        print("Connected to the database")

# Create a MinIO client
minio_client = boto3.client(
    "s3",
    endpoint_url=minio_endpoint,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)

@app.get("/get_versions")
def get_versions():
    python_version = platform.python_version()
    major, minor, micro = python_version.split('.')
    current_version = f"{major}.{minor}.{micro}"
    

    try:
        url = "https://www.python.org/downloads/windows"
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        
        # Find the version information from the page content
        version_start = content.find("Latest Python 3 Release")
        if version_start != -1:
            version_start += len("Latest Python 3 Release")
            version_end = content.find("</strong>", version_start)
            latest_version = content[version_start:version_end].strip()
            index = latest_version.find('</a>')
            before_a = latest_version[:index]
            words = before_a.split()           
            new_version = words.pop(2)
            
        else:
            print("Version information not found")
    except Exception as e:
        return "Error: " + str(e)

    return current_version,new_version

# @app.get("/check_for_latest_version")
# def check_for_latest_version():
#     try:
#         url = "https://www.python.org/downloads/windows"
#         response = requests.get(url)
#         response.raise_for_status()
#         content = response.text
        
#         # Find the version information from the page content
#         version_start = content.find("Latest Python 3 Release")
#         if version_start != -1:
#             version_start += len("Latest Python 3 Release")
#             version_end = content.find("</strong>", version_start)
#             latest_version = content[version_start:version_end].strip()
#             index = latest_version.find('</a>')
#             before_a = latest_version[:index]
#             words = before_a.split()
#             words.pop(0)
#             result = " ".join(words)
#             return result
            
#         else:
#             return "Version information not found"
#     except Exception as e:
#         return "Error: " + str(e)


    
    
@app.get("/store")    
def store_in_s3():
    url = "https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe"
    filename = "python-3.11.4-amd64.exe"

    response = requests.get(url, stream=True)
    exe_content = response.content
    minio_client.put_object(Bucket=bucket_name, Key=object_name, Body=exe_content)
    print(f"{filename} has been downloaded successfully.")

@app.get("/install")    
def install():
    response = minio_client.get_object(Bucket=bucket_name, Key=object_name)
    exe_content = response["Body"].read()
    

    print("Sample data inserted")

    local_file_path = "downloaded_python.exe"
    with open(local_file_path, "wb") as local_file:
        local_file.write(exe_content)

    subprocess.run([local_file_path], shell=True)

    presigned_url = minio_client.generate_presigned_url(
    "get_object",
    Params={"Bucket": bucket_name, "Key": object_name}
    )

    data = ("Python",presigned_url)

    cursor = connection.cursor()
    insert_query = "INSERT INTO Softwares(SNO,SOFTWARE,LOCATION) VALUES (1,%s,%s)"
    try:
        cursor.execute(insert_query,data)
        connection.commit()

    except:
        return "Value already installed"

    






    
