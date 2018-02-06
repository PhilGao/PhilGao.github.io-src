 Build Your Own Static Blog by Pelican and Github Page
 ===========

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
* Install envitualenviroment
* Install Pelican 
* Create Two of Github repository (One stores site file , another store the souce code )
* Install Markdown 
### How to made it ?

    git clone git@github.com:username/username.github.io-src ghpages
    git remote -v
    git add .
    git commit -m "ADD themes "
    git push -u origin master
    
    
    cd output
    git add .
    git commit -m "First post."
    git push -u origin master
    cd ..
    echo '*.pyc' >> .gitignore #don't need pyc files
    git add .
    git commit -m "First commit."
    git push -u origin master

### How to add themes for you blog ?

### To be continued..

> **Note** : 
> 
>1. Customized your own themes (change ---> create )
>2. Add the comment area 
>3. Add picture at the post 
>4. change the site URL




