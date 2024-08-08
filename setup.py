from setuptools import find_packages, setup
from typing import List # See the get_requirements() function - why we need List ???
# find_packages --> will help you find all the packages that are used in this project's directory

# The below can be considered as the "meta-data" content about the project
# In short -> "Data / Information about the Project"

HYPHEN_E_DOT = '-e .'

# Creating a function, ingesting (.txt) files containing the names of packages (python libraries)
# to be installed along with this project package
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirtements (python libraries)
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() # readlines() function - when reading line by line, also add '\n' character at the end !
        requirements = [req.replace('\n', ' ') for req in requirements] # Get rid of '\n' by replacing it with ' ' (space)

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT) 
            # '-e .' is just used to trigger setup.py - because it's not a package and may cause error if it remains in requirements.txt file,
            # We need to remove it from the file's content before installing the mentioned packages

    return requirements

'''
In requirements.txt file, you must add '-e .' to trigger the setup.py file
to run the setup.py file to build the package(s).
'''
    
setup(
    name = 'datascienceproject',
    version = '0.0.1', # The version of your application / package
    author = 'Soubhik Sinha', # Author Name
    author_email = 'hackos.sinha@gmail.com', # Author Email ID
    packages = find_packages(),
    # install_requires = ['pandas', 'numpy', 'seaborn'], # Say you want these libraries to be installed with your package - it will be done automatically !!!
    # But imagine you want numerous packages to get installed along - then writing one-by-oine like the above is not feasible - SO SOLUTION ? 🔽🔽
    install_requires = get_requirements('requirements.txt') # Create a function which will ingest a (.txt) file which contains the name of all require packages to ne installed along
)

'''
How come find_packages() will be able to find the packages (made externally for this project) in this project's directory ? 🔽
>> Say 'src' is a packages. To make find_packages() know that it is a package, just add __init__.py
>> file in the package folder (This applies to all the package folders inside the project's directory)
>> Then, after finding the package, the function will try to build the package.
>> (Recall the way we install numpy, pandas, etc. - any python library)

>> Here, the project itself is considered as a package, thus the entire project development
>> will be done inside the 'src' folder.

>> If we even try to make another folder inside this 'src' folder, that internal folder
>> will also act as a 'package'
'''