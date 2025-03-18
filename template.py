import os                   # Provides functions to interact with the operating system, such as creating files and directories.
from pathlib import Path    # Offers an object-oriented approach to handling file system paths.

# Define the project name
project_name = "us_visa"

# List of all required files for the project structure
list_of_files = [ 
    f"{project_name}/__init__.py",                      # Marks the folder as a package
    f"{project_name}/components/__init__.py",           # Marks the components directory as a package
    f"{project_name}/components/data_ingestion.py",     # Handles data ingestion
    f"{project_name}/components/data_validation.py",    # Performs data validation
    f"{project_name}/components/data_transformation.py",  # Handles data transformation
    f"{project_name}/components/model_trainer.py",      # Trains the machine learning model
    f"{project_name}/components/model_evaluation.py",   # Evaluates the trained model
    f"{project_name}/components/model_pusher.py",       # Deploys the trained model
    f"{project_name}/configuration/__init__.py",        # Marks configuration directory as a package
    f"{project_name}/constants/__init__.py",            # Defines constants used throughout the project
    f"{project_name}/entity/__init__.py",               # Marks the entity directory as a package
    f"{project_name}/entity/config_entity.py",          # Defines configuration-related entities
    f"{project_name}/entity/artifact_entity.py",        # Defines artifact-related entities
    f"{project_name}/exception/__init__.py",            # Handles project-specific exceptions
    f"{project_name}/logger/__init__.py",               # Implements logging functionality
    f"{project_name}/pipline/__init__.py",              # Marks the pipeline directory as a package
    f"{project_name}/pipline/training_pipeline.py",     # Manages the training pipeline
    f"{project_name}/pipline/prediction_pipeline.py",   # Manages the prediction pipeline
    f"{project_name}/utils/__init__.py",                # Marks the utilities directory as a package
    f"{project_name}/utils/main_utils.py",              # Implements utility functions
    "app.py",                   # Entry point for the application
    "requirements.txt",         # Lists required dependencies for the project
    "Dockerfile",               # Defines containerization settings for Docker
    ".dockerignore",            # Specifies files to be ignored by Docker
    "demo.py",                  # A sample script for demonstration purposes
    "setup.py",                 # Script for packaging and distributing the project
    "config/model.yaml",        # Configuration file for the model
    "config/schema.yaml",       # Defines the schema for input data
]

# Iterate through the list and create necessary directories and files
for filepath in list_of_files:
    filepath = Path(filepath)                       # Convert string path to a Path object for better handling
    filedir, filename = os.path.split(filepath)     # Split into directory and filename
    
    # If the directory path is not empty, create directories if they do not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    
    # Create the file if it does not exist or if it is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file
    else:
        print(f"File already exists at: {filepath}")
