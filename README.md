# HotelCo - A Hotel Booking Website Application
## Stack:
### Front:
- HTML5 & CSS <br>
- Javascript <br>
- Django templates <br>
### Back:
- Python v. 3.9 <br>
- Django v. 3.1.5 <br>
## Installation:
### Setup:
Inside folder /HotelCo_project, on your terminal of choice, execute the following:

python manage.py makemigrations in order to generate the necessary files for the database setup;
python manage.py migrate to execute the previous setup files created;
python manage.py runserver to run the server.
As per default, the server adress is http://127.0.0.1:8000/.

Setup Django's deafult admin interface (optional):
In order to access the administrative interface via /admin, it is necessary to creat an administrative user.

To do that, inside /HotelCo_project execute python manage.py createsuperuser and follow the instructions.
## Requirement:
#### Your web application must utilize Django (including at least one model) on the back-end and JavaScript on the front-end.
Fulfilled the requirement the project has 4 django models and also 2 javascript files in the static folder
#### Your web application must be mobile-responsive.
 Fulfilled the requirement the project has is mobile responsive

---------------

## Features:

### Page routes:

#### / (home page)
Allows movies to be searched by their title.

Utilizes javascript to dynamically show the queried search after 500 milliseconds of text being typed.

Specific files for this page are: (this section title will be hidden for the features below)

- hotells.js
- index.html
---------------
#### `/register`

This helps the user to register with the Hotel Booking Application so that the user can login in and do hotel booking.

- `register.html`

---------------
#### `/login`

Allows the user to login in and enable the user to book hotel rooms

- `login.html`

---------------
#### `/logout`

Allows the user to logout from the hotel booking web application

---------------
#### `/option`

Displays the top 50 Hotels to the user according to the Check-in and Check-out date and also on the basis on the city
<br>
We provide with 3 options for booking a hotel:
- Economy Room
- Business Room
- Presidential Suit

- `option.html`

---------------
#### `/focus`

Shows 3 options for the selected hotel 

- `focus.html`

---------------
#### `/focus/<id>`

This is a Hotel focused room which is the last step inorder to book a hotel. On clicking the book button we get an alert and room is booked.

- `focus.html`

---------------
#### `/booking`

Displays a list of all of the user's booking.

- `booking.html`

---------------
### Views.py:
* index function
* login view
* logout view
* register
* option
* focus
* booking
---------------
### urls.py:
The url patterns used in this project are:
* "" : this takes to the index page
* "login": this takes to the login page
* "logout": this takes to the logout page
* "register": this takes to the register page
* "option": this takes to the option page
* "focus/<int:id>" this takes to the focus page
* "booking": this takes to the booking page
---------------
### User Authentication:

#### `/login`

Displays a page for the login of registered users.

- `login.html`

---------------
#### `/logout`

Allows logged in users to log out.

---------------
#### `/register`

Allows the registration of new users. 

- `register.html`

---------------

&nbsp;

# CS50W Capstone project requirements:

&nbsp;

## Distinctiveness and Complexity
### Why you believe your project satisfies the distinctiveness and complexity requirements, mentioned above.

The project was made from scratch, based on an original idea, following the requirements and trying to implement all methods learned through the lectures and problem sets.

## What’s contained in each file you created.

  - `/HotelCo/hotel/static` contains all javascript and css files.

  - `/HotelCo/hotel/templates/hotel` contains all .html files.

All files created and used in the project are described in the [Features](#features) section, with the exception of the following, used more generally:

  - `hotells.js` used to add javascript functionality to add to the user interface.

  - `style.css` used to store all the css specifications.

  - `script.js` used to add javascript functionality to add to the user interface.

## How to run your application.

Described in [Instalation](#instalation) section.

## Any other additional information the staff should know about your project.
Some observations:
- The project allows (and requires, initially) manually book hotel room to it's database.
- `models.py` allows to implement:
<br>
--->  User models to store user database
<br>
--->  Choice models to store checkin, checkout, city, duration into the database
<br>
--->  MyHotels models contains all the 50 hotel for user booking
<br>
--->  Booking models to store hotel name,type of room, price of room and duration of stay
<br>
<br>
To change it's default values, it is needed to access Django's admin interface via /admin.
