from setuptools import find_packages, setup
from typing import List 

def get_requirements()->List[str]:
    """
    This functions will return list of requirements
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt') as file:
            #Read all the lines in the file
            lines = file.readlines()
            #Process each line 
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e . 
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_lst

setup(
    name = 'MLOPS_NetworkSecurity',
    version = '0.0.1',
    author = 'Andrew Melendez',
    author_email = 'melendeza895@outlook.com',
    packages=find_packages(),
    install_requires = get_requirements()
)