import os
import shutil
import subprocess
import requests

# Constants
DOCKERFILE_URL = 'https://raw.githubusercontent.com/Xoro-1337/libxenon-docker/main/Dockerfile'


def download_dockerfile():
    print('Downloading the Dockerfile...')
    response = requests.get(DOCKERFILE_URL)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the Dockerfile to the local file
        with open('Dockerfile', 'wb') as f:
            f.write(response.content)
        print('Dockerfile has been successfully downloaded.')
    else:
        print(f'Failed to download the Dockerfile. Status code: {response.status_code}')


def build_libxenon_image():
    build_command = ['docker', 'build', '-t', 'libxenon', '.']

    print('Building the libxenon image. This may take some time...')
    try:
        subprocess.run(build_command, check=True)
        print('Libxenon image has been built successfully.')
    except subprocess.CalledProcessError as e:
        print(f'Failed to build libxenon image. Error: {e}')


def is_docker_installed():
    return shutil.which('docker') is not None


def check_dockerfile_in_cwd():
    # Get the current working directory
    current_directory = os.getcwd()

    # Check if a Dockerfile exists in the current directory
    dockerfile_path = os.path.join(current_directory, "Dockerfile")
    if os.path.isfile(dockerfile_path):
        return True
    else:
        return False


def run_docker():
    cmd = f'docker run -ti -v "{os.getcwd()}:/mnt/share" libxenon:latest /bin/sh -c "su - libxenon"'
    return cmd


if __name__ == "__main__":
    if not is_docker_installed():
        print('Docker is either not installed or is not in your PATH. Please correct this before continuing.')
        exit(1)
    if not check_dockerfile_in_cwd():
        download_dockerfile()
    build_libxenon_image()
    os.system(run_docker())
