# Set vim easy to use when writing python codes

### 1. Create the vim setting file, which is automatically executed every time you start vim.
```
$ vi ~/.vimrc
```

### 2. Copy the following setting commands in the file.
```
syntax on
set autoindent
set expandtab
set tabstop=4
set shiftwidth=4
```

### 3. Start vim to edit a file by the following command.
```
$ vi ${filename}
```
And you can write python codes conveniently with autoindent and highlights!

@[Reference](https://okuzawats.com/vim-syntax-highlighting-20150730/)

# Some hints to use vim

Vim has many convenient functions, and is especially efficient for batch processing.
Using vim properly accelerates your work enormously.

Here are some tips I usually use in my daily work.

(All of the following commands are available in vim command mode)
---
#### Search
##### Search for strings
```
:/${string}
```
##### Hide search result highlights
```
:noh
```

---
#### Line Numbers
##### Display line numbers
```
:set nu
```
##### Hide line numbers
```
:set nonu
```
---
#### Delete
##### Delete one line
```
:dd
```
##### Delete all
```
:%d
```
---
#### Copy and Paste
##### Copy all
```
:%y
```
##### Paste to current line
```
P
```
##### Paste to the next line
```
p
```
##### Paste mode (disable autoindent)
```
:set paste
```
---
#### Select
##### Select all
```
:ggVG
```
##### Disable select all
```
:shift+g
```
---
#### Replace
##### Replace strings
```
:%s/${stringToBeReplaced}/${stringReplacedTo}/g
```
##### Replace regular expression ^M to line break
```
:%s/^M/\r/g
```
\※ ^M is input by ctrl-V, ctrl-M
##### Replace "/"
```
%s;/;${stringReplacedTo}/g
```
---
#### Move Cursor
##### Move cursor to the last char in the line
```
$
```
##### Move cursor to first char in the line
```
^
```
##### Move cursor to the head of the line
```
O
```
