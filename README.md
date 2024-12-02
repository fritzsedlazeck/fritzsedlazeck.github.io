# How to run the dev-container

1. install docker compose
2. cd the folder
3. docker-compose pull // run it first time
4. docker compose up // start dev server
5. docker compose down // end dev server


# how to update publication 

1. login to google scholar 
2. check the box left the `TITLE`
3. click export -->  BibTex --> Export all my article
4. python process_publication.py citations.txt > citations.with-year.txt // This is uesd to filter out items without year.

copy all bibs into _bibliography/papers.bib


# how to add a blog

Create a markdown file at _posts.
Copy the headers in existing md file and modify tags etc...
Write blog as normal markdown.

# how to update news

write markdown file in _news folder

if you want the news has a independent page, use `inline: false` at header, otherwise, it will be shown in the `About` page only:

```
---
layout: post
title: A long announcement with details <--provide a title
date: 2015-11-07 16:11:00-0400
inline: false <---set as false
related_posts: false
---

other text

```

if you only need a sentence that declare something without details use:

```
---
layout: post
date: 2015-11-07 16:11:00-0400
inline: true
related_posts: false
---

a sentence

```

