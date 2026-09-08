Question 1: Observe the files created, what do you think they contain.
uv init created pyproject.toml which contains the project's metadata, its dependencies and requirements and scirpts. the python-version file which sais what python version the project needs, the readme file for any explanations abt the project like instructions on how ton run it and what it does and the init file which makes it so that the folder is seen by the code as a python package so it can import from it.

> Question 2: What are the created files. What do you think they are used for? And which ones should be pushed to git?
it created dvc/config which is a dvc config file used to save any variables or paths related to dvc
the dvc ignore to ignore files and not track them with dvc
the dvc/.gitignore file to ignore dvc files from being tracked by git and we should push all of them to git

> Question 3: Where are the credentials stored? and what are the options other than --global? Should the credentials be pushed to github? 
it stores the credentials on a global dvc config folder on my compouter outside my repo we can also save it locally in a dvc config.local file ignored by github or project which also saves it in a config file in the repo or system which is same as global but for all users on the comouter
We should never push credentials to github

> Question 4: Take a look at the .gitignore file. Explain what happened.
dvc automatically added /data to .gitignore file to tell github to not track data files

> Question 5: Do you see a .dvc file? What does it contain? 
yes I see a dvc folder in my project it contains metadata abt the data files like like the unique number md5 for the version of the data the size of the data number of files and the path to the original data folder

> Question 6: You can check your main branch on the github web UI. Is the code there? Is the data there? Do you have any file that points to the data location. And what about dagshub web UI do you see the data? 
On github i see the code dont see the data but see data.dvc which points to the data and on dagshub i see the data

> Question 7: In a completely new temporary folder clone your github repo. Do you see the data folder? What dvc command is needed to get the data folder?
no i dont see the data folder the command needed to get it is dvc pull

> Question 8: Do you still see the new folders you created? food11_processed and food11_processed_mini?
No i dont see the new folders i created when i went back and checked out main the dvc again they showed back up.

