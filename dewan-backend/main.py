from fastapi import FastAPI
import platform
import subprocess
from fastapi.middleware.cors import CORSMiddleware
import util
import requests
import constants

from Connections import Connections

app = FastAPI()

origins = [
    constants.FRONTEND_URL,  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


connection = Connections()

db_connection = connection.db_connection()

minio_client = connection.minio_connection()



@app.get("/get_versions")
def get_versions():
    python_version = platform.python_version()
    major, minor, micro = python_version.split('.')
    current_version = f"{major}.{minor}.{micro}"
    
    new_version = util.get_version_info()

    return current_version,new_version

    
@app.get("/store")    
def store_in_s3():
    url = constants.SOFTWARE_URL
    filename = constants.FILE_NAME

    response = requests.get(url, stream=True)
    exe_content = response.content

    connection.save_into_minio(minio_client,exe_content)
    print(f"{filename} has been downloaded successfully.")

@app.get("/install")    
def install():
    response = connection.get_from_minio(minio_client)
    exe_content = response["Body"].read()

    print("Sample data inserted")

    local_file_path = constants.LOCAL_FILE_PATH

    with open(local_file_path, "wb") as local_file:
        local_file.write(exe_content)

    subprocess.run([local_file_path], shell=True)

    presigned_url = connection.get_presigned_url(minio_client)

    insert_data = (constants.SOFTWARE_NAME,presigned_url)

    cursor = db_connection.cursor()
    insert_query = constants.INSERT_QUERY
    try:
        cursor.execute(insert_query,insert_data)
        db_connection.commit()

    except:
        return "Value already installed"

    






    
