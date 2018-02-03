# Steps to enable git on your terminal.

## 1. install git
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew install git
$ git --version
```
> git version 2.8.1

## 2. git clone -- copy git files to your local terminal
```
$ git clone https://github.com/biebiefei/MachineLearningCMU.git
$ ls
```
> ... MachineLearningCMU ...
```
$ cd MachineLearningCMU
$ ls
```
> Homeworks	README.md aboutGit.md

## 3. git branch -- make your own branch
```
$ git branch ${new_branch_name}
```
(new_branch_name="shutong" suggested :p)
```
$ git checkout ${new_branch_name}
$ git branch
```
> master

> \* ${new_branch_name}

("*" means your current branch)

## 4. make directories to organise files
```
$ cd Homeworks
$ ls
```
> make_directories.sh
```
$ chmod u+x make_directories.sh
$ ./make_directories.sh
```
(This is a shellscript file I made to make directories for all lectures)
```
$ ls
```
> Lecture1 Lecture2 ..... Lecture30

# Steps to upload your files to git

## 5. git add -- add your files to git directories

First, copy your local files to your git directories.

Example
```
$ cp /Users/dashu/Desktop/${homework_path}/${code_file} ./Lecture1/wa/
```
\* If you have mistakenly put your files in a wrong directory, you can use the follwing command to move files.
```
$ mv /${wrong_directory}/${code_fiile} /${right_directory}/${code_file}
```
Then, add your files to git and get ready to push.
```
$ git add .
```
\* "." means your current directory, and so all modified/newly created files under your current directory will be commit to git
## 6. git push -- push your changes to git
Check what you have changed on git.
```
$ git status
```
Example

> On branch fei
> Changes to be committed:
>   (use "git reset HEAD <file>..." to unstage)
>
>	modified:   Homeworks/make_derectories.sh
```
$ git commit -m "${your_commit_message}"
```
Example

> 1 file changed, 3 insertions(+), 3 deletions(-)
```
$ git push origin ${new_branch_name}
```
Next, go to your git webpage, check on your push result, and click on "create pull request" button.

Then others can check or review on your uploaded files!
