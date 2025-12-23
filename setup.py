from setuptools import setup, find_packages
from typing import List

# setup.py is the build script for setuptools. It tells pip how to install your package,
# manage dependencies, and handle metadata. While modern projects often use 
# pyproject.toml, setup.py remains a standard for:
# 1. Making your code installable (pip install .)
# 2. Defining dependencies (install_requires)
# 3. Distributing your package to PyPI

def get_requirements() -> List[str]:

    '''
    This function will return the list of requirements
    '''
    requirements = []
    try:
        with open('requirements.txt', 'r') as file:
            for line in file:
                req = line.strip()
                if req and req != '-e .' and not req.startswith('#'):
                    requirements.append(req)
    except FileNotFoundError:
        print("requirements.txt not found")

    return requirements

setup(
    name = 'NetworkSecurity with MLOPS',
    version = '0.0.1',
    author = 'whyCharan',
    author_email = 'charan.sandaka5@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements()
)