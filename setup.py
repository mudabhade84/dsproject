from setuptools import find_packages,setup 
from typing import List 

 
HYPHEN_E_DOT ='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
     this function will return the packages mentioned in requirements.txt  
     it will take file file path and return list of package names to be installed 
    '''
    requirements=[]
    with open(file_path) as file_obj: 
        requirements = file_obj.readline()
        requirements = [req.replace("\n"," ") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT )

    return requirements


setup( 
    name ='dsproject',
    version='0.0.1',
    author = 'mahendra',
    author_email='mudabahde84@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')

)