import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

project_name = "CNN-classifier"

def create_project_structure():
    """
    Create the project structure for the CNN classifier.
    """
    
    # Define the directory structure
    directories = [
        ".github/workflows/.gitkeep",
        f"src/{project_name}/__init__.py",
        f"src/{project_name}/components/__init__.py",
        f"src/{project_name}/utils/__init__.py",
        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/config/config.py",
        f"src/{project_name}/pipeline/__init__.py",
        f"src/{project_name}/entity/__init__.py",
        f"src/{project_name}/constants/__init__.py",
        f"notebooks/trials.ipynb",
        f"config/config.yaml",
        f"dvc.yaml",
        f"params.yaml",
        f"requirements.txt",
        f"requirements.txt",
        f"setup.py",
        f"templates/index.html"    
    ]
    
    # Create directories
    for directory in directories:
        file_path = Path(directory)
        file_dir,filename = os.path.split(file_path)

        if file_dir:
            os.makedirs(file_dir, exist_ok=True)
            logger.info(f"Created directory: {file_dir}")
        if filename:
            with open(file_path, 'w') as f:
                pass
        logger.info(f"Created file: {file_path}")

    logger.info("Project structure created successfully.")

if __name__ == "__main__":
    create_project_structure()
    logger.info(f"Project '{project_name}' structure has been created.")
    print(f"Project '{project_name}' structure has been created.")
