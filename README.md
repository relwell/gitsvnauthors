In sufficiently large projects, or those with a large group of non-core 
commit authors, the default author migration scheme in Git-SVN falls short. 
In order to use an authors file, you need to have an exhaustive list of 
every author in the repo, with their correct Git credentials. Sometimes these 
contributors were one-offs that don't have an email address you can use 
for this info, and other times, you just don't want to enumerate every single 
author. The default behavior of Git-SVN with an authors file 
provided during cloning is to run until an unlisted author is encountered 
in an SVN commit, and then fail there. For certain repositories -- 
particularly those with numerous commits, this can be a big time-waster. 

This script is designed to make it easy to migrate a list of SVN authors
from an SVN project to a Git project. This list does not have to be 
exhaustive. To do this, take the following steps:

## Clone your SVN Project with Git-SVN
If you don't know how to do this, check out the [documentation on the Git
site](http://git-scm.com/book/en/Git-and-Other-Systems-Migrating-to-Git).
Ignore the instructions about authors; that's what we're going to handle here.

## Create an Authors List
Create a file that lists authors in the following format:

    [SVN login] = [Full Name] <[email]>

So for instance, mine would look like this:

    robert = Robert Elwell <robert@wikia-inc.com>

## Run the Script
You should run the script from the root folder of the repo that you are 
planning on migrating. **You should perform this before making any branches, 
since you will need to run this on every single branch in your Git repo.**
The syntax of the script is as follows:

    [my-git-repo]$ /path/to/gitsvnauthors.py /path/to/authors.txt

This script compiles all authorship information into a single-pass 
git-filter-branch call on each commit.