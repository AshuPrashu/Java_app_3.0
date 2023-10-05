import requests

def upload_jar_to_artifactory(repo_url, jar_file_path, username, password):
    upload_url = f"{repo_url}/{jar_file_path}"
    
    # Read the JAR file
    with open(jar_file_path, 'rb') as jar_file:
        jar_content = jar_file.read()

    # Set the headers for the POST request
    headers = {
        'Content-Type': 'application/java-archive',
    }

    # Send the POST request to upload the JAR file
    response = requests.put(upload_url, data=jar_content, auth=(username, password), headers=headers)

    # Check the response status
    if response.status_code == 201:
        print('JAR file uploaded successfully.')
    else:
        print(f'Failed to upload JAR file. Status code: {response.status_code}')
        print(f'Response content: {response.text}')


# Replace with your Artifactory repository URL, JAR file path, username, and password
repository_url = 'http://52.53.218.227:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
jar_file_path = 'example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
username = 'admin'
password = 'Password@123'
# Upload the JAR file to the Artifactory repository
#upload_jar_to_artifactory(repository_url, jar_file_path, username, password)
