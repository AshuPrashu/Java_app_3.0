import requests
import subprocess

def jfrogupload():
    # Define the URL, file path and authentication credentials
    url = "http://13.52.251.141:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"
    file_path = "/var/lib/jenkins/workspace/job1/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"
    username = 'admin'
    password = 'Password123'
    
    #send the PUT request with authentication and file upload
    with open(file_path, 'rb') as file:
        response = requests.put(url, auth=(username, password), data=file)
        
    #check the response status code
    if response.status_code == 201:
        print("\nPUT request was sucessful!")
    else:
        print(f"PUT request failed with status code {response.status_code}")
        print("Response content:")
        print("response.text")
        
def main():
    jfrogupload()
