Title: Build Your Own Static Blog by Pelican and Github Page PartI
Date: 2018-02-23 22:39
Modified: 2018-02-23 22:39
Category: Blog
Tags: pelican, publishing
Slug: Build Your Own Static Blog by Pelican and Github Page PartI
Authors: Phil.Gao
Summary: Introducation how to quick start to set up the site,add themes,configure publish configuration file & apply theme.Also record some tips on git command that are used to commit into github.

#Build Your Own Static Blog by Pelican and Github Page
![Alt text]({filename}/images/cat.jpg "Cat")

### What's the Pelican ?
Pelican is a static site generator, written in Python. You could see it as a tools that able to transform your markdown post as html format.
> Here is the document link for *[Pelican](http://docs.getpelican.com/en/stable/)*

### What's Github Pages ?
GitHub Pages is a static site hosting service. It is designed to host your personal, organization, or project pages directly from a GitHub repository.

I simply list steps about creating  github pages :
  * Create a account 
  * Create a repository named : `username.github.io`
  * Pull this reporsitory
  * Add one index.html file to initial 
  * Commit & Push

> Here is [*Step by step guide*](https://pages.github.com/) from github 

### Before you go , what you should prepare ?
* Install envitual enviroment
* Install Pelican 
* Create Two of Github repository (One stores site file , another store the source code )
* Install Markdown 
### How to made it ?

#####Step 1 : Install virtaulenv

    pip install virtualenv

#####Step 2 : Setup virtualenv

	virtualenv F:\venv1

> F:\venv1 is a directory to place the new virtual environment

	cd F:\venv1\Scripts
	activate
> As I am using windows I need to change directory to "Scripts" folder  
> Then the command line would look like this 
	
	(venv1) F:\venv1\Scripts> 
>Note : using deactivate to close the environment  
>Code like this : 

    cd F:\venv1\Scripts
	deactivate 
	
#####Step 3 : Install the Pelican
Simply run 
```python
pip install pelican
```

#####Step 4: Initial the Repository
Clone the souce code repository  
```
git clone git@github.com:username/username.github.io-src blog
cd blog
```
Confirm the repository information 
```
git remote -v
```
Add submodel as the output folder to blog repository

```
git submodule add git@github.com:username/username.github.io.git output
```

#####Step 5 : Set up Pelican 
```python
pelican quickstart 
```
#####Step 6 : Build Blog
```
pelican content
pelican content -s publishconf.py
```
#####Step 7 : Preview the Site

```
cd ~/projects/yoursite/output
python -m pelican.server
```


#####Step 8 : Add & Commit Change
   

```
cd output
git add .
git commit -m "First post."
git push -u origin master
cd ..
echo '*.pyc' >> .gitignore #don't need pyc files
git add .
git commit -m "First commit."
git push -u origin master
```

### How to add themes for you blog ?
Pelican has made a lot of themes in the github. You could preview these themes in http://www.pelicanthemes.com/ and choose one you like.
####Step one : get the themes file from github 
You can clone all the reporsitory or download zip file 
####Step two : Install themes
You shall activate the virtaulenv first , move the folder scripts 
```Python
pelican-themes --install C:\Users\Phil.Gao\BlogThemes\pelican-themes\bootlex
pelican-themes -l
```
####Step Three : configure the file in 
Add Theme configuration 
```
THEME = "bootlex"
```

### To be continued..

> **Note** : 
> 
>1. Customized your own themes (change ---> create )
>2. Add the comment area 
>3. Add picture at the post 
>4. change the site URL
>5. What's best practise to publish consistly ? 


----------


