<h1 align="center">Testing</h1>
<hr>

<span id="breaktop"></span>

[1. **Manual Testing**](#1-manual-testing)
-   [1.1 Visitor Goals](#1-1-visitor-goals)
-   [1.2 Consumer Goals (Unregistered)](#1-2-consumer-goals-unregistered)
-   [1.3 Returning Consumer Goals (Registered)](#1-3-returning-consumer-goals-registered)
-   [1.4 Administrator Goals](#1-4-administrator-goals)

[2. **Validators**](#2-validators)
-   [2.1 HTML Validator](#2-1-html-validator)
-   [2.2 CSS Validator](#2-2-css-validator)
-   [2.3 JSHint](#2-3-jshint)
-   [2.4 Python Validator (PEP8)](#2-4-python-validator-pep8)
-   [2.5 Lighthouse](#2-5-lighthouse)

[3. **Other Tests performed**](#3-other-tests-performed)
-   [3.1 Color Contrast Check](#3-1-color-contrast-check)
-   [3.2 Responsiveness](#3-2-responsiveness)
-   [3.3 Multi Browser Testing](#3-3-multi-browser-testing)

[4. **Bugs during development**](#4-bugs-during-development)
-   [4.1 E-mail sending](#4-1-email-sending)
-   [4.2 Am I responsive](#4-2-am-i-responsive)
-   [4.3 No Custom Error Pages](#4-3-no-custom-error-pages)
-   [4.4 Ruined up layout on product detail page](#4-4-ruined-up-layout-on-product-detail-page)
-   [4.5 Stripe warning on the console](#4-5-stripe-warning-on-the-console)



## **1. Manual Testing**

### **1-1 Visitor Goals**
1.  As a visitor, I want to access the website from any device (PC / notebook / tablet / mobile )
    -   **Testing:** The testing was performed first in the Chrome Devtools to check the responsivness and later the access was checked phisically different devices.
    -   **Result:** ***PASSED***

2.  As a visitor, I want to be able navigtae through the website easily
    -   **Testing:** I have performed a test, involving test users from the family to click on the links if they are working. I also gave them tasks to perform on the websitem like: purchase 1 protein powder and 2 vitamins etc. The structure of the pages are the same allover the webshop. The top Navigation bar is always visible and accessibla in every device sizes, so the possibility to browse on the site with different navbar menus is given all the time.

        ![Header](docs/navbar.jpg)
     
    -   **Result:** Since my test users could be taken consideration as first time visitors and they did not experienced any difficulties to perform my requests and they have not found any dead links i consider this test as ***PASSED***

3.  As a visitor i want to be able to get more background information about the company through socail media accounts
    -   **Testing:** All the social media links are present in the footer sectionallover the entire website. Though the footer is not fixed or sticky the visitor has to scroll down to the bottom of the page to see them. All the social media link has been tested allover the entire webpage and there were no issues with them. In every cases the icon represented social media platform opened in a separate window.

        ![Footer](docs/footer.jpg)

    -   **Result:** ***PASSED***

4.  As a visitor i want to be able to follow the company to see the lastest trends and news
    -   **Testing:** On all social media platform there is the possibility to follow the company. Also the company focus more on social media campaigns then e-mail campaigns.
    -   **Result:** ***PASSED***

5.  As a visitor i want to be able to contact the company and ask questions
    -   **Testing:** This also possible through the different social media platforms. If the contact is connected to an order, the order confirmation email contains all the correct contact informations.

        <details>
        <summary>Confirmation E-mail</summary>

        ![Confirmation Email](docs/test/order_contact.jpg)
            </details>

    -   **Result:** ***PASSED***

6.  As a visitor i want to be able to see all the products on the website to see what it can offer me
    -   **Testing:** By entering into the shop from the Home page the visitor can see all the products right way. From therepoint the visitor can sort the products, search for products or select different categories products. In the navigation bar - which is always visible on every screen - these possibilites are always given.

        <details>
        <summary>Sorting / Filtering / Searching Products</summary>

        ![Sorting Products](docs/test/sorting_products.jpg)

        ![Filtering Products](docs/test/filtering_products.jpg)

        ![Searching Products](docs/test/searching_products.jpg)
            </details>

    -   **Result:** ***PASSED***

7.  As a visitor i want to be able to search among the products or filter or sort them to get easily to a specific product
    -   **Testing:** The previous test description has already given the answer to this point. See **Visitor Goals nr 6**
    -   **Result:** ***PASSED***

8.  As a visitor i want to be able to get more information about the product (product description, price, image about the product ...)
    -   **Testing:** Every product has its on product detail page. The visitor can see all the detailed product information before place it into the shopping bag. The product detail page also provide extra information with the product reviews.

        <details>
        <summary>Product Detail</summary>

        ![Product Detail](docs/product_details.jpg)
            </details>

    -   **Result:** ***PASSED***

9.  As a visitor i want to be able to see what other peoples opinion about the product 
    -   **Testing:** The visitor can see all other user reviews on the product detail page independently if the visitor has an account or not with the store.
    -   **Result:** ***PASSED***

    
### **1-2 Consumer Goals (Unregistered)**
1.  As a consumer i want to able to fill up a virtual shopping bag and purchasing the content of it.
    -   **Testing:** The consumer has the possibility to place any of the products into the shopping bag from the detailed product page. The consumer has the possibility to change the quantity of the products or even delete them from the shopping bag. Moreover the consumer can return back to the product page and continue shopping if she/he wants. When the consumer satisfied with the content of the shopping bag she/he can purchase them through a **secure payment** process, which is provided by **STRIPE** 
    -   **Result:** All the above mentioned features has been actively tested and experienced no problem with them. The result of the consumer selected steps were continuesly cinfirmed by toasts. ***PASSED***

2.  As a consumer i want to have control over the content of the shopping bag until the very last step of purchasing (payment)
    -   **Testing:** The cosumer has the possibility to manipulate the content of the shopping bag until the last payment step. The different possibilities on different pages towards the payment process:
        - **Product Detail Page:** the consumer has the possibility to select the required quantity or return back to the Products 

        - **Shopping Bag Page:** the consumer has the possibility to **change** the quantity of the selected product, **remove** the selected product or **continue shopping** by selecting the keep shopping button. On this page the consumer can manipulate the different products individually

        - **Checkout Page:** at this stage the consumer cannot modify the products, but has the possibility to return back to the shopping bag by selecting the "Adjust bag" button at the bottom of the page

        <details>
        <summary>Porduct Detail / Shopping Bag / Checkout</summary>

        ![Product Detail](docs/product_details.jpg)

        ![Shopping Bag](docs/shopping_bag.jpg)

        ![Checkout](docs/checkout.jpg)
            </details>

    -   **Result:** ***PASSED***

3.  As a consumer i want to see the total value of my shopping bag including possible shipping fee
    -   **Testing:** through the purchasing process the **Shopping Bag** page and the **Checkout Page** give information about the **Sub-/Grand-Total** values and about the possible **Shipping fee**. The website provide **Free Shipping** if the order value is more than $50, otherwise the shipping fee is calculated as 10% of the order value.
    -   **Result:** all the above mentioned features were tested without any failure ***PASSED***

4.  As a consumer i want to have a fast and safe way to pay for the ordered products 
    -   **Testing:** 
        - Consumers can pay with credit card and the payment goes via Stripe payments. 
        - The stripe setup is based on a test environment. A consumer can fill in the number 4242 4242 4242 4242  to make a succesful payment. 
        - A Stripe webhook is implemented for extra secure payments. 
        - The consumer has to fill in personal information and delivery information. 
            - The required fields are full name, email address, phone number, country, town or city and street address 1. 
            - The email has a validator where someone has to use a @. 
            - The country field is a dropdown with all countries. 
    -   **Result:** The above mentioned payment system has been tested several times, since the beginning I had problem with that (problem description and solution can be found in this Testing document in an other chapter) ***PASSED***

5.  As a consumer i want to have continous feedback about my selected operations on the website.
    -   **Testing:** The consumer contonpusly get a toast message as a feedback the success of the selected operation. Type of Toasts: Error / Info / Success / Warning
    The attached image shows an example of a **Success Toast**. The Toast also contains the message what was success. Tis functionality was always a focus point of the test
        <details>
        <summary>Success Toasts</summary>

        ![Toast Success 1](docs/test/toast_success_1.jpg)     
        ![Toast Success 2](docs/test/toast_success_2.jpg)     
            </details>

    -   **Result:** ***PASSED***

6.  As a consumer i want to have confirmation e-mail about my purchase with order number.
    -   **Testing:** 
        - When the purchase is succeeded the consumer is redirected to the checkout success page. On the page there is an order summary and it mentions that the consumer will receive an email confirmation. 
        - The email is connected with gmail and when the purchase is made, an automatic confirmation is sent from **ci.gergely.vig@gmail.com**

            <details>
            <summary>Confirmation Email</summary>

            ![Confirmation Email](docs/test/order_contact.jpg)
                </details>

    -   **Result:** ***PASSED***

7.  As a consumer i want to have the possibility to create my own account to save my profile information and see my previous orders.
    -   **Testing:** The consumer can create her/his own account by signing up. Personal information, delivery information and the order history are visible on the Profile page. The consumer can change the delivery information by updating the details and the consumer can change the password or manage email

    -   **Result:** ***PASSED***


### **1-3 Returning Consumer Goals (Registered)**
1.  As a returning consumer I have the same goals than the not returning consumers and more
    -   **Testing:** All the functionality is accessable for a registered consumer as the not registered consumer. The registered consumer has actually more features in their account. They can see an extra menupoint called **Diet Library** in the header section. The registerd consumer also has the possibility to **leave a review** or **see the ordere history** or **add products to favourites**

    -   **Result:** authorization has been tested and worked correctly ***PASSED***

2.  As a returning customer I want to easily login/logout to my previously created account. I also want to see my order history
    -   **Testing:** The returning consumer can login and logout through the link under the profile icon in the navbar. The consumer has a double check for logging out.
    -   **Result:** ***PASSED***

3.  As a returning consumer i want to be able to create my own favourite products database and add/remove products to that. 
    -   **Testing:** As a registered returning consumer has the permission to add a product into the Favourites. This can happen on the **Products page** by clicking on the **Add to Favourites** button on the product card or on the **Product Detailed Page** b ya also clicking on the **Add to Favourites** button.
    -   **Result:** ***PASSED***

4.  As a returning consumer i want to have full control over my password, I want to be able to reset or change it.
    -   **Testing:** The password for a registered returning consumer can be changed by clicking the button on the profile page or by the login page.
    -   **Result:** ***PASSED***

5.  As a returning consumer i want to see others people feedback about the product I also want to be able to write my opinion about the product 
    -   **Testing:** As a registered returning consumer has the authorization to leave review for a product on the product detail page. 
    -   **Result:** ***PASSED***

    ***All related Returning Consumer Images:***

    <details>
    <summary>Not Registered User Navbar</summary>

    ![Not Registered User Navbar](docs/test/not_registered_user_navbar.jpg)
        </details>

    <details>
    <summary>Registered User Navbar</summary>

    ![Registered User Navbar](docs/test/registered_user_navbar.jpg)
        </details>

    <details>
    <summary>Not Registered User Product Detail Page</summary>

    ![Not Registered User Product Detail Page](docs/test/not_registered_user_product_detail.jpg)
        </details>

    <details>
    <summary>Registered User Product Detail Page</summary>

    ![Registered User Product Detail Page](docs/test/registered_user_product_detail.jpg)
        </details>

    <details>
    <summary>Not Registered User Product Detail Page - Review</summary>

    ![Not Registered User Product Detail Page - Review](docs/test/not_registered_user_product_detail_review.jpg)
        </details>

    <details>
    <summary>Registered User Product Detail Page - Review</summary>

    ![Registered User Product Detail Page - Review](docs/test/registered_user_product_detail_review.jpg)
        </details>


### **1-4 Administrator Goals**
1.  As an administartor i want to have control over the produts at the webshop. I want to be able to execute CRUD operation
    -   **Testing:** It is only the Admin who has the possibility to add product / modify product or even delete a product. Under the my profile menu it is only the admin who can see the Product management feature. By selecting it the Admin is able to uplad a new produc into the database. Under the Admin accountit is only the Admin who can dee the Delete and Edit buttons on the individual products. The normal users are not authorised to see them.
    -   **Result:** All the Create / Update and Delete functionality were tested and worked as it should be ***PASSED*** 

        <details>
        <summary>Admin Navbar</summary>

        ![Admin Navbar](docs/test/admin_navbar.jpg)
            </details>

        <details>
        <summary>Admin Product Detail Page</summary>

        ![Admin Product Detail Page](docs/test/admin_product_detail.jpg)
            </details>

        <details>
        <summary>Admin Product Management Page</summary>

        ![Admin Product Management Page](docs/test/admin_product_management.jpg)
            </details>

<div align="right">
    <a href="#breaktop">↥ Back to top!</a>
</div>

## **2. Validators**
The website itself were tested on several automatd testing applications. Below you can see a list about the perforemd tests and their results.

### **2-1 HTML Validator** [link](https://validator.w3.org/)
The page has been tested by URL and also by Direct code input methods. 
-   Some Results for pages:
    <details>
    <summary>Test Result</summary>

    ![Test Result 1](docs/test/html_validator_1.jpg)
        </details>
    <details>
    <summary>Test Result</summary>

    ![Test Result 1](docs/test/html_validator_2.jpg)
        </details>
    <details>
    <summary>Test Result</summary>

    ![Test Result 1](docs/test/html_validator_3.jpg)
        </details>

    I got the same results for the rest of the pages with 2 exceptions. 
    -   There was an uncorrect usage of p tag in the product detailed page. The problem has been solved
    -   Warning: the type attribute is unnecessary for JavaScript resource.  I left it because it does not effect the performance


### **2-2 CSS Validator** [link](https://jigsaw.w3.org/css-validator/)
-   base.css: NO PROBLEM
-   checkout.css: NO PROBLEM
-   profiles.css: NO PROBLEM

    <details>
    <summary>CSS Validator Result</summary>

    ![CSS Validator](docs/test/css_validator.jpg)
        </details>

    Unfortunately my country region was set to Hungarian, so the Validator webpage used the Hungarian language settings. I got the same result for each of 3 CSS.
    -   **Gratulálunk! Nincsenek hibák** means **Congratulations! There are no failures**


### **2-3 JSHint** [link](https://jshint.com/)
-   No errors found

### **2-4 Python Validator (PEP8)** 

**PEP8** [link](http://pep8online.com)
-   I have used the PEP8 also to validate python code.
    It has also found the long line and whitespace erros.
-   After correcting all the the found problems and leaving the exceptions (written under Flake8 section) the PEP8 online validator did not found any error.

**Flake8** (python extension to test Python for PEP8 compliance)

I have had run Flake8 to check if my code comply with the PEP8 standard.

-   **Result:**
    <details>
    <summary>Flake8 before</summary>

    ![Flake8 before](docs/test/flake8_origin.jpg)
        </details>

    -   As you can see after the first running of Flake8 it was full with problems. The majority of the problems were too long line and white space in lines. 

    <details>
    <summary>Flake8 after</summary>

    ![Flake8 after](docs/test/flake8_after.jpg)
        </details>

    -   The following error handling happened to get through the above result:
        -   Any errors related to files that were not created by me (autogenerated) I left untouched (eg: migrations)
        -   Errors mentioning that the variable 'e' is not used are remained untouched. The reason is that as i know the 'e' as a variable used to capture any erros from Stripe webhook handler.
        -   I have fixed all long line error, there are only 2 rows left that i could not split the lines. There i had 2 selections:
            -   I change the character number limit 2 90 instead of 79, but it would effect on the entire project
            -   After searching the internet i have found the possibility to add #noqa after the long line, which means the Flake8 doeas not consider it as a quality issue **I have selected this solution**  


### **2-5 Lighthouse**

-   #### I have used Lighthouse to check the performance of my site. Here you can see   some results:
    -   ### **Desktop:**
        <details>
        <summary>Lighthouse Desktop Result 1</summary>

        ![Lighthouse Desktop Result 1](docs/test/lighthouse_desktop_1.jpg)
            </details>

        <details>
        <summary>Lighthouse Desktop Result 2</summary>

        ![Lighthouse Desktop Result 2](docs/test/lighthouse_desktop_2.jpg)
            </details>

        <details>
        <summary>Lighthouse Desktop Result 3</summary>

        ![Lighthouse Desktop Result 3](docs/test/lighthouse_desktop_3.jpg)
            </details>

        <details>
        <summary>Lighthouse Desktop Result 4</summary>

        ![Lighthouse Desktop Result 4](docs/test/lighthouse_desktop_4.jpg)
            </details>

        <details>
        <summary>Lighthouse Desktop Result 5</summary>

        ![Lighthouse Desktop Result 5](docs/test/lighthouse_desktop_5.jpg)
            </details>


    -   ### **Mobile:**
        <details>
        <summary>Lighthouse Mobile Result 1</summary>

        ![Lighthouse Mobile Result 1](docs/test/lighthouse_mobile_1.jpg)
            </details>

        <details>
        <summary>Lighthouse Mobile Result 2</summary>

        ![Lighthouse Mobile Result 2](docs/test/lighthouse_mobile_2.jpg)
            </details>

        <details>
        <summary>Lighthouse Mobile Result 3</summary>

        ![Lighthouse Mobile Result 3](docs/test/lighthouse_mobile_3.jpg)
            </details>

        <details>
        <summary>Lighthouse Mobile Result 4</summary>

        ![Lighthouse Mobile Result 4](docs/test/lighthouse_mobile_4.jpg)
            </details>

        <details>
        <summary>Lighthouse Mobile Result 5</summary>

        ![Lighthouse Mobile Result 5](docs/test/lighthouse_mobile_5.jpg)
            </details>

-   ### **Conclusion:**   
    The overall performance for the website on Desktop was pretty good. Normally ove 90%, which I am happy with. However on mobile the performance poorer, so it requires improvements in the future. Right now it is around 70%+, the target should be 90%+ just like on Desktop.

<div align="right">
    <a href="#breaktop">↥ Back to top!</a>
</div>

## **3. Other Tests performed**

### **3-1 Color Contrast Check**
-   The first color scheme selection was very unlucky. IT resultesd a lot of Contrast Ratio issue all over the site. On the below pictures you can see how the contrast ratio was before. Thanks to my Assessro who highlighted this problem in my project.
    -   <details>
        <summary>Contrast Ratio Fail 1</summary>

        ![Contrast Ratio Fail 1](docs/test/contrast_ratio_1.JPG)
            </details>

        <details>
        <summary>Contrast Ratio Fail 2</summary>

        ![Contrast Ratio Fail 2](docs/test/contrast_ratio_2.JPG)
            </details>

-   I have kept the same primary colorset (dark colors) and picked a brand new secondary color set. I tried to select a color set which results 2 green pipes. Right now the color contrast looks like this:
    -   <details>
        <summary>Contrast Ratio GOOD 1</summary>

        ![Contrast Ratio GOOD 1](docs/test/contrast_ratio_good_1.jpg)
            </details>

        <details>
        <summary>Contrast Ratio GOOD 2</summary>

        ![Contrast Ratio GOOD 2](docs/test/contrast_ratio_good_2.jpg)
            </details>

- to check the contrast ratio i have used the Chrom DevTools

### **3-2 Responsiveness**
-   The inbuilt Chrome development tool was used through the whole development process to check the responsiveness of the website. It was handy, because it was always for me. The smallest width that i used was 320px. The first submission of the project has failed because the navigation bar has wrapped up on small screen and ruined the whole appearence. After correcting the problem there was an intensive testing of responsiveness 
-   I have used the [Lambdatest](https://www.lambdatest.com/) website to test on different equipments
-   [Exported PDF](docs/pdfs/mp4_diet_pantry_lambda_test.pdf)

### **3.3 Multi Browser Testing**
-   I have used the [Browserstack website](https://www.browserstack.com/) to check the browser compatibility of my website.
-   #### **Result:**
    The optimal browser for the website is Google Chrome browser. The website was tested on the following browsers:
    -   Microsoft Edge 99 - Windows 10: **PASS**
    -   Internet Explorer 11 - Windows 10: **FAILED**
    -   Opera 84 - Windows 10: **PASS**
    -   Yandex 14.12 - Windows 10:  **FAILED**
    -   Mozzilla 99 Beta - Windows 10: **PASS**
    -   Safari - IOS15: **PASS**
    -   Chrome 99 - Windoes 10: **PASS**

    ### Screenshot examples: ###
    -   <details>
        <summary>Iphone SE - Safari</summary>

        ![Lighthouse Desktop Result 1](docs/test/lighthouse_desktop_1.jpg)
            </details>

        <details>
        <summary>Ms Edge - Windoews 10</summary>

        ![Lighthouse Desktop Result 2](docs/test/lighthouse_desktop_2.jpg)
            </details>

        <details>
        <summary>Opera - Windoes 10</summary>

        ![Lighthouse Desktop Result 3](docs/test/lighthouse_desktop_3.jpg)
            </details>

<div align="right">
    <a href="#breaktop">↥ Back to top!</a>
</div>

## **4 Bugs during development**

### **4-1 E-mail sending**
-   One of the biggest issue during develop my final project was that the real e-mail sending did not work at all through gmail. This was a critical issue, since this failure made my site totally unusable a it was highlighted by my Assessor. Among others this was the major reason to fail with my project.
    -   **Problem Description:**
        During signing up to my website, the signup process went flawlessly until we get to the last step. The registration was successfull and the Success message appeared that an email with confirmation link has been sent. But that e-mail has never arrived, making the registration feature totally usless.
    -   **Solution:**
        After a lot of investigating thanks to **Ger** at the **Code Institute Tutor Group**, he figured out the the **DEVELOPMENT VARIABLE** has to be removed from the environment variables. Some reason it was nit enough to set the **VALUE = TRUE**, it had to be deleted totally. Even with this the Development Variable had a True Value. After removing that Variable the e-mail sending feature  worked flawlesly
    
### **4-2 Am I responsive**
-   **Problem Description:**
    [Am Irsponsive](http://ami.responsivedesign.is/) website was not able to render my deployed webpage. 
-   **Solution:**
    Thanks to **James** from the **Code Institute Tutor Team** we figured out that x-frame couse the problem that it cannot render. **James** could suggested me a Chrome extension, which is called, **Ignore X-Frame headers** and it solved the issue

### **4-3 No Custom Error Pages**
-   **Problem Description:**
    There were no custom Error Pages created. Thanks to my Assessor to highlight it to me.
-   **Solution:**
    Custom Error Pages has been created in the format of the website. The covered Errors are: Error 404 and Error 500

### **4-4 Ruined up layout on product detail page**
-   **Problem Description:**
    On the product detail page the product iamge and the product description bellow that could change the direction to row. This ruined up the layout of the page. This problem was discovered during testing procedure. The cause of the problem was that there were no flex direction defined and if the description text was short enough the direction was row. 
    <details>
    <summary>Product Detail page Error</summary>

    ![Contrast Ratio Fail 1](docs/test/new_product_error.JPG)
        </details>

-   **Solution:**
    There was a new **class** defined to style the related **div** and at the base css the **flex-direction** has been defined as **column**. This problem has never showed up again during testing. 

### **4-5 Stripe warning on the console**
-   **Problem Description:**
    During testing period I have not experienced any critical error displayed on the console. There was a warning generated related to Stripe. The reason was that there was only HTTP connection, not secured one 
    <details>
    <summary>Stripe Warning on Console</summary>

    ![Contrast Ratio Fail 1](docs/test/stripe_warning.JPG)
        </details>

-   **Solution:**
    Ass i changed http to https at the address the warning disappeared


<div align="right">
    <a href="#breaktop">↥ Back to top!</a>
</div>




