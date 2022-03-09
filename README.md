# **The Diet Pantry **

Welcome to My 4th milestone project at Code Institute. The Diet Pantry website is more or less the end of a long long and hard journey in the world of Coding. The purpose of this project 
to use build a full-stack site around a business logic. I have applied everything what i have learned at Code Institute. The technologies i have used for this project are: HTML, CSS, JAvaScript, Python and Django. Stripe handles online test payments and Heroku Postgres as a relational database.

This website is a fictional webshop for people who are following different type of diets. Sometimes it is really hard to find the right and trustable products for the different diets, so this website supposed to collect the tested and trusted dietary products. 

[Live site](http://mp4-diet-pantry.herokuapp.com)
[Github link] (https://github.com/szomoru/MP4-DietPantry) 


## Table of Contents

[User Experience (UX)](#UX)

[Features](#features)

[Technologies Used](#technologies)

[JavaScripts](#scripts)

[Testing](#testing)

[Deployment](#deployment)

[Credits](#credits)










<a name="deployment"></a>

## **Deployment**

### Requirements for Deployment

* Python
* GitHub account
* Heroku account

### Initial Deployment


**Heroku Deployment**

1. Log into Heroku
2. Create a new app, choose a location closest to you
3. Search for Heroku Postgres from the resources tab and add to your project
4. Make sure to have `dj_database_url` and `psycopg2` installed.
```
pip3 install dj_database_url
pip3 install psycopg2
```
5. Login to the Heroku CLI - `heroku login -i`
6. Run migrations on Heroku Postgres - `heroku run python manage.py migrate`
7. Create a superuser - `python manage.py createsuperuser`
8. Install `gunicorn` - `pip3 install gunicorn`
9. Create a requirements.txt file - `pip3 freeze > requirements.txt`
10. Create a `Procfile` (note the capital P), and add the following,
```
web: gunicorn moose_juice.wsgi:application
```
11. Disable Heroku from collecting static files - `heroku config:set DISABLE_COLLECTSTATIC=1 --app <your-app-name>`
12. Add the hostname to project settings.py file
```
ALLOWED_HOSTS = ['<you-app-name>.herokuapp.com', 'localhost']

```
13. Connect Heroku to you Github, by selecting Github as the deployment method and search for the github repository and pressing `connect`
14. In Heroku, within settings, under config vars select `Reveal config vars`
15. Add the following, 
```
AWS_ACCESS_KEY_ID =	<your variable here>
AWS_SECRET_ACCESS_KEY =	<your variable here>
DATABASE_URL =	<added by Heroku when Postgres installed>
DISABLE_COLLECTSTATIC =	1 
EMAIL_HOST_PASS = <your variable here>
EMAIL_HOST_USER = <your variable here>
SECRET_KEY = <your variable here>
STRIPE_PUBLIC_KEY = <your variable here>
STRIPE_SECRET_KEY = <your variable here>
STRIPE_WH_SECRET = <different from env.py>
USE_AWS = True
```
16. Go back to the Deploy tab and under Automatic deploys choose `Enable Automatic Deploys`
17. Back in your CLI add, commit and push your changes and Heroku will automatically deploy your app
```
git add .
git commit -m "Initial commit"
git push
```
18. Your deployed site can be launched by clicking `Open App` from its page within Heroku.

### How to Fork it

1. Login or Sign Up to [GitHub](www.github.com).
2. On GitHub, go to [szomoru/extrahand-mp3](https://github.com/szomoru/extrahand-mp3).
3. In the top right, click "Fork".
4. You will need to create an env.py file with your own values, and create a MongoDB database with the data keys and types as shown above.
5. You will also need to install all of the project requirements. This can be done using the command:
    * `pip3 install -r requirements.txt`
6. Type `python3 app.py` in your GitPod terminal to run your local site of this project.

### Making a Local Clone

1. Log in to [GitHub](https://www.github.com) and locate the [Repository](https://github.com/szomoru/extrahand-mp3) for this site.
2. Under the repository name, above the list of files, click "Code".
3. Here you can either Clone or Download the repository.
4. You should clone the repository using HTTPS, clicking on the icon to copy the link.
5. Open Git Bash.
6. Change the current working directory to the new location, where you want the cloned directory to be.
7. Type `git clone`, and then paste the URL that was copied in Step 4.
    * `git clone https://github.com/szomoru/extrahand-mp3.git`
8. Press Enter, and your local clone will be created.
9. You will need to create an env.py file with your own values, and create a MongoDB database with the data keys and types as shown above.
10. You will also need to install all of the project requirements. This can be done using the command:
    * `pip3 install -r requirements.txt`.
11. Type `python3 app.py` in your Gitpod terminal to run your local site of this project.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/szomoru/extrahand-mp3)


<a name="credits"></a>

## Credits

### Code

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

-   [W3Schools](https://www.w3schools.com/): I have used their content many times to understand CSS and HTML, JavaScript and learned a lot from their content

-   [Froggy](https://flexboxfroggy.com/): I have used this cute educator site to understand better the flexbox method

-   [CSS tricks](https://css-tricks.com/): I have also learned a lot and found interesting topics on the CSS-tricks website

-   [Stackoverflow community](https://stackoverflow.com/): I have read a lot of forums and got a lot of hints how to continue when i was stucked.

### Content

-   All content was written by the developer -Gergely Vig. 
- I have used the following documents as a support and inspiration for the README.md file:
    - Code Institute [SampleREADME](https://github.com/Code-Institute-Solutions/SampleREADME)
    - Code Institute [README Template](https://github.com/Code-Institute-Solutions/readme-template)
    - [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)
    - [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
    - [Gergely Vig](https://github.com/szomoru/MP1-Bodyweight)
   
    

### Media

- 
    

### Acknowledgements

-   My Mentor for helpful feedback.
-   Thanks to my family specially my wife who taken over our 4 kids while i was doing my studies. 