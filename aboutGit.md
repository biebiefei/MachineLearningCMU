# Steps to enable git on your terminal.

## 1. install git
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

$ brew install git

$ git --version

> git version 2.8.1

## 2. git clone -- copy git files to your local terminal

$ git clone https://github.com/biebiefei/MachineLearningCMU.git

$ ls

> ... MachineLearningCMU ...

$ cd MachineLearningCMU

$ ls

> Homeworks	README.md aboutGit.md

## 3. git branch -- make your own branch

$ git branch ${new_branch_name}

(new_branch_name="shutong" suggested :p)

$ git checkout ${new_branch_name}

$ git branch

> master

> \* ${new_branch_name}

("*" means your current branch)

## 4. make directories to organise files

$ cd Homeworks

$ ls

> make_directories.sh

$ chmod u+x make_directories.sh

$ ./make_directories.sh

(This is a shellscript file I made to make directories for all lectures)

$ ls

> Lecture1 Lecture2 ..... Lecture30

# Steps to upload your files to git

## 5. git add -- add your files to corresponding directories

Ex.

$ copy /Users/dashu/Desktop/${homework_path}/${code_file} ./Lecture1/wa/

## 6. git push -- push your changes to git

$ git add .

$ git status

(check what you have changed on git)

Ex.

> On branch fei
> Changes to be committed:
>   (use "git reset HEAD <file>..." to unstage)
>
>	modified:   Homeworks/make_derectories.sh

$ git commit -m "${your commit message}"

Ex.

> 1 file changed, 3 insertions(+), 3 deletions(-)

$ git push origin ${new_branch_name}

Then go to git webpage, and check on your push result, click on "create pull request".

And others can check or review on your uploaded files!
