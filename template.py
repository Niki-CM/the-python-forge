import os

# Project name
project_name = "Python-Forge"

# Folder structure
folders = [

    # Python Basics
    "Python-Basics",

    # Logic Building
    "Logic-Building/patterns",
    "Logic-Building/number_problems",
    "Logic-Building/string_problems",
    "Logic-Building/logic_challenges",

    # DSA
    "DSA/Arrays",
    "DSA/Linked-Lists",
    "DSA/Stacks",
    "DSA/Queues",
    "DSA/Trees",
    "DSA/Recursion",
    "DSA/Searching",
    "DSA/Sorting",

    # Mini Projects
    "Mini-Projects/calculator",
    "Mini-Projects/password_generator",
    "Mini-Projects/tic_tac_toe",
    "Mini-Projects/expense_tracker",

    # Automation
    "Automation/file_organizer",
    "Automation/email_sender",
    "Automation/web_scraper",

    # APIs
    "APIs/weather_api",
    "APIs/spotify_api",
    "APIs/github_api",

    # Data Science
    "Data-Science/NumPy",
    "Data-Science/Pandas",
    "Data-Science/Data-Cleaning",
    "Data-Science/EDA",
    "Data-Science/Visualization",

    # Machine Learning
    "Machine-Learning/Linear-Regression",
    "Machine-Learning/Logistic-Regression",
    "Machine-Learning/Decision-Trees",
    "Machine-Learning/Random-Forest",
    "Machine-Learning/Clustering",
    "Machine-Learning/Projects",

    # Extra folders
    "notebooks",
    "assets"
]

# Files to create
files = [
    "requirements.txt",
    ".gitignore"
]

# Create folders
for folder in folders:
    folder_path = os.path.join(project_name, folder)
    os.makedirs(folder_path, exist_ok=True)

    # Create .gitkeep file inside each folder
    gitkeep = os.path.join(folder_path, ".gitkeep")

    with open(gitkeep, "w") as f:
        pass

# Create files
for file in files:
    file_path = os.path.join(project_name, file)

    with open(file_path, "w") as f:
        pass

print("⚒️ Python Forge structure created successfully!")