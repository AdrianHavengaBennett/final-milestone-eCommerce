# [Music'n'More](https://music-n-more.herokuapp.com/)

### Musical equipment E-commerce online store with so much more to offer registered users.

Music'n'More was founded by Adrian Havenga-Bennett in 2020 with a view of providing our customers with an immersive musical experience. The idea is to bring together fans of all genres and ages, from drummers to guitarists,
from djs to bassists, from those who want to learn an instrument to those who have years of experience. 

Joining our community will unlock the ability to chat to all sorts of music lovers and creators about anything you wish, from 50s to 90s, Electronic to Punk Rock, or Pop to Metal! 
Our Chat feature has the chatroom for you (like to see a particular chatroom? No problem, give us a shout and we'll coinsider adding it!). 

Start a blog about a product or a show, or just anything in general. Experienced musicians might start an advice blog. Avid giggers can get a group together to see some of the shows 
we offer our users at discount ticket prices. 

Start or continue your musical journey with us!

## UX
- This project is aimed at music lovers of all genres and ages who'd like to buy muiscal equipment or gig tickets at discounted prices, blog about everything music (or everything not music! You have full discretion), or just chat with like-minded music lovers in real time. This project provides it all, and under one roof.

### User Stories
- As a user, I would like to browse muiscal equipment across multiple categories, so that I can purchase what I want/need.
- As a user, I would like to be able to contact your office, so that I can clarify anything related to you and/or my order.
- As a user, I need to able to see some frequently-asked questions, so that I might be able to resolve my query without having to contact you.
- As a user, I would like to be able to create an account, so that I can unlock all of the features you offer.
- As a registered user, I would like to be able to choose a site-wide color-scheme from my profile page, so that I can customise my experience on your site.
- As a registered user, I would like to be able to chat with like-minded people in a chatroom suitable for our chosen musical style, so that I can ask questions or just make small talk.
- As a registered user, I would like to able to blog about your products and everything your site offers, with an aim of writing rich informative blogs for your site.
- As a registered user, I want a place to purchase discounted tickets to my favourite shows, so that I don't have to browse anywhere else and so that I can save some pennies.
- As a blog reader, I would like clear connections and links to products or shows blogged about, so that I can easily visit the page with a single click to see the product/show for myself.
- As a blog writer, I would like to link products and shows through my blog titles, so that my readers can see the product and show for themselves and make a decision on purchasing or not.
- As a musician and registered user, I would like to be able to blog about products and shows, so that I can help other people make wise decisions on purchases.
- As a musician and registered user, I would like to chat with people in real-time, so that I could perhaps give some advice to beginnners.

### Wireframes
- For this project, at the design phase, I decided to use [Balsamiq](https://balsamiq.com/).
- The wireframes can be found here:
[Desktop](https://www.dropbox.com/s/sfmcrf77k5esgej/ms_4_desktop-compressed.pdf?dl=0)
[Tablet](https://www.dropbox.com/s/buctbt9xxiereey/ms_4_tablet.pdf?dl=0)
[Mobile](https://www.dropbox.com/s/lwvh3qynnkc6mhw/ms_4_mobile-compressed.pdf?dl=0)
I was inspired by Salesforce and Whatsapp to include a doodle in the background. As a musically-inspired website, the choice was clear. Props to the artist, who is thanked in the appropriate section of this document.
Initial design was for a multicoloured background to make the doodle a little more interesting. But as I was about to implemented it, I had a thought on UX. So I decided to mould the themes with the background to give the user a choice of a site-wide colour scheme.

## Features

### Existing Features
- The site has a blog feature for registered users, and the ability to create blogs based to shows, products, or anything in general.
- The site has a chat feature for registered users with 13 different chatrooms available, based on genre.
- A shows section provides registered users with a list of shows and tickets offered at discount prices.
- Users have the ability to view products sorted by price - high or low.
- The site has a category section with 5 different categories to choose from.
- The site allows registered users to choose from 7 different site-wide color schemes, available on the profile page.
- The ability to change one's username, email address, and profile image, is also available within the profile.
- On wider screens, your profile image is displayed in the top-right corner, next to your basket and the ability to sign out of the site.
- The user has the ability to choose either delivery or click and collect, the latter then providing 2 further collection options.
- Handy breadcrumbs links provide a simple overview of you current location within the website.

### Features left to implement
- Chat feature is pretty basic but does a simple, effective job. Adding the ability to view an existing thread upon entering a room and also being able to tell if a user has left a room (see testing bug) will further add to the experience.
- The checkout process suggests an email will be sent as a confirmation of an order. This is not actually the case and is a feature left to implement.

## Technologies Used

## HTML5:
- https://en.wikipedia.org/wiki/HTML
- I used HTML because this project is a web application and HTML is required.

## CSS3:
- https://en.wikipedia.org/wiki/Cascading_Style_Sheets
- I used CSS to style the webpage's layout.

## SASS:
- https://en.wikipedia.org/wiki/Sass_(stylesheet_language)
- I decided to use Sass to simplify query nesting.

## Javascript:
- https://en.wikipedia.org/wiki/JavaScript
- I chose raw Javascript in some places because the django-channels docs uses raw Javascript.

## jQuery
- https://en.wikipedia.org/wiki/JQuery
- I used jQuery to simplify moving around the DOM and creating user interaction.

## Bootstrap
- https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)
- Bootstrap does a lot of the frontend heavy lifting for you, an easy choice to implement and realise your design.

## Python
- https://en.wikipedia.org/wiki/Python_(programming_language)
- I have used Python because the django framework runs on this technology.

## Django
- https://en.wikipedia.org/wiki/Django_(web_framework)
- I chose Django because it's a powerful framework, which does a lot of the heavy backend lifting for you, chief of which is the authentication system.

## Django-Channels
- https://channels.readthedocs.io/en/latest/index.html
- I used django-channels when creating the chat feature because channels allows the handling of websockets and adds an asynchronous layer underneath django (which runs synchronously). 

### And a whole host of other libraries, which can be found in the requirements.txt file.

## Testing

### Automated Testing

- A large majority of the back end code has been tested using Django's built-in testing suite. Nearly 80 unit tests have been written to test the code. Using coverage, I ran reports on my test code and concluded that the models, forms, and urls had coverage percentages of between 90 and 100. The views were quite a bit less and were subsequently tested via user testing to ensure functionality behaved as expected (see User Testing below). Test code can be found in each application's test folder, wherein they're appropriately named for each module tested. To run this test suite, I simply:
1. open a terminal (Windows PowerShell in my case),
1. cd (change directory) to my root project's directory (this should be the directory where your manage.py file lives), and
1. run the following command: `python manage.py test`
- This will run all test cases in all modules' test folders. To run only a certain application's tests, one could add the application's name and tests module onto the above command, like so:
`python manage.py test my_app.tests`
- To run a particular test file within that folder, one would type:
`python manage.py test my_app.tests.test_forms`
- Delving deeper, one could run only a particular test class within the application's test module, like so:
`python manage.py test my_app.tests.test_forms.TestUserRegisterForm`
- Finally, to run only a particular test in the class above, type:
`python manage.py test my_app.tests.test_forms.TestUserRegisterForm.test_does_this_thing_work`

### User Testing

- The following tests were undertaken to cover what the automated tests haven't, including a large percentage of the views' functionality.

#### General

Action | Expected outcome | Pass or Fail
------ | ---------------- | ------------
Clicking website icon | redirect to home page | PASS
Hovering a nav item in desktop | custom hover to highlight item | PASS
Hovering social icons in about section | icons change color | PASS
Navigating to a page | active nav link showing with underline | PASS
Successful contact form submit | thank you message shown | PASS
Clicking one of the FAQ | accordion dropdown with the answer | PASS
Clicking different FAQ | previous open accordion to close and new one opens | PASS
Grabbing, using Pegman, or zooming any Google Map | works as it should | PASS
Hovering a product on the home page | product image slight zoom | PASS
Adding product to basket | small digit appears next to basket icon, which itself turns red | PASS
Adding product to basket | success toast appears with current basket items visible in small window | PASS
Clicking basket icon | redirect to basket page | PASS
Clicking the plus icon for product or shows' tickets quantity | increments quantity | PASS
Clicking the minus icon for product or shows' tickets quantity | decrements quantity | PASS
Clicking plus or minus on 99 or 1 quantity respectively | icon greyed out, not able to add/remove any further | PASS
Choosing to sort products by price, low or high | products sorted by price low or high | PASS
Clicking previous or next on pagination links | loads previous/next page and grey out if on first/last page | PASS
Clicking "Contact Us" in FAQs page | redirect to contact form | PASS
Clicking any breadcrumb | navigate to page clicked | PASS
Choosing click and collect at checkout | charges updated and new location option visible | PASS
Clicking click and collect location at checkout | populates the form fields with correct address and contact info | PASS

#### While Logged Out

Action | Expected outcome | Pass or Fail
------ | ---------------- | ------------
Trying to access Chat, Blog, Shows, or Profile features | redirect to login page | PASS
Clicking to register through feature highlights on home page | redirect to registration page | PASS
Clicking on forgot password | redirect to input email form | PASS
Submitting forgot password form | email with reset link received in current Music'n'More registered email's inbox | PASS
Trying to submit any empty form | handy tooltips will advise which fields need to contain data | PASS

#### While Logged In

Action | Expected outcome | Pass or Fail
------ | ---------------- | ------------
Successful login | redirect to home page | PASS
Change color scheme in Profile | site-wide color-scheme change | PASS
Change profile image in Profile | new profile image displayed at top of page | PASS
Change profile image in Profile | open profile image in new tab and confirm image size is at max 300 x 300 pixels | PASS
Hardcode delete or edit blog url when you're not the author | warning that you cannot proceed | PASS
Clicking to "Blog About It" on product or show | new blog page loads with product or show pre-selected | PASS
Clicking "New Post" in Blog home | redirect to new blog post form | PASS
Saving new show or product blog | redirect to same blog with show or product name in title as a link to the show or title | PASS
Saving any blog after editing | redirect to same blog, now updated, with success toast displayed | PASS
Clicking on show or product blog title | takes you to the show or product details page | PASS
Searching existing products, faqs, blogs, or shows | product, faq, blog, or show filtered out | PASS
Searching non-existent products, faqs, blogs, or shows | not found message quoting what user searched for displayed along with a link back to all products, faqs, blogs, or shows | PASS
Clicking sign out | redirects to personal logout notification with ability to log back in | PASS

#### Bugs
- Adding a group_send() message to the disconnect() consumer in the chat application, when a user left the room, introduced a bug where the user who entered the room first couldn't leave before the user who entered after. This subsequently caused the websocket to crash on the server's side. Thus the functionality was removed until further understanding of the bug could be achieved and then rectified.

## Deployment

### Heroku
- The first thing I did was create fixture modules in each app for all of my data, like so:
Open new Windows cmd terminal (using Powershell was not possible because the json data 	saves with utf-8 character incompatibilities - something to note), navigate to project directory, 	activate venv (cd Scripts and run 'activate' - not 'Activate.ps1' as this is for Powershell only), 	then type:
`python manage.py dumpdata --format=json the-target-app > the-target-app_data.json`
I then repeated this for every module containing data which I wanted to save.
- Open Heroku in web browser and create new app.
- Add addons to heroku project - postgres hobby-dev and redis hobby-dev - the latter required for my chat functionality.
- Comment out old DATABASES in setting.py, replace with
`DATABASES = {"default": dj_database_url.parse("paste DATABASE_URL here (found in heroku 	config. vars.")}`
- Then run `python manage.py migrate` to run all migrations to new database.
- Now, load your data:
`python manage.py loaddata app_data` Note the order at which these are loaded. For example: A blog, needs a profile, which needs a user, so the load order is: user_data, then profile_data, then blog_data.
- Go to project's settings.py and add app-name.herokuapp.com to ALLOWED_HOSTS list, as well as 'localhost'.
`pip install pyscopg2-binary && dj_database_url && django-heroku` then:
`pip freeze > requirements.txt`
- Create Procfile and add `web: bin/start-pgbouncer-stunnel daphne milestone_four.asgi:application --port $PORT --bind 0.0.0.0` See additional notes below.
- Back in settings.py, import django_heroku at the top, then add this to the bottom of the file:
`django_heroku.settings(locals())
if 'DATABASE_URL' in os.environ:
    locals()['DATABASES']['default'] = dj_database_url.config(
        conn_max_age=django_heroku.MAX_CONN_AGE, ssl_require=False)`
- I add the following to ensure the correct database and redis server are running in production:
`if 'DATABASE_URL' in os.environ:
	    DATABASES = {
	        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
	    }
	else:
	    DATABASES = {
	        'default': {
	            'ENGINE': 'django.db.backends.sqlite3',
	            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	        }
	    }
if 'REDIS_URL' in os.environ:
      CHANNEL_LAYERS = {
      'default': {
	       'BACKEND': 'channels_redis.core.RedisChannelLayer',
         'CONFIG': {
             'hosts': [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
    },
}
else:
    CHANNEL_LAYERS = {
         'default': {
             'BACKEND': 'channels_redis.core.RedisChannelLayer',
             'CONFIG': {
                 'hosts': [(os.getenv('MY_IP'), 6379)],
             },
           },
    }`
- Generate new secret key (Google search: 'django secret key generator') and add to heroku config. vars
- Add new local environment variable: DEVELOPMENT = '1' to env.py
- In project's settings.py, change `DEBUG = 'DEVELOPMENT' in os.environ`
- Create an AWS account/sign in and head over to S3
- Create a new S3 bucket and IAM group and user with all applicable policies
- Back in the project, `pip install boto3 && django_storages`, then `pip freeze > requirements.txt`
- Add S3 access, secret key, maps api key, stripe keys, email, and USE_AWS=True to heroku config. vars. (if using an AWS S3 Bucket, make sure the config. vars. in heroku have no quotations; "" or '')
- Then add the following in settings.py:
`if 'USE_AWS' in os.environ:
	AWS_STORAGE_BUCKET_NAME = 'music-n-more'
	AWS_S3_REGION_NAME = 'eu-west-2' # EU (London)
	AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
	AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
	AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'`
- Then I created custom_storages.py at root level (where manage.py lives), and add the following:
`from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
class StaticStorage(S3Boto3Storage):
	location = settings.STATICFILES_LOCATION
class MediaStorage(S3Boto3Storage):
	location = settings.MEDIAFILES_LOCATION`
- Now add the following to the 'USE_AWS' condition:
`STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'`
- Finally, in the terminal, I type:
`git add .
git commit -m "meaningful message about deployment settings"
git push && git push heroku master (The latter if you have not setup automatic heroku pushes)`

#### Additional notes
I had to install some buildpacks for heroku (pgbouncer) to manage the number of connections to the database. This is because, due to using channels - which subsequently changes my project to an asynchronous project (asgi), the number of connections can spiral and cause exceptions. Postgres only provides 20 active connections on its free tier, so pgbouncer helps. From the docs: "PgBouncer maintains a pool of connections that your database transactions share." Running heroku pg in the terminal confirms 1/20 connections even after plenty of requests sent.

### Local
- To run this project locally, I will:
1. open PowerShell; and 
1. change directory to the project's root directory (the manage.py file will be in this directory); then
1. type the following command `.\manage.py runserver` ; then
1. copy the localhost address displayed in the windows command that pops up; then
1. open a new web browser.
1. I will then paste the location in the url bar at the top and press enter.

## Version Control
For this project, I have used Github for static version control:
- https://github.com/AdrianHavengaBennett/final-milestone-eCommerce

## Credits

### Code
- Most of the chat app's code comes straight from the django-channels docs tutorial and I edited pieces here and there to integrate the software into my project and my own personal needs.
- The checkout app's code was for the most part copied straight from the Code Institute modules.

### Media
- Background doodle courtesy of [@doodlebarn](https://www.freepik.com/doodlebarn)
- Chat images courtesy of [Online Tech Tips](https://www.online-tech-tips.com/), [PiniMG](https://pinimg.com/), [Billboard](https://billboard.com/), [123RF](https://123rf.com/), [DBSMusic](https://dbsmusic.co.uk/), [YTIMG](https://ytimg.com/), [Scarlet & Gray](https://www.unlvfreepress.com/), [8Tracks](https://8tracks.com/)
- Product images and product descriptions are courtesy of [Gear4Music](https://www.gear4music.com/)
- Category images are courtesy of [Wedding Wire](https://www.weddingwire.co.uk/), [Wesley's Chapel](https://www.wesleyschapel.org.uk/), [superprof](https://www.superprof.co.uk/), [shopify](https://www.shopify.co.uk/), [Guitar](https://guitar.com/)
- I do not own any of the above and use the content solely within an educational environment.

### Thanks
- Thanks go out to [The Code Institute](https://courses.codeinstitute.net/) student support team for helping me debug. You're all Saints!
- Special thanks to Justin Mitchel at [codingforentrepreneurs](https://www.codingforentrepreneurs.com/) and Corey Schafer at [CoreyMS](https://coreyms.com/), both of whose YouTube Django tutorials have been a great help to me as a top up to what I've learned from [The Code Institute](https://courses.codeinstitute.net/).
- Also thanks to all of the helpful answers from the kind folks over at [StackOverFlow](https://stackoverflow.com/).
- Honourable mention to my mentor, Nishant Kumar, for his patience and guidance throughout my Full Stack Web Development journey with The Code Institute.

I drew inspiration from my love of everything music-related.

Copyright 2020 - Adrian Havenga-Bennett
