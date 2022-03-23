# The Diet Pantry

<span id="breaktop"></span>

<h1 align="center"><img src="docs/amiresponsive_tiny.jpg"/></h1>

Welcome to My 4th milestone project at Code Institute. The Diet Pantry website is more or less the end of a long long and hard journey in the world of Coding. The purpose of this project 
to use build a full-stack site around a business logic. I have applied everything what i have learned at Code Institute. The technologies i have used for this project are: HTML, CSS, JAvaScript, Python and Django. Stripe handles online test payments and Heroku Postgres as a relational database.

This website is a fictional webshop for people who are following different type of diets. Sometimes it is really hard to find the right and trustable products for the different diets, so this website supposed to collect the tested and trusted dietary products. 

[Live site](http://mp4-diet-pantry.herokuapp.com) 

[Github link](https://github.com/szomoru/MP4-DietPantry) 


## Table of Contents

[1. **UX**](#1-ux)
+   [1.1 Project Goals](#1.1-project-goals)
+   [1.2 Business Goals](#1.2-business-goals)
+   [1.3 Visitor Goals](#1.3-visitor-goals)
+   [1.4 Target Audience](#1.4-target-audience)
+   [1.5 User Stories](#1.5-user-stories)
    +   [1.5.1 Visitor Goals](#1.5.1-visitor-goals)
    +   [1.5.2 Consumer Goals (Unregistered)](#1.5.2-consumer-goals)
    +   [1.5.3 Returning Consumer Goals (Registered)](#1.5.3-returning-consumer-goals)
    +   [1.5.4 Administrator Goals](#1.5.4-administrator-goals)

[2. **Features**](#2-features)

[3. **Database Design**](#3-database-design)

[4. **Technologies Used**](#4-technologies-used)

[5. **Testing**](#5-testing)

[6. **Deployment**](#6-deployment)

[7. **Credits**](#7-credits)


## 1. **UX**

<hr>

### **1.1 Project goals**
-   Making a full-stack site based around business logic used to control a centrally-owned database. 
-   The site provides an authentication mechanism and provides access to the site’s data based on the dataset. 
-   Making a full-stack site that uses HTML, CSS, JavaScript, Python + Django.
-   Creating a website that uses a relational database 
-   Creating a website that uses Stripe payments 
-   Creating a website that serves as a webshop to sell healthy food products   

### **1.2 Business goals**
-   Creating a secure and professional e-commerce website. 
-   Provide users acces to good quality healthy cooking/baking ingredients used in different type of diets 
-   Makes profit with selling healthy food products 
-   Makes healthy lifestyle and healthier food selection accessible to everyone

### **1.3 Visitor goals**
-   Get inspired beeing open minded to different diets and changing to a healthier food selection 
-   Safely purchase products on the webshop

### **1.4 Target audience**
-   Everyone who has been following, following or planning to follow a healthier diet.
-   Everyone who is interested to eat different
-   Everyone who has to eat different because of some health issues (eg Diabetes, High Blood Pressure, Overweight)

### **1.5 User stories**

-   #### **1.5.1 Visitor goals**
    1.  As a visitor, I want to access the website from any device (PC / notebook / tablet / mobile )
    2.  As a visitor, I want to be able navigtae through the website easily
    3.  As a visitor i want to be able to get more background information about the company through socail media accounts
    4.  As a visitor i want to be able to follow the company to see the lastest trends and news
    5.  As a visitor i want to be able to contact the company and ask questions
    6.  As a visitor i want to be able to see all the products on the website to see what it can offer me
    7.  As a visitor i want to be able to search among the products or filter or sort them to get easily to a specific product
    8.  As a visitor i want to be able to get more information about the product (product description, price, image about the product ...)
    9.  As a visitor i want to be able to see what other peoples opinion about the product 

-   #### **1.5.2 Consumer goals**
    1.  As a consumer i want to able to fill up a virtual shopping bag and purchasing the content of it.
    2.  As a consumer i want to have control over the content of the shopping bag until the very last step of purchasing (payment)
    3.  As a consumer i want to see the total value of my shopping bag including possible shipping fee
    4.  As a consumer i want to have a fast and safe way to pay for the ordered products 
    5.  As a consumer i want to have continous feedback about my selected operations on the website.
    6.  As a consumer i want to have confirmation e-mail about my purchase with order number.
    7.  As a consumer i want to have the possibility to create my own account to save my profile information and see my previous orders.

-   #### **1.5.4 Returning consumer goals**
    1.  As a returning consumer I have the same goals than the not returning consumers and more  
    2.  As a returning customer I want to easily login/logout to my previously created account. I also want to see my order history
    3.  As a returning consumer i want to be able to create my own favourite products database and add/remove products to that. 
    4.  As a returning consumer i want to have full control over my password, I want to be able to reset or change it.
    5.  As a returning consumer i want to see others people feedback about the product I also want to be able to write my opinion about the product 

-   #### **1.5.5 Administrator goals**
    1.  As an administartor i want to have control over the produts at the webshop. I want to be able to execute CRUD operations
        -   Create
        -   Read
        -   Update
        -   Delete

-   ### Design

    -   #### Colour Scheme
        There are used 2 main color groups on the website. Both groups contain 3 color codes:

        <details>
        <summary>Primary colors</summary>

        ![Primary colors](docs/primary_colors.jpg)

        </details>

        <details>
        <summary>Seconary colors</summary>

        ![Secondary colors](docs/secondary_colors.jpg)   

        </details>    

        Both color groups are used either background or font color. And there are also other blight colors are used on dark background to improve color contrast ratio.
            
        

    -   #### Typography
        There are 2 main font styles used through the webshop. The fonts were selected from the Google Font website. 
        <ul>
            <li><strong>Sacramento:</strong> This font is used only at the logo of the website. The reason is it is a handwriting style from the 50's - 60's. The reason to have that style for the logo that it gives more private feeling. It is needed since the name of the webshop refers to fill up someones pantry, which is already very private. </li>
            <li><strong>Lato:</strong> This font is used the rest of the website. It is easy to read and longer texts are also look very good with this font. It provides stabilty and seriousness feeling. The designer of the font is <i>Łukasz Dziedzic</i>. He says about his design: <i>“Male and female, serious but friendly. With the feeling of the Summer ...”</i>  </li>
            <li><strong>San-serif:</strong> This font is used as a Web safe font if the other 2 main fonts cannot be loaded some reason.</li>
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

    -   [profile.html WireFrame](c/wireframe/profile.png) 

    -   [bag.html WireFrame](docs/wireframe/shoppingbag.png) 

    -   [checkout.html WireFrame](docs/wireframe/checkout.png) 

    -   [checkout_success.html WireFrame](docs/wireframe/thankyou.png) 

    -   [keto.html / lowcarb.html /  highprotein.html / mediterranean.html WireFrame](docs/wireframe/dietlibrary.png)

<div align="right">
    <a href="#breaktop">↥ Back to top!</a>
</div>

## 2. **Features**

<hr>
 
 ### Existing Features ###

 ### Possible Future Features ###


<div align="right">
    <a href="#breaktop">↥ Back to top!</a>
</div>

## 3. **Database design**

<hr>

There were used relational databases for this project. During development phase i have used SQLite, and in production Heroku PostgreSQL was used. You can find attached the database schema on the link bellow.

![Database Design](docs/database_diagram.png)


<div align="right">
    <a href="#breaktop">↥ Back to top!</a>
</div>


## 4. **Technologies used**

<hr>

-   ### Languages ###
    -   [HTML5](https://en.wikipedia.org/wiki/HTML5)
        -   HTML5 provides the structure and the content of my website
    -   [CSS3](https://en.wikipedia.org/wiki/CSS)
        -   CSS3 provides the style of the HTML5 elements
    -   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
        -   JS provides the interactive part
    -   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
        -   The backend of the website is provided by Python
    -   [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine))
        -   Jinja is a web template language for python


-   ### Frameworks ###
    -   [Django](https://www.djangoproject.com/)
        -   Django is used as Python framework in this project


-   ### Libraries ###
    -   [Bootstrap CSS Framework](https://getbootstrap.com/)
        -   One of the largest pre-built library of HTML and CSS components. It was used every section of the webpage just like buttons or navigation ...
    -   [Font Awesome](https://fontawesome.com/)
        -   This library is used for getting icons
    -   [Google Fonts](https://fonts.google.com/)
        -   Font library
    -   [JQuery](https://jqueryui.com/)
        -   JavaScript library. MAinly used to simplify DOM manipulation and JS simplification


-   ### Editors ###
    -   [GitHub](https://github.com/)
        -   Remote code repository. It was use for source control 
    -   [dbDiagram](https://dbdiagram.io/)
        -   Plan and visualize database structures
    -   [Balsamiq](https://balsamiq.com/)
        -   Wireframe creator for visual testing


-   ### Tools ###
    -   [TinyPNG](https://tinypng.com/)
        -   Minimize image file size to deacrease the loading time, so maximize the webpage speed
    -   [Autoprefixer](https://autoprefixer.github.io/)
        -   Vendor prefixes to CSS rules 
    -   [Am I Responsive](http://ami.responsivedesign.is/)
        -   Creates demo views for ewsponsive design. Readme hero image was created by it.
    -   [Lambdatest](https://www.lambdatest.com/)
        -   Check website response across device types

-   ### Database Management ###
    -   [SQLite3](https://www.sqlite.org/)
        -   It was used as the Development Database
    -   [PostgreSQL](https://www.postgresql.org/)
        -   It was used as the production Database


-   ### Deployment platform(s) ###
    -   [Heroku](https://dashboard.heroku.com/)
        -   Remote hosting platform, it was used to hos my project
    -   [Amazon AWS](https://aws.amazon.com/)
        -   AWS Amazon is used to store static and media files.

-   ### Testing Tools ###
    -   [Chrome DevTool](https://developer.chrome.com/docs/devtools/open/)
        -   was used to check site responsiveness, and as a general debugger
    -   [W3C Markup Validator](https://validator.w3.org/)
        -   This Validator is used to check if there is any eror in the HTML5 code
    -   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
        -   This validator is used to check if there is any error in the CSS3 code
    -   [JShint](https://jshint.com/)
        -   JShint validator can find errors in JavaScript codes
    -   [PEP8](http://pep8online.com/) 
        -   was used to validate the python syntax.
    -   [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
        -   was used to check the site's Performance, Accessibility, Best Practices, and SEO.

<div align="right">
    <a href="#breaktop">↥ Back to top!</a>
</div>

## **5. Testing**

<hr>

You can find the detailed testing description by clicking on the link below:

[TESTING.MD]()

<div align="right">
    <a href="#breaktop">↥ Back to top!</a>
</div>

## 6. **Deployment**

<hr>

-   ### Requirements for Deployment

    * Python3
    * GitHub account
    * Heroku account
    * Stripe account
    * AWS Amazon account
    * An emailaccount preferably Gmail


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

<div align="right">
    <a href="#breaktop">↥ Back to top!</a>
</div>

## 7. **Credits**

<hr>

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

<div align="right">
    <a href="#breaktop">↥ Back to top!</a>
</div>