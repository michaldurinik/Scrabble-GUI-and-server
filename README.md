# Scrabble-game

## Instructions for first installation
* Create a new folder on your computer and inside  that folder:
* `git init`
* `git checkout -b PICK-YOUR-BRANCH-NAME`
* IF you **NOT** using SSH `git remote add origin https://gitlab.computing.dcu.ie/durinim2/scrabble-game.git`
* If you **ARE** using SSH `git remote add origin git@gitlab.computing.dcu.ie:durinim2/scrabble-game.git`
* `git pull origin master`
* it will create your own branch where you can work, which is copy of master


## Swapping between branches
* `git checkout BRANCHNAME`

### good read about python networking: https://realpython.com/python-sockets/

## how to run:
1. run server.py in one terminal
2. run client.py in another terminal

## Instructions for merging your work into master

### Preconditions

* You are on your own branch, `myBranch_1` for example.
* You have committed all your changes.
* You have pushed your commits to the remote copy of your branch.

### Instructions

* `git checkout master` move to master branch locally.
* `git pull` if you are asked to i.e. if your copy is not up to date.
* `git merge YOUR-BRANCH-NAME` merge the branches.
* `git push origin master` push your master to the remote version.