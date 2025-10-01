
from setuptools import setup,find_packages


def find_requirements(filename)->list[str]:
    with open(filename,"r") as file:
        lines=file.readlines()
        lines=[line.replace("\n","") for line in lines]
        for line in lines:
            if line=="-e .":
                lines.remove(line)
        return lines
        
        
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Vamsi",
    author_email="vamsigandavarapu101@gmail.com",
    packages=find_packages(),
    install_requires=find_requirements("requirements.txt")
    
    
    
    
    
    
)