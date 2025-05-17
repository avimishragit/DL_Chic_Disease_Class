import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "CNN-Image-Classification_v1.0"

# List of files and directories to create
list_of_files = [
    ".github/workflows/.gitkeep",#for GitHub Actions
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "setup.py",
    "requirements.txt",
    "research/trials.ipynb",
    "templates/index.html"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        # Create directories if they don't exist
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for the file: {file_name}")
        
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        # Create the file if it doesn't exist or is empty
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Creating empty file: {file_path}")
            
    else:
        # If the file already exists and is not empty, log a message
        logging.info(f"File {file_name} already exists: {file_path}")
        
        
    # # Create directories if they don't exist
    # file_dir = os.path.dirname(file_path)
    # if file_dir:
    #     os.makedirs(file_dir, exist_ok=True)
    #     logging.info(f"Creating directory: {file_dir}")

    # # Create the file
    # with open(file_path, 'w') as f:
    #     pass  # Just create an empty file
    #     logging.info(f"Creating file: {file_path}")