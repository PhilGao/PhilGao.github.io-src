Title: Build Your Own Static Blog by Pelican and Github Page PartII
Date: 2018-03-27 22:39
Modified: 2018-03-27 22:39
Category: Blog
Tags: pelican, publishing
Slug: Build Your Own Static Blog by Pelican and Github Page PartII
Authors: Phil.Gao
Summary: Part2 would go to answer some questions I left in part1.It also post some issue and solution that i met when trying to build my blog. The part 2 would continusely update.

#Build Your Own Static Blog by Pelican and Github Page Part2

Part2 would go to answer some questions i left in part1.It also post some issue and solution that i met when trying to build my blog. The part 2 would continusly update.

## How to insert pictures in pelican.
I put the link in pelican guide about how to insert static file here.
[*Link to internal content*](http://docs.getpelican.com/en/latest/content.html?highlight=files#linking-to-internal-content)
######  Step1 Create one Folder under content which named images
######  Step2 Put the picture that you want to link to in this fold. I download a cat picture and name it as cat.jpg
######  Step3 Use below MD gramar to insert picture.In here {filename} would direct to content folder.

    ![Alt text]({filename}/images/cat.jpg "Cat")
![Alt text]({filename}/images/cat.jpg "Cat")