import requests

def get_version_info():
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
            return new_version
            
        else:
            print("Version information not found")
    except Exception as e:
        return "Error: " + str(e)