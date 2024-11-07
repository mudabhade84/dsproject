## end to end ds project #


1. set up  git cofiguration 


if you are using git first time use git global - configuration 
-- git config --global user.email



-- add gitignore file on github website 
-- use following commands to use github 

git init 
git add README.md
git commit -m 'first commit'
branch -M main 
git remote add origin http://github.com/mudabhade84/dsproject.git
git push -u origin main 
git pull  



---------------------------------------------

create files 

-- src folder 
-- __init__.py file 

setup.py 

setup.py file has

packages= find_packages(),
install_requires = get_requirements('requirements.txt')

which is used for finding the packages 

----------------------------------------------

requirements.txt file has packages names ending with -e . (hyphen E dot )

