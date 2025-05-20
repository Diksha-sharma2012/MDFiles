## Git is a version Control System. It is:
* Popular
* Free & Source
* Fast & Scalable

#### <b> Git is mainly used and helps for:</b>
1. Track the History: It is used to track the history of code. For instance we create a signup page and we add some buttons on it and we add a help page on it.  
   If we want to go to the coding where only the buttons are added  then we can go to that code by Git.  
   we can also go to the signup page where the help page is connected with buttons in it and we cal also go to the signup page where only th buttons are added.
2. Collaborate:  Working in team. It helps to reduce code overwritting by multiple users. 

## Github:
- It is a website that allows developers to store and manage their code using Git.
- In it we can upload our projects and assignments that other user can see.
## Git Commands:
* --version: Used to check the version of Git.
* cd : Change directory
* ls: Will print all the files and folder.
* ls -Force : will also show hidden directories.
* Clear: Command will clear the window.
* pwd: Command will provide us the working directory.
* mkdir: "mkdir dir_name" used to make new directory.
## Git Config: (Used to configure the Git account)
- "~" show that we are in root directory
- To change user name, user email id 
- <b>Following are steps to configure username, email</b>
* git config --global user.name "My Name" (used to configure username)
* git config --global user.email "someone@email.com" (used to configure email)
* git config --list (used to show list of changed user name and email)
* <b>Clone & status:</b>
   - clone- Cloning a repository on our local machine   
   ``` git clone <- some link -> ``` (instead of <- some link -> enter the link of code (HTTPS) that is uploaded on Github, and the uploaded file will be clone or stored in our device.)
   - status- Display the state of the code
   ``` git status ``` (If we will do any change in device project and github project and changes are not same in both files then it will show us where we have to do change.)  
   Whenever we do changes in the device file it will show four status:
   1. Untracked: new files that git doesn't yet track.
   2. modified: changed
   3. staged: file is ready to be committed
   4. unmodified: unchanged 
   * Add & Commit 
   If we add a new file in device location and we want to that change on git then we will follow the following steps:  
   Add the file by using command ``git add file_name`` and the file will be shown in "changes to be committed".  
   And if we have multiple changed file to add in github then we run the command ``git add .``, the "." is for all files.  
   To commit the file we will run command ``git commit -m "Some message"``, but still our file changes are not /shown on github.  
   The ``git push origin main`` is Push command used to push the file from local device to github.
### Init Command 
<b> init: </b> Used to create a new git repository.  
- git init
- git remote add origin <- link ->  (add repo to git)
- git remote -v     (to verify remot)
- git branch        (to check branch)
- git branch -M main  (to rename barnch)
- git push origin main  
      or  
  git push -u origin main (will always push repo in main)

### Git Branches
#### Branch Commands:
* git branch (to check branch)
* git branch -M main (to rename branch)
* git checkout <- branch name ->    (to navigate / got from one branch to another)
* git checkout -b <- new branch name ->   (to create new branch)
* git branch -d <- branch name ->       (to delete branch)

### Merging Code
There are two ways to merge code:
* Way 1
   - git diff <- branch name ->      (to compare commits, branches, files & more)
   - git merge <- branch name>        (to merge 2 branches)
* way 2
    - Create a PR  (Pull Request lets you tell other about changes you've pushed to a branch in a repository on GitHub.)
    - git pull origin main (is used to apply the pull request on the VS code.)

### Resolving Merge Conflicts
    - An event that takes place when Git is unable to automatically resolve differences in code between two commits.
    - git merge main  (Remove unwanted comments or commands and select the change that you want to done in your code)
    - git status
    - git add.
    - git commit -m "Add both features"
    - git status
    - git diff main
    - git merge feature  
    - git push

### Undoing Changes
Case 1: staged changes  
      git reset <- file name ->
      git reset

Case 2: commited changes (for one commit) 
       git reset HEAD-1

Case 3: commited changes (for many commits)
       git reset <- commit hash ->
       git reset --hard <- commit hash ->            

## ``git log`` is used to check all the commits. (And quit with "Q")

### Fork
  - A frok is a new repository that shares code and visibility settings with the original "upstream" repository.  
  Fork is a rough copy.
  - Go to someone's project and click on "Fork" and after that click on "create Fork", Now the someone's project is copied on your account.

## Create a new repository on the command line
- echo "# Interview-Questions" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/Diksha-sharma2012/Interview-Questions.git
- git push -u origin main

## Push an existing repository from the command line
- git remote add origin https://github.com/Diksha-sharma2012/Interview-Questions.git
- git branch -M main
- git push -u origin main



