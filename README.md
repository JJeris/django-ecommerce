# django-ecommerce

A learning project for the Django framework.

Follows this [tutorial](https://www.youtube.com/watch?v=u6R4vBa7ZK4&list=PLCC34OHNcOtpRfBYk-8y0GMO4i1p1zn50).

Commands:
- source virt/Scripts/activate - activate the Python VE.
- python manage.py migrate
- python manage.py runserver - runs the server.
- python manage.py makemigrations - adds any changes made to the models in the store/models.py.

Episode #1 - .
Episode #2 - .
Episode #3 - .
Episode #4 - .


Episode #5 - Migration.

When changing the models in the store/models.py, you need to push a migration into the database.

Use python manage.py makemigrations adds the changes to the database, but python manage.py migrate pushes it to the database.

You can then access the changes model fields as you would any other field: model_name.field_name.

Episode #6 - Template.

In Django you are able to template your site with separate .html files. For example, you can add the navbar.html to the top of the home.html file by simply 'importing' it there.

Along side that you can extend other html documents (home.html) into other documents (base.html).


Any time you create a new page in Django its 3 step process:
- Need an html page: you create it int the template directory.
- Need a view: you define it as a function in the store/views.py file, that returns a rendered html page.
- Need a url: you simply add the newly created views page to the urlpatterns list, providing a path and a name for the view.

After that, simply provide a way for the user to access that file via a hyperlink.

Episode #7 - Login/Logout.

You use Django provided methods for login and logout - you only need an html doc for the login, but still need view function for both the login and logout.

Make sure to use the csrf_token and the POST method when making a log in form.

Episode #8 - Register users.

