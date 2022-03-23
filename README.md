# The Diet Pantry

<h1 align="center"><img src="docs/amiresponsive_tiny.jpg"/></h1>

Welcome to My 4th milestone project at Code Institute. The Diet Pantry website is more or less the end of a long long and hard journey in the world of Coding. The purpose of this project 
to use build a full-stack site around a business logic. I have applied everything what i have learned at Code Institute. The technologies i have used for this project are: HTML, CSS, JAvaScript, Python and Django. Stripe handles online test payments and Heroku Postgres as a relational database.

This website is a fictional webshop for people who are following different type of diets. Sometimes it is really hard to find the right and trustable products for the different diets, so this website supposed to collect the tested and trusted dietary products. 

[Live site](http://mp4-diet-pantry.herokuapp.com) 

[Github link](https://github.com/szomoru/MP4-DietPantry) 


## Table of Contents

[User Experience (UX)](#ux)

[Features](#features)

[Technologies Used](#technologies)

[JavaScripts](#scripts)

[Testing](#testing)

[Deployment](#deployment)

[Credits](#credits)


<a name="ux"></a>

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the content of the webpage and the aim of the site and also to get a general picture about the type of the products.
        2. As a First Time Visitor, I want Register for an Account
        3. As a First Time Visitor, I want to be able to easily navigate through the site and get an overal picture about the site structure.
        4. As a First Time Visitor, I want to see their social media availability, where i can get more information about the site or organisation / person behind that.
        5. As a first Time Visitor i want to see clearly what content available for without registration and what requires registration. 

    -   #### Unregistered User Goals

        1. As a Returning Visitor, I want to be able to login with my previously registered credentials.
        2. As a Returning Visitor, I want to be able to register request for help.
        3. As a Returning Visitor, I want to be able to apply to help someone else.
        4. As a Returning Visitor, I want to be able to update my profile information.
        5. As a Returning Visitor, I want to be able to edit my help request information.
        6. As a Returning Visitor, I want to be able to delete my registered requests.
        7. As a Returning Visitor, I want to be able to browse among all regitered tasks.
    
    
    -   #### Registered User Goals

        1. As a Registered User, I want to be able to login with my previously registered credentials.
        2. As a Returning Visitor, I want to be able to register request for help.
        3. As a Returning Visitor, I want to be able to apply to help someone else.
        4. As a Returning Visitor, I want to be able to update my profile information.
        5. As a Returning Visitor, I want to be able to edit my help request information.
        6. As a Returning Visitor, I want to be able to delete my registered requests.
        7. As a Returning Visitor, I want to be able to browse among all regitered tasks.

    -   #### Admin Goals
        As the admin i want to be able to delete any of the registered tasks.


-   ### Design

    -   #### Colour Scheme
        There are used mainly 2 big color groups on the website:
        <ul>
            <li></li>
            <li></li>
        </ul>

    -   #### Typography
        There are 2 main font styles used through the webshop. The fonts were selected from the Google Font website. 
        <ul>
            <li><strong>Sacramento:</strong> This font is used only at the logo of the website. The reason is it is a handwriting style from the 50's - 60's. The reason to have that style for the logo that it gives more private feeling. It is needed since the name of the webshop refers to fill up someones pantry, which is already very private. </li>
            <li><strong>Lato:</strong> This font is used the rest of the website. It is easy to read and longer texts are also look very good with this font. It provides stabilty and seriousness feeling. The designer of the font is <i>Łukasz Dziedzic</i>. He says about his design: <i>“Male and female, serious but friendly. With the feeling of the Summer,”</i>  </li>
        </ul>

    -   #### Imagery
        On the main page there are 4 photos which were supposed to promote healthy feeling and happiness. The 4 pictures were selected by symbolise the mission of the webshop creator. 
        Further images throught the website are only product images. The product imaes are straightforward and most cases comming from the product manufacturer database. 

-   ### Wireframes

    There were several design changes during the development process, but the final site looks very similar with the wireframe. The wireframe does not contain any colorscheme, because at that time it was still not decided what colors i am going to use (Note: after a failed submit the colorscheme has been changed for better contrast ratio -more in the TESTING.md ). 
    On the following pictures the wireframes are introduced by htmls. Each image contain a desktop and phone size wireframe.  

    -   [index.html WireFrame](docs/wireframe/index.png)

    -   [products.html WireFrame](docs/wireframe/products.png) 

    -   [product_detail.html WireFrame](docs/wireframe/productdetail.png)

    -   [profile.html](docs/wireframe/profile.png) 

    -   [bag.html WireFrame](docs/wireframe/shoppingbag.png) 

    -   [checkout.html WireFrame](docs/wireframe/checkout.png) 

    -   [checkout_success.html WireFrame](docs/wireframe/thankyou.png) 

    -   [keto.html / lowcarb.html /  highprotein.html / mediterranean.html WireFrame](docs/wireframe/dietlibrary.png)


<a name="technologies"></a>

## **Technologies Used**

<hr>

-   ### Languages ###
    -   HTML
    -   CSS
    -   JavaScript
    -   Python

<br>

-   ### Frameworks ###
    -   Django

<br>

-   ### Libraries ###
    -   Bootstrap CSS Framework
    -   Font Awesome
    -   Google Fonts
    -   JQuery

<br>

-   ### Editors ###
    -   GitHub
    -   dbDiagram
    -   Balsamiq

<br>

-   ### Tools ###
    -   TinyPNG
    -   Autoprefixer
    -   Am I Responsive

<br>

-   ### Database Management ###
    -   PostgreSQL

<br>

-   ### Deployment platform(s) ###
    -   Heroku:
    -   Amazon AWS


<a name="testing"></a>

## **Testing**
### ***fdsgdf***

<a name="deployment"></a>

## **Deployment**

-   ### Requirements for Deployment

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
web: gunicorn mp4-dietpantry.wsgi:application
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

*AWS S3 Bucket setup**
1. Create an Amazon AWS account
2. Search for S3 and create a new bucket
    - Allow public access
3. Under Properties > Static website hosting
    - Enable
    - index.html as index.html
    - save
4. Under Permissions > CORS use the following:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
5. Under Permissions > Bucket Policy:
    - Generate Bucket Policy and take note of Bucket ARN
    - Chose S3 Bucket Policy as Type of Policy
    - For Principal, enter *
    - Enter ARN noted above
    - Add Statement
    - Generate Policy
    - Copy Policy JSON Document
    - Paste policy into Edit Bucket policy on the previous tab
    - Save changes
6. Under Access Control List (ACL):
    - For Everyone (public access), tick List
    - Accept that everyone in the world may access the Bucket
    - Save changes

**AWS IAM (Identity and Access Management) setup**
1. From the IAM dashboard within AWS, select User Groups:
    - Create a new group
    - Click through and Create Group
2. Select Policies:
    - Create policy
    - Under JSON tab, click Import managed policy
    - Choose AmazongS3FullAccess
    - Edit the resource to include the Bucket ARN noted earlier when creating the Bucket Policy
    - Click next step and go to Review policy
    - Give the policy a name and description of your choice
    - Create policy
3. Go back to User Groups and choose the group created earlier
    - Under Permissions > Add permissions, choose Attach Policies and select the one just created
    - Add permissions
4. Under Users:
    - Choose a user name 
    - Select Programmatic access as the Access type
    - Click Next
    - Add the user to the Group just created
    - Click Next and Create User
5. Download the `.csv` containing the access key and secret access key.
    - **THE `.csv` FILE IS ONLY AVAILABLE ONCE AND CANNOT BE DOWNLOADED AGAIN.**

**Connecting Heroku to AWS S3**
1. Install boto3 and django-storages
```
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```
2. Add the values from the `.csv` you downloaded to your Heroku Config Vars under Settings:
3. Delete the `DISABLE_COLLECTSTATIC` variable from your Cvars and deploy your Heroku app
4. With your S3 bucket now set up, you can create a new folder called media (at the same level as the newly added static folder) and upload any required media files to it.
    - **PLEASE MAKE SURE `media` AND `static` FILES ARE PUBLICLY ACCESSIBLE UNDER PERMISSIONS**

### How to Fork it

1. Login or Sign Up to [GitHub](www.github.com).
2. On GitHub, go to [szomoru/MP4-DietPantry](https://github.com/szomoru/MP4-DietPantry).
3. In the top right, click "Fork".
4. You will need to create an env.py file with your own values, and create a MongoDB database with the data keys and types as shown above.
5. You will also need to install all of the project requirements. This can be done using the command:
    * `pip3 install -r requirements.txt`
6. Type `python3 app.py` in your GitPod terminal to run your local site of this project.

### Making a Local Clone

1. Log in to [GitHub](https://www.github.com) and locate the [Repository](https://github.com/szomoru/MP4-DietPantry) for this site.
2. Under the repository name, above the list of files, click "Code".
3. Here you can either Clone or Download the repository.
4. You should clone the repository using HTTPS, clicking on the icon to copy the link.
5. Open Git Bash.
6. Change the current working directory to the new location, where you want the cloned directory to be.
7. Type `git clone`, and then paste the URL that was copied in Step 4.
    * `git clone https://github.com/szomoru/MP4-DietPantry.git`
8. Press Enter, and your local clone will be created.
9. You will need to create an env.py file with your own values, and create a MongoDB database with the data keys and types as shown above.
10. You will also need to install all of the project requirements. This can be done using the command:
    * `pip3 install -r requirements.txt`.
11. Type `python3 app.py` in your Gitpod terminal to run your local site of this project.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/szomoru/MP4-DietPantry)


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
    - [Gergely Vig](https://github.com/szomoru/Extrahand-mp3)
   
    

### Media

- 
    

### Acknowledgements

-   My Mentor for helpful feedback.
-   Thanks to my family specially my wife who taken over our 4 kids while i was doing my studies. 