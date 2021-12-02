I chose Django Framework as it one of the most popular Python Restful API Framework since it will have more user base,
more articles and questions will be written about making it easier for me to find answers. As for drawback, I have no clue how
use it, or use python in general since I came from coding in C++/C#. I did include some Random name and address generator from online to make it easier to generate sample data.

For potential improvement, I have not yet implement the filter location, min-max price and language. I had a problem or I don't know the solution yet on Joining Tables in Django so I was not able to filter them. One solution I had thought of was just to all the fiields in the Doctor Model but this is not an elegant solution.

I would like to add some Unit Testing but that's another framework to learn, I had to focus on the develeopment since this is time restricted. I would also like to refactor and clean my implementations.

I would also take into account the locazation, but I have no Idea how to do this python. In my experience, we use resources files that contain localized string and never use static values. 

For production consideration, this is also the first time I created this kind of project. I had found a way to create an env settings for this project that included all the libraries I used. And would assume that we only need python to run this project.

One assumption I had was that the number below the address was phone numbers

Instructions
    1. Run env/bin/activate to install 3rd party libraries
    2. cd necktieapi
    3. Run python manage.py migrate
    4. Run python manage.py runserver

http://127.0.0.1:8000/doctor                        -> see all doctors
http://127.0.0.1:8000/doctor/<id>                   -> see single doctor by id
http://127.0.0.1:8000/doctor/?category=<category>   -> filter by category
http://127.0.0.1:8000/generate                      -> this will clear and generate 50 Doctor Items
http://127.0.0.1:8000/add                           -> to add doctor using post, sample json below

{
    "name": "Christopher Santos",
    "category": "General Practioner",
    "address": {
        "street": "722 13th Street Northeast",
        "city": "Washington"
    },
    "contacts": "96733296, 88792690",
    "fee": {
        "price": "710.00",
        "daysIncludingMedicine": 0
    }
}