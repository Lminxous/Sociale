# Sociale

A blog website hosted on heroku using AWS(S3 and IAM) on Postgres database .


# Explanation of Models

Authenticated User(BITS mail)

1. An authenticated user can post & update blogs. It must be given the following attributes:
```
author
date_posted
title
content
```
2. An authenticated user can comment on blogs. It must be given the following attributes:
```
author
post
content
```
3. An authenticated user can report blogs written by other users & if a blog is reported by 5 independent users, blog would be deleted. It must be given the following attributes:
```
author
date_posted
title
content
reported_by
```
4. User Model is just used for the Authentication(security reasons) , all other models are related to Profile model.

5. An authenticated user can follow other users.

6. An staff user can print out a user report (openpyxl).


# Google Oauth2.0

1. Go to https://console.developers.google.com/apis/dashboard and create a project.

2. Fill out the OAuth consent screen , add Application name & your email.

3. Go to Credentials & click on Create Credntials to make OAuth 2.0 Client ID.

4. Go to your admin page & in social accounts add Client ID & Client Secret & shift example.com/localhost in Chosen sites.
