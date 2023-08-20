import requests

url = "https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe"
filename = "python-3.11.4-amd64.exe"

response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(filename, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"{filename} has been downloaded successfully.")
else:
    print(f"Failed to download {filename}. Status code: {response.status_code}")


    import subprocess

executable_path = "C:\Users\Nikhil Pai\Desktop\React\Dewan\dewan-backend\python-3.11.4-amd64.exe"

try:
    subprocess.run([executable_path])  # Open the executable
except Exception as e:
    print(f"Failed to open {executable_path}: {e}")
