# Scrabble-game

## Instructions for first installation
* Create a new folder on your computer and inside  that folder:
* `git init`
* `git checkout -b node-YOURNAME`
* IF you **NOT** using SSH `https://gitlab.computing.dcu.ie/durinim2/scrabble-game.git`
* If you **ARE** using SSH `git remote add origin git@gitlab.computing.dcu.ie:durinim2/scrabble-game.git`
* `git pull origin node`

## Instructions for merging your work into master

### Preconditions

* You are on your own branch, `myBranch_1` for example.
* You have committed all your changes.
* You have pushed your commits to the remote copy of your branch.

### Instructions

* `git checkout master` move to master branch locally.
* `git pull` if you are asked to i.e. if your copy is not up to date.
* `git merge myBranch_1` merge the branches.
* `git push origin master` push your master to the remote version.