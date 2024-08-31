import setuptools

# Read the long description from the README.md file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the package version
__version__ = "0.0.0"

# Metadata for the package
REPO_NAME = "Student_Mgt_System_Project"                       # The repository name
AUTHOR_USER_NAME = "onisj"                                     # GitHub username of the author
SRC_REPO = "src"                                               # The source repository name
AUTHOR_EMAIL = "elyxir4lyf@hotmail.com"                        # Contact email for the author

# Set up the package using setuptools
setuptools.setup(
    name=SRC_REPO,                                             # Package name
    version=__version__,                                       # Package version
    author=AUTHOR_USER_NAME,                                   # Author's GitHub username
    author_email=AUTHOR_EMAIL,                                 # Author's contact email
    description="A student management system in python",       # Short description of the package
    long_description=long_description,                         # Long description read from README.md
    long_description_content_type="text/markdown",             # Format of the long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # URL of the project repository
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"  # URL to report issues
    },
    package_dir={"": "src"},                                   # Directory where the package is located
    packages=setuptools.find_packages(where="src")             # Find all packages in the 'src' directory
)