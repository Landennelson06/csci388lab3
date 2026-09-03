x# Lab 03: Git and GitHub

This repository documents my practice with 
local Git, GitHub, branches, and pull requests.
## README Responses

### 1.1 After initialization
```text
ls -la
drwxr-xr-x 1 landen landen 4096 Sep  3 09:55 .
drwxr-x--- 1 landen landen 4096 Sep  1 11:05 ..
drwxr-xr-x 1 landen landen 4096 Sep  3 09:55 .git
-rw-r--r-- 1 landen landen  910 Sep  3 09:55 README.md
-rw-r--r-- 1 landen landen  435 Aug 20 11:06 ReadinessCheck.class
-rw-r--r-- 1 landen landen  128 Aug 20 11:06 ReadinessCheck.java
drwxr-xr-x 1 landen landen 4096 Sep  3 09:55 cd
drwxr-xr-x 1 landen landen 4096 Aug 27 10:31 class-exercises-fall2026
drwxr-xr-x 1 landen landen 4096 Sep  1 11:03 collab
-rw-r--r-- 1 landen landen  110 Aug 25 10:20 init-app.sh
drwxr-xr-x 1 landen landen 4096 Sep  3 09:55 lab03-exercises
drwxr-xr-x 1 landen landen 4096 Aug 20 11:04 lab1
drwxr-xr-x 1 landen landen 4096 Aug 25 10:20 my-app
-rw-r--r-- 1 landen landen   14 Aug 25 10:19 readme.txt
```
### 1.2 First git status
On branch main
nothing to commit, working tree clean
### 1.3 After the first commit
b054167 (HEAD -> main) create labs readme
### 1.4 git log

### 1.5 git diff

Paste the `git status` and `git diff` commands and their output.

How does this `git status` differ from the one in **1.2**?
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

diff --git a/README.md b/README.md
index e56d7dc..2cd0f2f 100644
--- a/README.md
+++ b/README.md
@@ -1,5 +1,6 @@
 x# Lab 03: Git and GitHub
-
+This repository documents my practice with
+local Git, GitHub, branches, and pull requests.
 ## README Responses

 ### 1.1 After initialization
@@ -21,9 +22,10 @@ drwxr-xr-x 1 landen landen 4096 Aug 25 10:20 my-app
 -rw-r--r-- 1 landen landen   14 Aug 25 10:19 readme.txt
 ### 1.2 First git status
-
+On branch main
+nothing to commit, working tree clean
 ### 1.3 After the first commit
-
+b054167 (HEAD -> main) create labs readme
 ### 1.4 git log

 ### 1.5 git diff
@@ -31,6 +33,15 @@ drwxr-xr-x 1 landen landen 4096 Aug 25 10:20 my-app
 Paste the `git status` and `git diff` commands and their output.

 How does this `git status` differ from the one in **1.2**?


This status has untracked files 
### 1.6 Git command reflections

In one or two sentences each, what does each command do?

- `git init`
creates .git files
- `git status`
shows current status of staging etc
- `git add`
adds unstaged files to staging area
- `git commit`
commits staged files to a commit
- `git log`
shows a list of commits
- `git diff`
compare file to prev commit

### 1.7 Repository link
https://github.com/Landennelson06/csci388lab3
### 1.8 Comparing approaches

In your own words:

- How does the nested-loop approach check for a duplicate?
- How does the set-based approach check for a duplicate?
- What is the runtime and memory trade-off of each?

### 1.9 Pull request merge options

In your own words, what does each GitHub merge option do?

- Create a merge commit
- Squash and merge
- Rebase and merge
